from typing import Optional

from pythautomata.abstract.finite_automaton import FiniteAutomataComparator
from pythautomata.base_types.sequence import Sequence
from pythautomata.base_types.state import State


class WFAComparator(FiniteAutomataComparator):
    """
    Class containing a WFA Comparator Strategy.

    Methods
    -------   
    are_equivalent: bool
        returns true iif wfa1 is equivalent to wfa2
    
    get_counterexample_between: Sequence
        returns a Sequence where the next token weights differ (or its difference is greater than the tolerance)
    """
    def are_equivalent(self, wfa1, wfa2, tolerance = 0) -> bool:
        return self.get_counterexample_between(wfa1, wfa2, tolerance) is None

    def get_counterexample_between(self, wfa1, wfa2, tolerance = 0) -> Optional[Sequence]:
        if wfa1.alphabet != wfa2.alphabet:
            raise ValueError("Alphabets are not equivalent.")
        self._alphabet = wfa1.alphabet
        # initialPairs is an arbitrary pair of states
        initialPair: tuple[State, State] = (
            min(wfa1.initial_states), min(wfa2.initial_states))

        pairsToVisit = [initialPair]
        sequenceForPairs = {initialPair: Sequence()}
        visitedPairs: set[tuple[State, State]] = set()

        while pairsToVisit:
            pair = pairsToVisit[0]
            if not self._states_are_equivalent(pair[0],pair[1], tolerance):
                return sequenceForPairs[pair]
            for symbol in wfa1.alphabet.symbols:
                self._process_equivalence_iteration_with(symbol, pairsToVisit,
                                                         visitedPairs, sequenceForPairs)
            pairsToVisit.remove(pair)
            visitedPairs.add(pair)
        return None
    
    def _states_are_equivalent(self, state1, state2, tolerance):        
        r1 = self._within_tolerance(state1.initial_weight, state2.initial_weight, tolerance)
        r2 = self._within_tolerance(state1.final_weight, state2.final_weight, tolerance)
        r3 = self._check_transitions(state1, state2, tolerance)
        return r1 and r2 and r3
    
    def _within_tolerance(self, value1, value2, tolerance):
        return abs(value1 - value2) <= tolerance
    
    def _check_transitions(self, state1, state2, tolerance):
        for symbol in self._alphabet:
            transitions1 = state1.transitions[symbol]
            transitions2 = state2.transitions[symbol]
            if len(transitions1) > 1 or len(transitions2) > 1:
                # TODO custom exception
                raise Exception("Eq method supported only for Deterministic Weighted FA")
            transition1 = transitions1[0]
            transition2 = transitions2[0]
            if not self._within_tolerance(transition1.weight, transition2.weight, tolerance):
                return False
        return True

    def _process_equivalence_iteration_with(self, symbol, pairs_to_visit, visited_pairs, sequence_for_pairs):
        pair = pairs_to_visit[0]
        selfNextState = min(pair[0].next_states_for(symbol))
        otherNextState = min(pair[1].next_states_for(symbol))
        nextPair = (selfNextState, otherNextState)
        if nextPair not in pairs_to_visit and nextPair not in visited_pairs:
            sequence_for_pairs[nextPair] = sequence_for_pairs[pair] + symbol
            pairs_to_visit.append(nextPair)
