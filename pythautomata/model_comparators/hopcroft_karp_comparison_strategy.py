import utilities.automata_comparator as AutomataComparator
from abstract.model_comparison_strategy import ModelComparisonStrategy


class HopcroftKarpComparisonStrategy(ModelComparisonStrategy):
    def are_equivalent(self, automaton1, automaton2):
        return AutomataComparator.are_equivalent(automaton1, automaton2)

    def get_counterexample_between(self, automaton1, automaton2):
        return AutomataComparator.get_counterexample_between(automaton1, automaton2)
