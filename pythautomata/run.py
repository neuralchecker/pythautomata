from pythautomata.automata.deterministic_finite_automaton import DeterministicFiniteAutomaton
from pythautomata.base_types.alphabet import Alphabet
from pythautomata.base_types.state import State
from pythautomata.base_types.symbol import SymbolStr
from pythautomata.model_comparators.dfa_comparison_strategy import DFAComparisonStrategy as DFAComparator
from pythautomata.model_exporters.dot_exporters.dfa_dot_exporting_strategy import DfaDotExportingStrategy
from pythautomata.model_exporters.image_exporters.image_exporting_strategy import ImageExportingStrategy
from pythautomata.model_exporters.standard_exporters.dfa_standard_dot_exporting_strategy import DfaStandardDotExportingStrategy


binaryAlphabet = Alphabet(frozenset((SymbolStr('0'), SymbolStr('1'))))
zero = binaryAlphabet['0']
one = binaryAlphabet['1']


def run():
    stateA = State("State A", True)
    stateB = State("State B")
    stateA.add_transition(one, stateA)
    stateA.add_transition(zero, stateB)
    stateB.add_transition(one, stateB)
    stateB.add_transition(zero, stateB)

    comparator = DFAComparator()

    dot_exporter = DfaDotExportingStrategy()
    standard_dot_exporter = DfaStandardDotExportingStrategy()

    dot_image_exporter = ImageExportingStrategy(dot_exporter, "png")
    standard_image_exporter = ImageExportingStrategy(
        standard_dot_exporter, "pdf")

    dfa = DeterministicFiniteAutomaton(binaryAlphabet, stateA,
                                       set([
                                           stateA, stateB]), comparator, "Tomita's grammar 1 automaton",
                                       exportingStrategies=[dot_image_exporter, standard_image_exporter, dot_exporter])

    dfa.export()


if __name__ == "__main__":
    run()
