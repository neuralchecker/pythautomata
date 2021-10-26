from typing import Optional

from pythautomata.abstract.finite_automaton import FiniteAutomataComparator
from pythautomata.base_types.sequence import Sequence
from pythautomata.base_types.state import State


class WFAComparisonStrategy(FiniteAutomataComparator):
    """
    Class containing a WFA Comparison Strategy.

    Methods
    -------   
    are_equivalent: bool
        returns true iif wfa1 is equivalent to wfa2
    
    get_counterexample_between: Sequence
        returns a Sequence where the next token weights differ
    """
    def are_equivalent(self, wfa1, wfa2) -> bool:
        return self.get_counterexample_between(wfa1, wfa2) is None

    def get_counterexample_between(self, wfa1, wfa2) -> Optional[Sequence]:
        if wfa1.alphabet != wfa2.alphabet:
            raise ValueError("Alphabets are not equivalent.")

        # initialPairs is an arbitrary pair of states
        initialPair: tuple[State, State] = (
            min(wfa1.initial_states), min(wfa2.initial_states))

        pairsToVisit = [initialPair]
        sequenceForPairs = {initialPair: Sequence()}
        visitedPairs: set[tuple[State, State]] = set()

        while pairsToVisit:
            pair = pairsToVisit[0]
            if not pair[0] == pair[1]:
                return sequenceForPairs[pair]
            for symbol in wfa1.alphabet.symbols:
                self._process_equivalence_iteration_with(symbol, pairsToVisit,
                                                         visitedPairs, sequenceForPairs)
            pairsToVisit.remove(pair)
            visitedPairs.add(pair)
        return None

    def _process_equivalence_iteration_with(self, symbol, pairs_to_visit, visited_pairs, sequence_for_pairs):
        pair = pairs_to_visit[0]
        selfNextState = min(pair[0].next_states_for(symbol))
        otherNextState = min(pair[1].next_states_for(symbol))
        nextPair = (selfNextState, otherNextState)
        if nextPair not in pairs_to_visit and nextPair not in visited_pairs:
            sequence_for_pairs[nextPair] = sequence_for_pairs[pair] + symbol
            pairs_to_visit.append(nextPair)
