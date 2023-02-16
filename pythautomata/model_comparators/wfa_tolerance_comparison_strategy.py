from pythautomata.model_comparators.wfa_comparison_strategy import WFAComparator
from pythautomata.utilities import pdfa_utils


class WFAToleranceComparator(WFAComparator):
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

    def equivalent_output(self, observation1, observation2) -> bool:
        return pdfa_utils.are_within_tolerance_limit(observation1, observation2, self.tolerance)

    def equivalent_values(self, value1, value2):
        return abs(value1 - value2) <= self.tolerance

    def next_tokens_equivalent_output(self, observation1, observation2) -> bool:
        return self.equivalent_output(observation1, observation2)
