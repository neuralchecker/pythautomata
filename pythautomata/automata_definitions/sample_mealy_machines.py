from pythautomata.automata.mealy_machine import MealyMachine
from pythautomata.base_types.alphabet import Alphabet
from pythautomata.base_types.mealy_state import MealyState
from pythautomata.base_types.symbol import SymbolStr
from pythautomata.model_comparators.mealy_machine_comparison_strategy import MealyMachineComparisonStrategy


abAlphabet = Alphabet(frozenset((SymbolStr('a'), SymbolStr('b'))))
abcAlphabet = Alphabet(
    frozenset((SymbolStr('a'), SymbolStr('b'), SymbolStr('c'))))


class SampleMealyMachines:
    """
    Class containing sample Moore Machines

    Methods
    -------
    get_all_mealy_machines()
        Returns a list containing all the sample Mealy Machines
    get_3_states_mealy_machine()
        Returns a Mealy Machine with 3 states
    get_tomitas_automaton_1()
        Returns a Mealy Machine that accepts the language of Tomita's automaton 1
    """

    @staticmethod
    def get_all_mealy_machines():
        return [
            SampleMealyMachines.get_3_states_mealy_machine(),
            SampleMealyMachines.get_tomitas_automaton_1(),
        ]

    @staticmethod
    def get_3_states_mealy_machine():
        a = abAlphabet['a']
        b = abAlphabet['b']

        state0 = MealyState("State 0")
        state1 = MealyState("State 1")
        state2 = MealyState("State 2")

        state0.add_transition(a, state1, abcAlphabet['a'])
        state0.add_transition(b, state2, abcAlphabet['b'])
        state1.add_transition(a, state2, abcAlphabet['c'])
        state1.add_transition(b, state0, abcAlphabet['a'])
        state2.add_transition(a, state0, abcAlphabet['b'])
        state2.add_transition(b, state1, abcAlphabet['c'])

        return MealyMachine(abAlphabet, abcAlphabet, state0,
                            set([state0, state1, state2]), MealyMachineComparisonStrategy(), "3 States Mealy Machine")

    @staticmethod
    def get_tomitas_automaton_1():
        alphabet = Alphabet(frozenset((SymbolStr('False'), SymbolStr('True'))))

        binaryAlphabet = Alphabet(frozenset((SymbolStr('0'), SymbolStr('1'))))
        zero = binaryAlphabet['0']
        one = binaryAlphabet['1']

        stateA = MealyState("State A")
        stateB = MealyState("State B")
        stateA.add_transition(one, stateA, alphabet['True'])
        stateA.add_transition(zero, stateB, alphabet['False'])
        stateB.add_transition(one, stateB, alphabet['False'])
        stateB.add_transition(zero, stateB, alphabet['False'])

        hole_state = MealyState(name="hole")

        return MealyMachine(binaryAlphabet, alphabet, stateA,
                            set([stateA, stateB]
                                ), MealyMachineComparisonStrategy(),
                            name="Mealy machine implementation of Tomita's grammar 2 automaton", hole=hole_state)
