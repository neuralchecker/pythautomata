from pythautomata.base_types.state import State
from pythautomata.base_types.symbol import SymbolStr
from pythautomata.base_types.alphabet import Alphabet

from pythautomata.automata.moore_machine_automaton import MooreMachineAutomaton
from pythautomata.base_types.moore_state import MooreState

from pythautomata.model_comparators.moore_machine_comparison_strategy import MooreMachineComparisonStrategy as MooreMachineComparison


abAlphabet = Alphabet(frozenset((SymbolStr('a'), SymbolStr('b'))))
abcAlphabet = Alphabet(
    frozenset((SymbolStr('a'), SymbolStr('b'), SymbolStr('c'))))


class SampleMooreMachines:

    """
    Class containing sample Moore Machines

    Methods
    -------
    get_a_symbol()
        Returns the symbol 'a'
    get_b_symbol()
        Returns the symbol 'b'
    get_c_symbol()
        Returns the symbol 'c'
    get_all_automata()
        Returns a list containing all the sample Moore Machines that are correct
    get_3_states_automaton()
        Returns a Moore Machine with 3 states
    get_3_states_automaton_wrong_alphabet()
        Returns a Moore Machine with 3 states and wrong alphabet. This is used to test the Moore Machine constructor 
        and will raise an exception when used
    get_3_states_automaton_non_deterministic()
        Returns a Moore Machine with 3 states and non deterministic transitions. 
        This is used to test the Moore Machine constructor and will raise an exception when used
    get_tomitas_automaton_1()
        Returns a Moore Machine that accepts the language of Tomita's automaton 1
    get_tomitas_automaton_2()
        Returns a Moore Machine that accepts the language of Tomita's automaton 2

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
            SampleMooreMachines.get_tomitas_automaton_1(),
            SampleMooreMachines.get_tomitas_automaton_2(),
        ]

    @staticmethod
    def get_3_states_automaton():
        a = abAlphabet[SampleMooreMachines.get_a_symbol()]
        b = abAlphabet[SampleMooreMachines.get_b_symbol()]

        state0 = MooreState(
            "State 0", abcAlphabet[SampleMooreMachines.get_a_symbol()])
        state1 = MooreState(
            "State 1", abcAlphabet[SampleMooreMachines.get_b_symbol()])
        state2 = MooreState(
            "State 2", abcAlphabet[SampleMooreMachines.get_c_symbol()])

        state0.add_transition(a, state1)
        state0.add_transition(b, state2)
        state1.add_transition(a, state2)
        state1.add_transition(b, state0)
        state2.add_transition(a, state0)
        state2.add_transition(b, state1)

        return MooreMachineAutomaton(abAlphabet, abcAlphabet, state0,
                                     set([state0, state1, state2]), MooreMachineComparison(), "3 States Moore Machine")

    @staticmethod
    def get_3_states_automaton_wrong_alphabet():
        a = abAlphabet[SampleMooreMachines.get_a_symbol()]
        b = abAlphabet[SampleMooreMachines.get_b_symbol()]

        state0 = MooreState(
            "State 0", abcAlphabet[SampleMooreMachines.get_a_symbol()])
        state1 = MooreState(
            "State 1", abcAlphabet[SampleMooreMachines.get_b_symbol()])
        state2 = MooreState(
            "State 2", abcAlphabet[SampleMooreMachines.get_c_symbol()])

        state0.add_transition(a, state1)
        state0.add_transition(b, state2)
        state1.add_transition(a, state2)
        state1.add_transition(b, state0)
        state2.add_transition(a, state0)
        state2.add_transition(b, state1)

        return MooreMachineAutomaton(abAlphabet, abAlphabet, state0,
                                     set([state0, state1, state2]), MooreMachineComparison(), "3 States Moore Machine")

    @staticmethod
    def get_3_states_automaton_non_deterministic():
        a = abAlphabet[SampleMooreMachines.get_a_symbol()]
        b = abAlphabet[SampleMooreMachines.get_b_symbol()]

        state0 = MooreState(
            "State 0", abcAlphabet[SampleMooreMachines.get_a_symbol()])
        state1 = MooreState(
            "State 1", abcAlphabet[SampleMooreMachines.get_b_symbol()])
        state2 = MooreState(
            "State 2", abcAlphabet[SampleMooreMachines.get_c_symbol()])

        state0.add_transition(a, state1)
        state0.add_transition(a, state2)
        state0.add_transition(b, state2)
        state1.add_transition(a, state2)
        state1.add_transition(b, state0)
        state2.add_transition(a, state0)
        state2.add_transition(b, state1)

        return MooreMachineAutomaton(abAlphabet, abAlphabet, state0,
                                     set([state0, state1, state2]),
                                     MooreMachineComparison(), "3 States Moore Machine")

    @staticmethod
    def get_tomitas_automaton_1():
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
                                     set([stateA, stateB]
                                         ), MooreMachineComparison(),
                                     name='2 States Moore Machine', hole=hole_state)

    @staticmethod
    def get_tomitas_automaton_2():
        boolean_alphabet = Alphabet(
            frozenset((SymbolStr('False'), SymbolStr('True'))))

        binaryAlphabet = Alphabet(frozenset((SymbolStr('0'), SymbolStr('1'))))
        zero = binaryAlphabet['0']
        one = binaryAlphabet['1']

        stateA = MooreState("State A", boolean_alphabet['True'])
        stateB = MooreState("State B", boolean_alphabet['False'])
        stateC = MooreState("State C", boolean_alphabet['False'])
        stateA.add_transition(one, stateB)
        stateA.add_transition(zero, stateC)
        stateB.add_transition(one, stateC)
        stateB.add_transition(zero, stateA)
        stateC.add_transition(one, stateC)
        stateC.add_transition(zero, stateC)

        hole_state = MooreState("Hole", SymbolStr("False"))

        return MooreMachineAutomaton(binaryAlphabet, boolean_alphabet, stateA,
                                     set([stateA, stateB, stateC]),
                                     MooreMachineComparison(),
                                     name="MMA implementation of Tomita's grammar 2 automaton",
                                     hole=hole_state)
