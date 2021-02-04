from base_types.state import State
from base_types.symbol import SymbolChar
from base_types.alphabet import Alphabet
from queryable_models.finite_automaton import FiniteAutomaton

abcAlphabet = Alphabet(frozenset(
    (SymbolChar('a'), SymbolChar('b'), SymbolChar('c'))))
abcdAlphabet = Alphabet(frozenset(
    (SymbolChar('a'), SymbolChar('b'), SymbolChar('c'), SymbolChar('d'))))

# Automata taken from Omlin & Giles’
# "Constructing Deterministic Finite-State Automata in Recurrent Neural Networks".


class OmlinGilesAutomata:

    @staticmethod
    def get_all_automata():
        return [
            OmlinGilesAutomata.get_a_automaton(),
            OmlinGilesAutomata.get_az_automaton(),
            OmlinGilesAutomata.get_b_automaton(),
            OmlinGilesAutomata.get_bz_automaton()
        ]

    @staticmethod
    def get_a_automaton():
        a = abcAlphabet['a']
        b = abcAlphabet['b']
        c = abcAlphabet['c']
        state0 = State("State 0")
        state1 = State("State 1")
        state2 = State("State 2", True)
        state0.add_transition(a, state0)
        state0.add_transition(b, state1)
        state0.add_transition(c, state1)
        state1.add_transition(a, state1)
        state1.add_transition(b, state0)
        state1.add_transition(c, state2)
        state2.add_transition(a, state1)
        state2.add_transition(b, state0)
        state2.add_transition(c, state2)
        return FiniteAutomaton(abcAlphabet, frozenset({state0}),
                               set([state0, state1, state2]), "a automaton")

    @staticmethod
    def get_b_automaton():
        a = abcAlphabet['a']
        b = abcAlphabet['b']
        c = abcAlphabet['c']
        state0 = State("State 0")
        state1 = State("State 1")
        state2 = State("State 2")
        state3 = State("State 3")
        state4 = State("State 4")
        state5 = State("State 5", True)
        state0.add_transition(a, state0)
        state0.add_transition(b, state3)
        state0.add_transition(c, state3)
        state1.add_transition(a, state3)
        state1.add_transition(b, state1)
        state1.add_transition(c, state4)
        state2.add_transition(a, state4)
        state2.add_transition(b, state5)
        state2.add_transition(c, state2)
        state3.add_transition(a, state0)
        state3.add_transition(b, state1)
        state3.add_transition(c, state1)
        state4.add_transition(a, state1)
        state4.add_transition(b, state1)
        state4.add_transition(c, state2)
        state5.add_transition(a, state0)
        state5.add_transition(b, state0)
        state5.add_transition(c, state2)
        return FiniteAutomaton(abcAlphabet, frozenset({state0}),
                               set([state0, state1, state2, state3,
                                    state4, state5]), "b automaton")

    @staticmethod
    def get_az_automaton():
        a = abcdAlphabet['a']
        b = abcdAlphabet['b']
        c = abcdAlphabet['c']
        d = abcdAlphabet['d']
        state0 = State("State 0")
        state1 = State("State 1")
        state2 = State("State 2", True)
        state0.add_transition(a, state0)
        state0.add_transition(d, state0)
        state0.add_transition(b, state1)
        state0.add_transition(c, state1)
        state1.add_transition(a, state1)
        state1.add_transition(b, state0)
        state1.add_transition(c, state2)
        state1.add_transition(d, state1)
        state2.add_transition(a, state1)
        state2.add_transition(b, state0)
        state2.add_transition(c, state2)
        state2.add_transition(d, state2)
        return FiniteAutomaton(abcdAlphabet, frozenset({state0}),
                               set([state0, state1, state2]), "az automaton")

    @staticmethod
    def get_bz_automaton():
        a = abcdAlphabet['a']
        b = abcdAlphabet['b']
        c = abcdAlphabet['c']
        d = abcdAlphabet['d']
        state0 = State("State 0")
        state1 = State("State 1")
        state2 = State("State 2")
        state3 = State("State 3")
        state4 = State("State 4")
        state5 = State("State 5", True)
        state0.add_transition(a, state0)
        state0.add_transition(b, state3)
        state0.add_transition(c, state3)
        state0.add_transition(d, state0)
        state1.add_transition(a, state3)
        state1.add_transition(b, state1)
        state1.add_transition(c, state4)
        state1.add_transition(d, state1)
        state2.add_transition(a, state4)
        state2.add_transition(b, state5)
        state2.add_transition(c, state2)
        state2.add_transition(d, state2)
        state3.add_transition(a, state0)
        state3.add_transition(b, state1)
        state3.add_transition(c, state1)
        state3.add_transition(d, state3)
        state4.add_transition(a, state1)
        state4.add_transition(b, state1)
        state4.add_transition(c, state2)
        state4.add_transition(d, state4)
        state5.add_transition(a, state0)
        state5.add_transition(b, state0)
        state5.add_transition(c, state2)
        state5.add_transition(d, state5)
        return FiniteAutomaton(abcdAlphabet, frozenset({state0}),
                               set([state0, state1, state2, state3,
                                    state4, state5]), "bz automaton")
