from typing import Optional

from pythautomata.abstract.finite_automaton import FiniteAutomataComparator
from pythautomata.base_types.sequence import Sequence
from pythautomata.automata.wheighted_automaton_definition.weighted_state import WeightedState
from pythautomata.utilities import pdfa_utils


class WFAToleranceComparator(FiniteAutomataComparator):
    """
    Class containing a WFA Comparator Strategy based on next symbol distributions and a tolerance parameter.

    Methods
    -------   
    are_equivalent: bool
        returns true iif wfa1 is equivalent to wfa2 according to a given tolerance

    get_counterexample_between: Sequence
        returns a Sequence where the next token weights differ (or its difference is greater than the tolerance)
    """

    def __init__(self, tolerance: float = 0) -> None:
        super().__init__()
        self.tolerance = tolerance

    def are_equivalent(self, wfa1, wfa2) -> bool:
        return self.get_counterexample_between(wfa1, wfa2) is None

    def equivalent_output(self, observation1, observation2) -> bool:
        return pdfa_utils.are_within_tolerance_limit(observation1, observation2, self.tolerance)

    def get_counterexample_between(self, wfa1, wfa2) -> Optional[Sequence]:
        tolerance = self.tolerance
        if wfa1.alphabet != wfa2.alphabet:
            raise ValueError("Alphabets are not equivalent.")
        self._alphabet = wfa1.alphabet
        # initialPairs is a pair of initial states
        initialPair: tuple[WeightedState, WeightedState] = (
            min(wfa1.initial_states), min(wfa2.initial_states))

        pairsToVisit = [initialPair]
        sequenceForPairs = {initialPair: Sequence()}
        visitedPairs: set[tuple[WeightedState, WeightedState]] = set()

        while pairsToVisit:
            pair = pairsToVisit[0]
            if not self._states_are_equivalent(pair[0], pair[1], tolerance):
                return sequenceForPairs[pair]
            for symbol in self._alphabet.symbols:
                self._process_equivalence_iteration_with(symbol, pairsToVisit,
                                                         visitedPairs, sequenceForPairs)
            # pairsToVisit.remove(pair)
            pairsToVisit = list(
                filter(lambda x: not self._pair_equivalent_by_name(x, pair), pairsToVisit))
            visitedPairs.add(pair)
        return None

    def _pair_equivalent_by_name(self, states_pair1, states_pair2):
        return states_pair1[0].name == states_pair2[0].name and states_pair1[1].name == states_pair2[1].name

    def _states_are_equivalent(self, state1, state2, tolerance, ignore_initial_weight=True):
        r1 = self._within_tolerance(
            state1.initial_weight, state2.initial_weight, tolerance)
        r2 = self._within_tolerance(
            state1.final_weight, state2.final_weight, tolerance)
        r3 = self._check_transitions(state1, state2, tolerance)
        return (r1 or ignore_initial_weight) and r2 and r3

    def _within_tolerance(self, value1, value2, tolerance):
        return abs(value1 - value2) <= tolerance

    def _check_transitions(self, state1, state2, tolerance):
        for symbol in self._alphabet.symbols:
            transitions1 = list(state1.transitions_set[symbol])
            transitions2 = list(state2.transitions_set[symbol])
            if len(transitions1) > 1 or len(transitions2) > 1:
                # TODO custom exception
                raise Exception(
                    "Eq method supported only for Deterministic Weighted FA")
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
        nextPair_in_pairs_to_visit = any(self._pair_equivalent_by_name(
            elem, nextPair) for elem in pairs_to_visit)
        nextPair_in_visited_pairs = any(self._pair_equivalent_by_name(
            elem, nextPair) for elem in visited_pairs)
        if not nextPair_in_pairs_to_visit and not nextPair_in_visited_pairs:
            sequence_for_pairs[nextPair] = sequence_for_pairs[pair] + symbol
            pairs_to_visit.append(nextPair)
