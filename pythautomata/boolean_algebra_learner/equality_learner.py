from pythautomata.guards.equality_guard import EqualityGuard
from pythautomata.guards.union_guard import UnionGuard
from pythautomata.base_types.guard import Guard
from pythautomata.base_types.symbol import Symbol
from pythautomata.base_types.symbolic_state import SymbolicState
from pythautomata.boolean_algebra_learner.boolean_algebra_learner import BooleanAlgebraLearner


class EqualityLearner(BooleanAlgebraLearner):
    def __init__(self):
        return

    def learn(self, multidict: dict[SymbolicState, list[Symbol]]) -> list[tuple[Guard, SymbolicState]]:
        ret:list[tuple[Guard, SymbolicState]] = []

        symbols:list[Symbol]
        for state, symbols in multidict.items():
            guard = UnionGuard(*[EqualityGuard(symbol) for symbol in symbols])
            ret.append((guard, state))
            
        return ret
