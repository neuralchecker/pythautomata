from base_types.state import State
from base_types.symbol import SymbolStr
from base_types.alphabet import Alphabet
from queryable_models.finite_automaton import FiniteAutomaton
from model_comparators.hopcroft_karp_comparison_strategy import HopcroftKarpComparisonStrategy

binaryAlphabet = Alphabet(frozenset((SymbolStr('0'), SymbolStr('1'))))
zero = binaryAlphabet['0']
one = binaryAlphabet['1']


class TomitasGrammarMods:
    """
    Class containing modified versions of automata from paper:    
        Tomita, M. (1982). 
        Dynamic Construction of Finite Automata from examples using Hill-climbing. 
        Proceedings of the Fourth Annual Conference of the Cognitive Science Society 
        (p./pp. 105--108), Ann Arbor, Michigan.

    Methods
    -------   
    get_mod_automaton_5: DeterministicFiniteAutomaton
        returns a modified version of the automaton 5 from the paper
    """
 
    @staticmethod
    def get_mod_automaton_5():
        """
        method with specification of a modified version of the automaton 5 from the paper

        Recognizes strings that have an even ammount of 01 (and not taking into account 10). 
        It's a sublanguage of the fifth Tomita's grammar.

        Returns
        -------
        DeterministicFiniteAutomaton
            modified version of automaton 5 from the paper
        """
        stateQ0 = State("State 0", True)
        stateQ1 = State("State 1")
        stateQ2 = State("State 2")
        stateQ3 = State("State 3")
        stateQ0.add_transition(one, stateQ1) 
        stateQ1.add_transition(zero, stateQ2)        
        stateQ2.add_transition(one, stateQ3)        
        stateQ3.add_transition(zero, stateQ0) 
        
        comparator = HopcroftKarpComparisonStrategy()
        return FiniteAutomaton(binaryAlphabet, frozenset({stateQ0}),
                               set([stateQ1, stateQ2, stateQ3, stateQ0]), comparator, "Tomita's grammar 5 sub language automaton")