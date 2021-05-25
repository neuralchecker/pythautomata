from pythautomata.guards.closed_interval_guard import ClosedIntervalGuard
from pythautomata.guards.union_guard import UnionGuard
from pythautomata.base_types.guard import Guard
from pythautomata.base_types.symbol import Symbol, SymbolInfinity as Inf, SymbolNegativeInfinity as NInf
from pythautomata.base_types.symbolic_state import SymbolicState
from pythautomata.boolean_algebra_learner.boolean_algebra_learner import BooleanAlgebraLearner

inf = Inf()
ninf = NInf()
class ClosedDiscreteIntervalLearner(BooleanAlgebraLearner):

    
    def learn(self, multidict: dict[SymbolicState, list[Symbol]]) -> list[tuple[Guard, SymbolicState]]:
        if(len(multidict) == 0):
            return []
        aux:dict[SymbolicState, list[list[Symbol]]] = {}
        ret:list[tuple[Guard, SymbolicState]] = []
        min_state:SymbolicState
        min = inf
        max_state:SymbolicState
        max = ninf
        for state, symbols in multidict.items():
            symbols.sort()
            aux[state] = [symbols]
            if min > symbols[0]:
                min_state = state
                min = symbols[0]
            if max < symbols[-1]:
                max_state = state
                max = symbols[0]
        aux[min_state][0].insert(0,ninf)
        aux[max_state][0].append(inf)

        #TODO repensarlo para intervalos abierto-cerrado o vice versa
        sym_list:list[list[Symbol]]
        for state, sym_list in aux.items():
            others:list[Symbol] = []
            for st, syms_l in aux.items():
                if st.name != state.name:
                    for l in syms_l:
                        others.extend(l)
            #TODO if others is not ordered, should repeat until we find a fix point. need benchmark in order to tell which is better
            others.sort()
            new_list = []
            while len(others) > 0 and len(sym_list) > 0:
                symbols = sym_list.pop(0)
                should_add_symbols_to_new = True
                for symbol in others:
                    if symbols[0] <= symbol and symbols[-1] > symbol:
                        should_add_symbols_to_new = False
                        left = []
                        s = symbols.pop(0)
                        while s < symbol:
                            left.append(s)
                            s = symbols.pop(0)
                        left.append(symbol)
                        new_list.append(left)
                        symbols.insert(0,s)
                        sym_list.insert(0, symbols)
                if should_add_symbols_to_new:
                    new_list.append(symbols)
            if len(new_list):
                sym_list = new_list
            #end while not fix
            intervalGuards = []
            for symbols in sym_list:
                if len(symbols):
                    intervalGuards.append(ClosedIntervalGuard(symbols[0],symbols[-1]))
            guard = UnionGuard(*intervalGuards)
            ret.append((guard, state))

        return ret
