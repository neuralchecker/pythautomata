from base_types.state import State
from base_types.symbol import SymbolStr
from base_types.alphabet import Alphabet
from utilities.automata_convertor import AutomataConvertor
from automata.deterministic_finite_automaton import DeterministicFiniteAutomaton as DFA
from automata.non_deterministic_finite_automaton import NondeterministicFiniteAutomaton as NFA
from model_comparators.nfa_hopcroft_karp_comparison_strategy import NFAHopcroftKarpComparisonStrategy as NFAComparator
from model_comparators.dfa_comparison_strategy import DFAComparisonStrategy as DFAComparator

abAlphabet = Alphabet(frozenset((SymbolStr('a'), SymbolStr('b'))))
abcAlphabet = Alphabet(frozenset((SymbolStr('a'), SymbolStr('b'), SymbolStr('c'))))

#TODO: Check if some NFAS are not in the paper and test
class BolligHabermehlKernLeuckerAutomata:
    """
    Class containing automata from paper:
        Bollig B. and Habermehl P. and Kern C. and Leucker M. 2009. 
        Angluin-style learning of NFA. 
        IJCAI International Joint Conference on Artificial Intelligence. 1004-1009. 

    Methods
    -------
    Methods
    -------
    get_all_automata: list(FiniteAutomaton)
        returns a list containing all automata defined in this class
    
    get_first_example_DFA: DeterministicFiniteAutomaton
        returns the automaton 1 from the paper 
    
    get_first_example_NFA: NondeterministicFiniteAutomaton
        returns the automaton 2 from the paper

    """
    @staticmethod
    def get_all_automata():
        """
        Method returning a list of all automata of the class

        Returns
        -------
        list(FiniteAutomaton)
            all automata defined in the class
        """
        return [
            BolligHabermehlKernLeuckerAutomata.get_first_example_DFA(),
            BolligHabermehlKernLeuckerAutomata.get_first_example_NFA()
            ]
        
    @staticmethod
    def get_first_example_DFA() -> DFA:
        """
        Method returning a DFA that recognizes the regular expresion Σ*aΣ^2 (First example from paper, Fig. 3.)

        Returns:
            DFA: Method returning a DFA that recognizes the regular expresion Σ*aΣ^2
        """
        a = abAlphabet['a']
        b = abAlphabet['b']

        state0 = State("State 0")
        state1 = State("State 1")
        state2 = State("State 2")
        state3 = State("State 3", True)
        state4 = State("State 4", True)
        state5 = State("State 5", True)
        state6 = State("State 6")
        state7 = State("State 7", True)

        state0.add_transition(a, state1)
        state0.add_transition(b, state0)
        state1.add_transition(a, state2)
        state1.add_transition(b, state6)
        state2.add_transition(a, state3)
        state2.add_transition(b, state4)
        state3.add_transition(a, state3)
        state3.add_transition(b, state4)
        state4.add_transition(a, state5)
        state4.add_transition(b, state7)
        state5.add_transition(a, state2)
        state5.add_transition(b, state6)
        state6.add_transition(a, state5)
        state6.add_transition(b, state7)
        state7.add_transition(a, state1)
        state7.add_transition(b, state0)
        comparator = DFAComparator()
        return DFA(abAlphabet, state0,
                               set([state0, state1, state2, state3,
                                    state4, state5, state6, state7]), 
                                    comparator,
                                    "Angluin-style learning of NFA - first example DFA")
        
    @staticmethod
    def get_first_example_NFA() -> DFA:
        """
        Method returning a NFA that recognizes the regular expresion Σ*aΣ^2 (First example from paper, Fig. 4.)

        Returns:
            DFA: Method returning a DFA that recognizes the regular expresion Σ*aΣ^2
        """
        a = abAlphabet['a']
        b = abAlphabet['b']

        state0 = State("-+--")
        state1 = State("-++-")
        state2 = State("-+-+")
        state3 = State("++--", True)        

        state0.add_transition(a, state1)
        state0.add_transition(a, state0)
        state0.add_transition(b, state0)
        state1.add_transition(a, state1)
        state1.add_transition(a, state0)
        state1.add_transition(b, state0)
        state1.add_transition(a, state2)
        state1.add_transition(b, state2)
        state2.add_transition(a, state1)
        state2.add_transition(a, state0)
        state2.add_transition(b, state0)
        state2.add_transition(a, state3)
        state2.add_transition(b, state3)
        state3.add_transition(a, state1)
        state3.add_transition(a, state0)
        state3.add_transition(b, state0)

        comparator = NFAComparator()
        return NFA(abAlphabet,  frozenset({state0}),
                               set([state0, state1, state2, state3]), 
                                    comparator,
                                    "Angluin-style learning of NFA - first example NFA")    
