from typing import Optional

from pythautomata.abstract.finite_automaton import FiniteAutomataComparator
from pythautomata.base_types.sequence import Sequence

class MooreMachineComparisonStrategy(FiniteAutomataComparator):
    def are_equivalent(self, model1, model2) -> bool:
        return super().are_equivalent(model1, model2)

    def get_counterexample_between(self, model1, model2) -> Optional[Sequence]:
        return super().get_counterexample_between(model1, model2)

    def equivalent_output(self, observation1, observation2) -> bool:
        return super().equivalent_output(observation1, observation2)