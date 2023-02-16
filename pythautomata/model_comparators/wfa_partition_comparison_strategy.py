from pythautomata.model_comparators.wfa_comparison_strategy import WFAComparator
from pythautomata.utilities import pdfa_utils
from pythautomata.utilities.probability_partitioner import ProbabilityPartitioner
from pythautomata.automata.wheighted_automaton_definition.weighted_state import WeightedState


class WFAPartitionComparator(WFAComparator):
    """
    Class containing a WFA Comparator Strategy based on partitioning of next symbol distributions.

    Methods
    -------   
    are_equivalent: bool
        returns true iif wfa1 is equivalent to wfa2 according to arg max criterion

    get_counterexample_between: Sequence
        returns a Sequence where the arg max of next token weights differ
    """

    def __init__(self, partitioner: ProbabilityPartitioner) -> None:
        super().__init__()
        self._partitioner = partitioner

    def _get_probability_distribution(self, state: WeightedState):
        _, probs, _ = state.get_all_symbol_weights()
        return probs

    def _states_are_equivalent(self, state1, state2, alphabet, ignore_initial_weight=True):
        r1 = state1.initial_weight == state2.initial_weight
        r2 = self._partitioner.are_in_same_partition(self._get_probability_distribution(
            state1), self._get_probability_distribution(state2))
        return (r1 or ignore_initial_weight) and r2

    def next_tokens_equivalent_output(self, observation1, observation2) -> bool:
        return self._partitioner.are_in_same_partition(observation1, observation2)

    def equivalent_output(self, observation1, observation2) -> bool:
        raise NotImplemented
        return pdfa_utils.have_same_argmax(observation1, observation2)

    def equivalent_values(self, value1, value2):
        raise NotImplemented
        return abs(value1 - value2) <= self.tolerance
