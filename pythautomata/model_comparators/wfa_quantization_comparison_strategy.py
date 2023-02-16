from pythautomata.model_comparators.wfa_comparison_strategy import WFAComparator
from pythautomata.utilities import pdfa_utils


class WFAQuantizationComparator(WFAComparator):
    """
    Class containing a WFA Comparator Strategy based on next symbol distributions and a quantization parameter.

    Methods
    -------   
    are_equivalent: bool
        returns true iif wfa1 is equivalent to wfa2 according to which partitions the distributions over next symbols belong.

    get_counterexample_between: Sequence
        returns a Sequence where the next token weights differ (or belong to different partitions)
    """

    def __init__(self, partitions: float) -> None:
        super().__init__()
        self.partitions = partitions
        self._partition_cache = dict()

    def equivalent_output(self, observation1, observation2) -> bool:
        assert (len(observation1) == len(observation2))
        for i in range(len(observation1)):
            if self._get_partition(observation1[i]) != self._get_partition(observation2[i]):
                return False
        return True

    def equivalent_values(self, value1, value2):
        part1 = self._get_partition(value1)
        part2 = self._get_partition(value2)
        return part1 - part2 == 0

    def _get_partition(self, value):
        if value in self._partition_cache:
            return self._partition_cache[value]
        else:
            partition = pdfa_utils.get_quantized_interval_partition(
                value, self.partitions)
            self._partition_cache[value] = partition
            return partition

    def next_tokens_equivalent_output(self, observation1, observation2) -> bool:
        return self.equivalent_output(observation1, observation2)
