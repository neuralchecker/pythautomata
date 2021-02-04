from base_types.state import State
from base_types.symbol import SymbolChar
from base_types.alphabet import Alphabet
from queryable_models.finite_automaton import FiniteAutomaton

binaryAlphabet = Alphabet(frozenset((SymbolChar('0'), SymbolChar('1'))))
zero = binaryAlphabet['0']
one = binaryAlphabet['1']


class TomitasGrammarMods:

    # Definition: Recognizes strings that have an even ammount of 01 (and not taking into account 10). It's a sublanguage of Tomita5 
    @staticmethod
    def get_mod_automaton_5():
        stateQ0 = State("State 0", True)
        stateQ1 = State("State 1")
        stateQ2 = State("State 2")
        stateQ3 = State("State 3")
        stateQ0.add_transition(one, stateQ1) 
        stateQ1.add_transition(zero, stateQ2)        
        stateQ2.add_transition(one, stateQ3)        
        stateQ3.add_transition(zero, stateQ0) 
        return FiniteAutomaton(binaryAlphabet, frozenset({stateQ0}),
                               set([stateQ1, stateQ2, stateQ3, stateQ0]), "Tomita's grammar 5 sub language automaton")