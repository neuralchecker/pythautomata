from base_types.state import State
from base_types.symbol import SymbolStr
from base_types.alphabet import Alphabet
from automata.deterministic_finite_automaton import DeterministicFiniteAutomaton
from model_comparators.dfa_comparison_strategy import DFAComparisonStrategy as DFAComparator

abcAlphabet = Alphabet(frozenset(
    (SymbolStr('a'), SymbolStr('b'), SymbolStr('c'))))
abcdAlphabet = Alphabet(frozenset(
    (SymbolStr('a'), SymbolStr('b'), SymbolStr('c'), SymbolStr('d'))))

class OmlinGilesAutomata:
    """
    Class containing automata from paper:
        Christian W. Omlin and C. Lee Giles. 1996. 
        Constructing deterministic finite-state automata in recurrent neural networks. 
        J. ACM 43, 6 (Nov. 1996), 937–972. DOI:https://doi.org/10.1145/235809.235811

    Methods
    -------
    get_all_automata: list(DeterministicFiniteAutomaton)
        returns a list containing all automata defined in this class
    
    get_a_automaton: DeterministicFiniteAutomaton
        returns the automaton A from the paper 
    
    get_b_automaton: DeterministicFiniteAutomaton
        returns the automaton B from the paper

    get_az_automaton: DeterministicFiniteAutomaton
        returns the automaton A from the paper with stuttering symbol (d)
    
    get_bz_automaton: DeterministicFiniteAutomaton
        returns the automaton A from the paper with stuttering symbol (d)
    """
    
    @staticmethod
    def get_all_automata():
        """
        method returning a list of all automata of the class

        Returns
        -------
        list(DeterministicFiniteAutomaton)
            all automata defined in the class

        """
        return [
            OmlinGilesAutomata.get_a_automaton(),
            OmlinGilesAutomata.get_az_automaton(),
            OmlinGilesAutomata.get_b_automaton(),
            OmlinGilesAutomata.get_bz_automaton()
        ]

    @staticmethod
    def get_a_automaton():
        """
        method with specification of the automaton A from the paper

        Returns
        -------
        DeterministicFiniteAutomaton
            automaton A from the paper

        """
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
        comparator = DFAComparator()
        return DeterministicFiniteAutomaton(abcAlphabet, state0,
                               set([state0, state1, state2]), comparator, "a automaton",)

    @staticmethod
    def get_b_automaton():
        """
        method with specification of the automaton B from the paper

        Returns
        -------
        DeterministicFiniteAutomaton
            automaton B from the paper
        """
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
        comparator = DFAComparator()
        return DeterministicFiniteAutomaton(abcAlphabet, state0,
                               set([state0, state1, state2, state3,
                                    state4, state5]), comparator, "b automaton")

    @staticmethod
    def get_az_automaton():
        """
        method with specification of the automaton A from the paper, with a stuttering symbol

        Returns
        -------
        DeterministicFiniteAutomaton
            automaton A from the paper, with a stuttering symbol
        """
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
        comparator = DFAComparator()
        return DeterministicFiniteAutomaton(abcdAlphabet, state0,
                               set([state0, state1, state2]), comparator, "az automaton")

    @staticmethod
    def get_bz_automaton():
        """
        method with specification of the automaton B from the paper, with a stuttering symbol

        Returns
        -------
        DeterministicFiniteAutomaton
            automaton B from the paper, with a stuttering symbol
        """
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
        comparator = DFAComparator()
        return DeterministicFiniteAutomaton(abcdAlphabet, state0,
                               set([state0, state1, state2, state3,
                                    state4, state5]), comparator, "bz automaton")
