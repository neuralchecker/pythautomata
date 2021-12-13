from pythautomata.base_types.guard import Guard
from pythautomata.base_types.symbol import Symbol
from pythautomata.base_types.symbol import SymbolInfinity as Inf
from pythautomata.base_types.symbol import SymbolNegativeInfinity as NInf
from pythautomata.base_types.symbolic_state import SymbolicState
from pythautomata.boolean_algebra_learner.boolean_algebra_learner import \
    BooleanAlgebraLearner
from pythautomata.guards.closed_interval_guard import ClosedIntervalGuard
from pythautomata.guards.union_guard import UnionGuard

inf = Inf()
ninf = NInf()
class ClosedDiscreteIntervalLearner(BooleanAlgebraLearner):

    
    def learn(self, multidict: dict[SymbolicState, list[Symbol]]) -> list[tuple[Guard, SymbolicState]]:
        if(len(multidict) == 0):
            return []
        ret:list[tuple[Guard, SymbolicState]] = []
        dict_state_to_symbol_intervals = self._init_dict_state_symbol_intervals(multidict)
        state_intervals:dict[SymbolicState,list[list[Symbol]]] = {}
        #TODO repensarlo para intervalos abierto-cerrado o vice versa
        intervals:list[list[Symbol]]
        for state, intrs in dict_state_to_symbol_intervals.items():
            intervals = [intr.copy() for intr in intrs]
            others:list[Symbol] = []
            for st, syms_l in dict_state_to_symbol_intervals.items():
                if st.name != state.name:
                    for l in syms_l:
                        others.extend(l)
            others.sort()
            
            new_intervals:list[list[Symbol]] = []
            init_len = len(intervals)
            is_fixed_point = False
            while len(intervals):
                if len(others) == 0:
                    break
                if is_fixed_point:
                    break
                is_fixed_point = True
                right = intervals[0]
                #right because I will split the interval in left of other and right of other
                for other in others:
                    if right[0] > other:
                        # then @other is smaller than every symbol in right
                        continue 
                    if right[-1] < other:
                        # then @other and the rest of the symbols in @others are bigger than those in the right interval
                        break
                    is_fixed_point = False
                    left = []
                    while True:
                        s=right[0]
                        #if @s is bigger than @other then i've found the symbol in which i should break the interval
                        if s > other:
                            #the interval will be between the first element of left and the symbol that comes before @other
                            other_copy = other.copy()
                            other_copy.add_to_value(-1)
                            left.append(other_copy)
                            new_intervals.append(left)
                            break
                        #if not, should remove s form right and add it to right
                        left.append(right.pop(0))
            new_intervals.extend(intervals)
            assert(len(new_intervals)>=init_len)
            state_intervals[state]=new_intervals

            
        
        self._add_infinities_to_state_intervals(state_intervals)
        for state, intervals in state_intervals.items():
            interval_guards = []
            for interval in intervals:
                assert(len(interval))
                interval_guards.append(ClosedIntervalGuard(interval[0],interval[-1]))
            guard = UnionGuard(*interval_guards)
            ret.append((guard, state))
        
        return ret

    def _add_infinities_to_state_intervals(self, state_intervals: dict[SymbolicState, list[list[Symbol]]]):
        min_state:SymbolicState
        min:Symbol = inf
        max_state:SymbolicState
        max:Symbol = ninf
        for state, intervals in state_intervals.items():
            assert(len(intervals))
            if min > intervals[0][0]:
                min = intervals[0][0]
                min_state = state
            if max < intervals[-1][-1]:
                max = intervals[-1][-1]
                max_state = state
        state_intervals[min_state][0].insert(0, ninf)
        state_intervals[max_state][-1].append(inf)


    def _init_dict_state_symbol_intervals(self, multidict: dict[SymbolicState, list[Symbol]]):
        dict_state_to_symbol_intervals:dict[SymbolicState, list[list[Symbol]]] = {}

        for state, symbols in multidict.items():
            symbols.sort()
            dict_state_to_symbol_intervals[state] = [symbols]
        return dict_state_to_symbol_intervals
