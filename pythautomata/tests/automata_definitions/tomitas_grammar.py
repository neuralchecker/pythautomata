from base_types.state import State
from base_types.symbol import SymbolChar
from base_types.alphabet import Alphabet
from queryable_models.finite_automaton import FiniteAutomaton

binaryAlphabet = Alphabet(frozenset((SymbolChar('0'), SymbolChar('1'))))
zero = binaryAlphabet['0']
one = binaryAlphabet['1']


class TomitasGrammar:

    @staticmethod
    def get_all_automata():
        return [
            TomitasGrammar.get_automaton_1(),
            TomitasGrammar.get_automaton_2(),
            TomitasGrammar.get_automaton_3(),
            TomitasGrammar.get_automaton_4(),
            TomitasGrammar.get_automaton_5(),
            TomitasGrammar.get_automaton_6(),
            TomitasGrammar.get_automaton_7()
        ]

    # Definition: 1*
    @staticmethod
    def get_automaton_1():
        stateA = State("State A", True)
        stateB = State("State B")
        stateA.add_transition(one, stateA)
        stateA.add_transition(zero, stateB)
        stateB.add_transition(one, stateB)
        stateB.add_transition(zero, stateB)
        return FiniteAutomaton(binaryAlphabet, frozenset({stateA}),
                               set([stateA, stateB]), "Tomita's grammar 1 automaton")

    # Definition: (10)*
    @staticmethod
    def get_automaton_2():
        stateA = State("State A", True)
        stateB = State("State B")
        stateC = State("State C")
        stateA.add_transition(one, stateB)
        stateA.add_transition(zero, stateC)
        stateB.add_transition(one, stateC)
        stateB.add_transition(zero, stateA)
        stateC.add_transition(one, stateC)
        stateC.add_transition(zero, stateC)
        return FiniteAutomaton(binaryAlphabet, frozenset({stateA}),
                               set([stateA, stateB, stateC]), "Tomita's grammar 2 automaton")

    # Definition: Recognizes strings that don't contain (1^(2n+1), 0^(2m+1)) as substring.
    @staticmethod
    def get_automaton_3():
        stateQ1 = State("State 0", True)
        stateQ2 = State("State 1", True)
        stateQ3 = State("State 2", True)
        stateQ4 = State("State 3")
        stateQ5 = State("State 4")
        stateQ1.add_transition(one, stateQ2)
        stateQ1.add_transition(zero, stateQ1)
        stateQ2.add_transition(one, stateQ1)
        stateQ2.add_transition(zero, stateQ4)
        stateQ3.add_transition(one, stateQ2)
        stateQ3.add_transition(zero, stateQ4)
        stateQ4.add_transition(one, stateQ5)
        stateQ4.add_transition(zero, stateQ3)
        stateQ5.add_transition(one, stateQ5)
        stateQ5.add_transition(zero, stateQ5)
        return FiniteAutomaton(binaryAlphabet, frozenset({stateQ1}),
                               set([stateQ1, stateQ2, stateQ3, stateQ4, stateQ5]),
                               "Tomita's grammar 3 automaton")

    # Definition: Recognizes strings that don't contain 000 as substring.
    @staticmethod
    def get_automaton_4():
        stateQ1 = State("State 0", True)
        stateQ2 = State("State 1", True)
        stateQ3 = State("State 2", True)
        stateQ4 = State("State 3")
        stateQ1.add_transition(one, stateQ1)
        stateQ1.add_transition(zero, stateQ2)
        stateQ2.add_transition(one, stateQ1)
        stateQ2.add_transition(zero, stateQ3)
        stateQ3.add_transition(one, stateQ1)
        stateQ3.add_transition(zero, stateQ4)
        stateQ4.add_transition(one, stateQ4)
        stateQ4.add_transition(zero, stateQ4)
        return FiniteAutomaton(binaryAlphabet, frozenset({stateQ1}),
                               set([stateQ1, stateQ2, stateQ3, stateQ4]), "Tomita's grammar 4 automaton")

    # Definition: Recognizes strings that have an even ammount of 01 and 10.
    @staticmethod
    def get_automaton_5():
        stateQ1 = State("State 0", True)
        stateQ2 = State("State 1")
        stateQ3 = State("State 2")
        stateQ4 = State("State 3")
        stateQ1.add_transition(one, stateQ2)
        stateQ1.add_transition(zero, stateQ3)
        stateQ2.add_transition(one, stateQ1)
        stateQ2.add_transition(zero, stateQ4)
        stateQ3.add_transition(one, stateQ4)
        stateQ3.add_transition(zero, stateQ1)
        stateQ4.add_transition(one, stateQ3)
        stateQ4.add_transition(zero, stateQ2)
        return FiniteAutomaton(binaryAlphabet, frozenset({stateQ1}),
                               set([stateQ1, stateQ2, stateQ3, stateQ4]), "Tomita's grammar 5 automaton")

    # Definition: Recognizes strings where (ammount of 0) - (amount of 1) = multiple of 3.
    @staticmethod
    def get_automaton_6():
        stateQ1 = State("State 0", True)
        stateQ2 = State("State 1")
        stateQ3 = State("State 2")
        stateQ1.add_transition(one, stateQ2)
        stateQ1.add_transition(zero, stateQ3)
        stateQ2.add_transition(one, stateQ3)
        stateQ2.add_transition(zero, stateQ1)
        stateQ3.add_transition(one, stateQ1)
        stateQ3.add_transition(zero, stateQ2)
        return FiniteAutomaton(binaryAlphabet, frozenset({stateQ1}),
                               set([stateQ1, stateQ2, stateQ3]), "Tomita's grammar 6 automaton")

    # Definition: 0*1*0*1*
    @staticmethod
    def get_automaton_7():
        stateQ1 = State("state0", True)
        stateQ2 = State("state1", True)
        stateQ3 = State("state2", True)
        stateQ4 = State("state3", True)
        stateQ5 = State("state4")
        stateQ1.add_transition(one, stateQ2)
        stateQ1.add_transition(zero, stateQ1)
        stateQ2.add_transition(one, stateQ2)
        stateQ2.add_transition(zero, stateQ3)
        stateQ3.add_transition(one, stateQ4)
        stateQ3.add_transition(zero, stateQ3)
        stateQ4.add_transition(one, stateQ4)
        stateQ4.add_transition(zero, stateQ5)
        stateQ5.add_transition(one, stateQ5)
        stateQ5.add_transition(zero, stateQ5)
        return FiniteAutomaton(binaryAlphabet, frozenset({stateQ1}),
                               set([stateQ1, stateQ2, stateQ3, stateQ4, stateQ5]),
                               "Tomita's grammar 7 automaton")
