from pythautomata.base_types.state import State
from pythautomata.base_types.symbol import SymbolStr
from pythautomata.base_types.alphabet import Alphabet

from pythautomata.automata.moore_machine_automaton import MooreMachineAutomaton
from pythautomata.base_types.moore_state import MooreState

from pythautomata.model_comparators.dfa_comparison_strategy import DFAComparisonStrategy as DFAComparison

from pythautomata.utilities.automata_converter import AutomataConverter

abAlphabet = Alphabet(frozenset((SymbolStr('a'), SymbolStr('b'))))
abcAlphabet = Alphabet(frozenset((SymbolStr('a'), SymbolStr('b'), SymbolStr('c'))))


# TODO: DOCUMENT AND TEST


class SampleMooreMachines:

    """
    Class containing sample Moore Machines

    Methods
    -------

    """
    @staticmethod
    def get_a_symbol():
        return 'a'
    
    @staticmethod
    def get_b_symbol():
        return 'b'

    @staticmethod
    def get_c_symbol():
        return 'c'

    @staticmethod
    def get_all_automata():
        return [
            SampleMooreMachines.get_3_states_automaton(),
            #! Estos ejemplos fallan las pruebas
            # SampleMooreMachines.get_3_states_automaton_wrong_alphabet(),
            # SampleMooreMachines.get_3_states_automaton_non_deterministic()
        ]

    @staticmethod
    def get_3_states_automaton():
        a = abAlphabet[SampleMooreMachines.get_a_symbol()]
        b = abAlphabet[SampleMooreMachines.get_b_symbol()]

        state0 = MooreState("State 0", abcAlphabet[SampleMooreMachines.get_a_symbol()]);
        state1 = MooreState("State 1", abcAlphabet[SampleMooreMachines.get_b_symbol()]);
        state2 = MooreState("State 2", abcAlphabet[SampleMooreMachines.get_c_symbol()]);

        state0.add_transition(a, state1)
        state0.add_transition(b, state2)
        state1.add_transition(a, state2)
        state1.add_transition(b, state0)
        state2.add_transition(a, state0)
        state2.add_transition(b, state1)

        return MooreMachineAutomaton(abAlphabet, abcAlphabet, state0, 
                set([state0, state1, state2]), DFAComparison(), "3 States Moore Machine")

    @staticmethod
    def get_3_states_automaton_wrong_alphabet():
        a = abAlphabet[SampleMooreMachines.get_a_symbol()]
        b = abAlphabet[SampleMooreMachines.get_b_symbol()]

        state0 = MooreState("State 0", abcAlphabet[SampleMooreMachines.get_a_symbol()]);
        state1 = MooreState("State 1", abcAlphabet[SampleMooreMachines.get_b_symbol()]);
        state2 = MooreState("State 2", abcAlphabet[SampleMooreMachines.get_c_symbol()]);

        state0.add_transition(a, state1)
        state0.add_transition(b, state2)
        state1.add_transition(a, state2)
        state1.add_transition(b, state0)
        state2.add_transition(a, state0)
        state2.add_transition(b, state1)

        return MooreMachineAutomaton(abAlphabet, abAlphabet, state0, 
                set([state0, state1, state2]), DFAComparison(), "3 States Moore Machine")

    @staticmethod
    def get_3_states_automaton_non_deterministic():
        a = abAlphabet[SampleMooreMachines.get_a_symbol()]
        b = abAlphabet[SampleMooreMachines.get_b_symbol()]

        state0 = MooreState("State 0", abcAlphabet[SampleMooreMachines.get_a_symbol()]);
        state1 = MooreState("State 1", abcAlphabet[SampleMooreMachines.get_b_symbol()]);
        state2 = MooreState("State 2", abcAlphabet[SampleMooreMachines.get_c_symbol()]);

        state0.add_transition(a, state1)
        state0.add_transition(a, state2)
        state0.add_transition(b, state2)
        state1.add_transition(a, state2)
        state1.add_transition(b, state0)
        state2.add_transition(a, state0)
        state2.add_transition(b, state1)

        return MooreMachineAutomaton(abAlphabet, abAlphabet, state0, 
                set([state0, state1, state2]), DFAComparison(), "3 States Moore Machine")

    @staticmethod
    def tomitas_automaton_1():
        alphabet = Alphabet(frozenset((SymbolStr('False'), SymbolStr('True'))))

        binaryAlphabet = Alphabet(frozenset((SymbolStr('0'), SymbolStr('1'))))
        zero = binaryAlphabet['0']
        one = binaryAlphabet['1']

        stateA = MooreState("State A", alphabet['True'])
        stateB = MooreState("State B", alphabet['False'])
        stateA.add_transition(one, stateA)
        stateA.add_transition(zero, stateB)
        stateB.add_transition(one, stateB)
        stateB.add_transition(zero, stateB)

        hole_state = MooreState(name="hole", value=SymbolStr('False'))

        return MooreMachineAutomaton(binaryAlphabet, alphabet, stateA, 
                set([stateA, stateB]), name='2 States Moore Machine', hole=hole_state)
    