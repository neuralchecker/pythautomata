from pythautomata.automata.moore_machine_automaton import MooreMachineAutomaton
from pythautomata.base_types.alphabet import Alphabet
from pythautomata.base_types.moore_state import MooreState
from pythautomata.base_types.symbol import SymbolStr
from pythautomata.model_comparators.moore_machine_comparison_strategy import MooreMachineComparisonStrategy
from pythautomata.model_exporters.dot_exporting_mm_strategy import DotExportingMMStrategy
from pythautomata.model_exporters.dot_exporting_strategy import DotExportingStrategy
from pythautomata.model_exporters.image_exporting_mm_strategy import ImageExportingMMStrategy
from pythautomata.utilities.simple_dfa_generator import generate_dfa
from pythautomata.utilities.nicaud_dfa_generator import generate_dfa as generate_dfa_nicaud
from pythautomata.utilities.simple_mm_generator import generate_moore_machine


def run():
    
#     generatedAutomata = generate_dfa(Alphabet(
#             frozenset([SymbolStr('0'), SymbolStr('1')])), 10, [DotExportingStrategy()])
#     generatedAutomata.export("./test.dot")

#     generatedAutomataNicaud = generate_dfa_nicaud(Alphabet(
#             frozenset([SymbolStr('0'), SymbolStr('1')])), 10, [DotExportingStrategy()])
    
#     generatedAutomataNicaud.export("./test.dot")

    # abAlphabet = Alphabet(frozenset((SymbolStr('a'), SymbolStr('b'))))
    # abcAlphabet = Alphabet(
    #     frozenset((SymbolStr('a'), SymbolStr('b'), SymbolStr('c'))))

    # a = abAlphabet['a']
    # b = abAlphabet['b']

    # state0 = MooreState(
    #     "State 0", abcAlphabet['a'])
    # state1 = MooreState(
    #     "State 1", abcAlphabet['b'])
    # state2 = MooreState(
    #     "State 2", abcAlphabet['c'])

    # state0.add_transition(a, state1)
    # state0.add_transition(b, state2)
    # state1.add_transition(a, state2)
    # state1.add_transition(b, state0)
    # state2.add_transition(a, state0)
    # state2.add_transition(b, state1)

    # exporting = [DotExportingMMStrategy()]

    # mm = MooreMachineAutomaton(abAlphabet, abcAlphabet, state0,
    #                                 set([state0, state1, state2]), MooreMachineComparisonStrategy(), "3 States Moore Machine", [DotExportingMMStrategy()])

    # mm.export("./test.dot")

    generatedMooreMachine = generate_moore_machine(Alphabet(
            frozenset([SymbolStr('0'), SymbolStr('1')])), Alphabet(
            frozenset([SymbolStr('primero'), SymbolStr('segundo'), SymbolStr('tercero')])), 25, [DotExportingMMStrategy()])    
    generatedMooreMachine.export("./test")


if __name__ == '__main__':
    run()