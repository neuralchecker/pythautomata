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

    def equivalent_output(self, observation1, observation2) -> bool:
        return pdfa_utils.are_in_same_partition(observation1, observation2, self.partitions)

    def equivalent_values(self, value1, value2):
        part1 = pdfa_utils.get_partition(value1, self.partitions)
        part2 = pdfa_utils.get_partition(value2, self.partitions)
        return part1 - part2 == 0
