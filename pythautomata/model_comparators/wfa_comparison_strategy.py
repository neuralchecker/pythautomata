from abc import abstractmethod
from typing import Optional

from pythautomata.abstract.finite_automaton import FiniteAutomataComparator
from pythautomata.base_types.sequence import Sequence
from pythautomata.automata.wheighted_automaton_definition.weighted_state import WeightedState


class WFAComparator(FiniteAutomataComparator):
    """
    Class containing a WFA Comparator Strategy based on next symbol distributions and a quantization parameter.

    Methods
    -------
    are_equivalent: bool
        returns true iif wfa1 is equivalent to wfa2 according to which partitions the distributions over next symbols belong.

    get_counterexample_between: Sequence
        returns a Sequence where the next token weights differ (or belong to different partitions)
    """

    def __init__(self) -> None:
        super().__init__()

    def are_equivalent(self, wfa1, wfa2) -> bool:
        return self.get_counterexample_between(wfa1, wfa2) is None

    def get_counterexample_between(self, wfa1, wfa2) -> Optional[Sequence]:
        if wfa1.alphabet != wfa2.alphabet:
            raise ValueError("Alphabets are not equivalent.")
        alphabet = wfa1.alphabet
        # initialPairs is a pair of initial states
        initial_pair: tuple[WeightedState, WeightedState] = (
            min(wfa1.initial_states), min(wfa2.initial_states))

        pairs_to_visit = [initial_pair]
        sequence_for_pairs = {initial_pair: Sequence()}
        visited_pairs: set[tuple[WeightedState, WeightedState]] = set()

        while pairs_to_visit:
            pair = pairs_to_visit[0]
            if not self._states_are_equivalent(pair[0], pair[1], alphabet):
                return sequence_for_pairs[pair]
            for symbol in alphabet.symbols:
                self._process_equivalence_iteration_with(symbol, pairs_to_visit,
                                                         visited_pairs, sequence_for_pairs)
            # pairs_to_visit.remove(pair)
            pairs_to_visit = list(
                filter(lambda x: not self._pair_equivalent_by_name(x, pair), pairs_to_visit))
            visited_pairs.add(pair)
        return None

    @abstractmethod
    def equivalent_output(self, observation1, observation2) -> bool:
        "Asumes observation is any collection of weights"
        raise NotImplementedError

    @abstractmethod
    def next_tokens_equivalent_output(self, observation1, observation2) -> bool:
        "Asumes observation is any collection of weights corresponding to the next token weights of a state"
        raise NotImplementedError

    def _pair_equivalent_by_name(self, states_pair1, states_pair2):
        return states_pair1[0].name == states_pair2[0].name and states_pair1[1].name == states_pair2[1].name

    def _states_are_equivalent(self, state1, state2, alphabet, ignore_initial_weight=True):
        r1 = self.equivalent_values(
            state1.initial_weight, state2.initial_weight)
        r2 = self.equivalent_values(state1.final_weight, state2.final_weight)
        r3 = self._check_transitions(state1, state2, alphabet)
        return (r1 or ignore_initial_weight) and r2 and r3

    @abstractmethod
    def equivalent_values(self, value1, value2):
        raise NotImplementedError

    def _check_transitions(self, state1, state2, alphabet):
        for symbol in alphabet.symbols:
            transitions1 = list(state1.transitions_set[symbol])
            transitions2 = list(state2.transitions_set[symbol])
            if len(transitions1) > 1 or len(transitions2) > 1:
                # TODO custom exception
                raise Exception(
                    "Eq method supported only for Deterministic Weighted FA")
            transition1 = transitions1[0]
            transition2 = transitions2[0]
            if not self.equivalent_values(transition1.weight, transition2.weight):
                return False
        return True

    def _process_equivalence_iteration_with(self, symbol, pairs_to_visit, visited_pairs, sequence_for_pairs):
        pair = pairs_to_visit[0]
        self_next_state = min(pair[0].next_states_for(symbol))
        other_next_state = min(pair[1].next_states_for(symbol))
        next_pair = (self_next_state, other_next_state)
        next_pair_in_pairs_to_visit = any(self._pair_equivalent_by_name(
            elem, next_pair) for elem in pairs_to_visit)
        next_pair_in_visited_pairs = any(self._pair_equivalent_by_name(
            elem, next_pair) for elem in visited_pairs)
        if not next_pair_in_pairs_to_visit and not next_pair_in_visited_pairs:
            sequence_for_pairs[next_pair] = sequence_for_pairs[pair] + symbol
            pairs_to_visit.append(next_pair)
