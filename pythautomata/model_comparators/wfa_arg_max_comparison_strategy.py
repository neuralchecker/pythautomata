from pythautomata.model_comparators.wfa_comparison_strategy import WFAComparator
from pythautomata.utilities import pdfa_utils


class WFAArgMaxComparator(WFAComparator):
    """
    Class containing a WFA Comparator Strategy based on arg max value of next symbol distributions.

    Methods
    -------   
    are_equivalent: bool
        returns true iif wfa1 is equivalent to wfa2 according to arg max criterion

    get_counterexample_between: Sequence
        returns a Sequence where the arg max of next token weights differ
    """

    def __init__(self) -> None:
        raise NotImplemented
        super().__init__()

    def equivalent_output(self, observation1, observation2) -> bool:
        raise NotImplemented
        return pdfa_utils.have_same_argmax(observation1, observation2)

    def equivalent_values(self, value1, value2):
        raise NotImplemented
        return abs(value1 - value2) <= self.tolerance
