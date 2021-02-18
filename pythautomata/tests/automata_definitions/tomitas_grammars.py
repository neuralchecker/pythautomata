from base_types.state import State
from base_types.symbol import SymbolStr
from base_types.alphabet import Alphabet
from automata.deterministic_finite_automaton import DeterministicFiniteAutomaton
from model_comparators.dfa_comparison_strategy import DFAComparisonStrategy as DFAComparator

binaryAlphabet = Alphabet(frozenset((SymbolStr('0'), SymbolStr('1'))))
zero = binaryAlphabet['0']
one = binaryAlphabet['1']


class TomitasGrammars:
    """
    Class containing automata from paper:    
    Tomita, M. (1982). 
    Dynamic Construction of Finite Automata from examples using Hill-climbing. 
    Proceedings of the Fourth Annual Conference of the Cognitive Science Society 
    (p./pp. 105--108), Ann Arbor, Michigan.

    Methods
    -------
    get_all_automata: list(DeterministicFiniteAutomaton)
        returns a list containing all automata defined in this class
    
    get_automaton_1: DeterministicFiniteAutomaton
        returns the automaton 1 from the paper 
    
    get_automaton_2: DeterministicFiniteAutomaton
        returns the automaton 2 from the paper

    get_automaton_3: DeterministicFiniteAutomaton
        returns the automaton 3 from the paper
    
    get_automaton_4: DeterministicFiniteAutomaton
        returns the automaton 4 from the paper

    get_automaton_5: DeterministicFiniteAutomaton
        returns the automaton 5 from the paper

    get_automaton_6: DeterministicFiniteAutomaton
        returns the automaton 6 from the paper
    
    get_automaton_7: DeterministicFiniteAutomaton
        returns the automaton 7 from the paper
    """

    @staticmethod
    def get_all_automata():
        """
        Method returning a list of all automata of the class

        Returns
        -------
        list(DeterministicFiniteAutomaton)
            all automata defined in the class
        """
        return [
            TomitasGrammars.get_automaton_1(),
            TomitasGrammars.get_automaton_2(),
            TomitasGrammars.get_automaton_3(),
            TomitasGrammars.get_automaton_4(),
            TomitasGrammars.get_automaton_5(),
            TomitasGrammars.get_automaton_6(),
            TomitasGrammars.get_automaton_7()
        ]

    @staticmethod
    def get_automaton_1():
        """
        Method with specification of the automaton 1 from the paper

        The first Tomita's grammar is defined as the regular expresion: 1*

        Returns
        -------
        DeterministicFiniteAutomaton
            automaton 1 from the paper
        """
        stateA = State("State A", True)
        stateB = State("State B")
        stateA.add_transition(one, stateA)
        stateA.add_transition(zero, stateB)
        stateB.add_transition(one, stateB)
        stateB.add_transition(zero, stateB)    

        comparator = DFAComparator()
        return DeterministicFiniteAutomaton(binaryAlphabet, stateA,
                               set([stateA, stateB]), comparator, "Tomita's grammar 1 automaton")

    @staticmethod
    def get_automaton_2():
        """
        Method with specification of the automaton 2 from the paper

        The second Tomita's grammar is defined as the regular expresion: (10)*

        Returns
        -------
        DeterministicFiniteAutomaton
            automaton 2 from the paper
        """

        stateA = State("State A", True)
        stateB = State("State B")
        stateC = State("State C")
        stateA.add_transition(one, stateB)
        stateA.add_transition(zero, stateC)
        stateB.add_transition(one, stateC)
        stateB.add_transition(zero, stateA)
        stateC.add_transition(one, stateC)
        stateC.add_transition(zero, stateC)
        
        comparator = DFAComparator()
        return DeterministicFiniteAutomaton(binaryAlphabet, stateA,
                               set([stateA, stateB, stateC]), comparator, "Tomita's grammar 2 automaton")

    @staticmethod
    def get_automaton_3():
        """
        Method with specification of the automaton 3 from the paper

        The third Tomita's grammar recognizes strings that don't contain the regular expresion (1^(2n+1), 0^(2m+1)) as substring.

        Returns
        -------
        DeterministicFiniteAutomaton
            automaton 3 from the paper
        """
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
        
        comparator = DFAComparator()
        return DeterministicFiniteAutomaton(binaryAlphabet, stateQ1,
                               set([stateQ1, stateQ2, stateQ3, stateQ4, stateQ5]),
                               comparator,
                               "Tomita's grammar 3 automaton")

    @staticmethod
    def get_automaton_4():
        """
        Method with specification of the automaton 4 from the paper

        The fourth Tomita grammar recognizes strings that don't contain the regular expresion 000 as substring.

        Returns
        -------
        DeterministicFiniteAutomaton
            automaton 4 from the paper
        """

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
        
        comparator = DFAComparator()
        return DeterministicFiniteAutomaton(binaryAlphabet, stateQ1,
                               set([stateQ1, stateQ2, stateQ3, stateQ4]), comparator, "Tomita's grammar 4 automaton")

    @staticmethod
    def get_automaton_5():
        """
        Method with specification of the automaton 5 from the paper

        The fifth Tomita's grammar recognizes strings that have an even ammount of 01 and 10

        Returns
        -------
        DeterministicFiniteAutomaton
            automaton 5 from the paper
        """
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

        comparator = DFAComparator()
        return DeterministicFiniteAutomaton(binaryAlphabet, stateQ1,
                               set([stateQ1, stateQ2, stateQ3, stateQ4]), comparator, "Tomita's grammar 5 automaton")
    
    @staticmethod
    def get_automaton_6():
        """
        Method with specification of the automaton 6 from the paper

        The sixth Tomita's grammar recognizes strings where (ammount of 0) - (amount of 1) = multiple of 3.

        Returns
        -------
        DeterministicFiniteAutomaton
            automaton 5 from the paper
        """
        stateQ1 = State("State 0", True)
        stateQ2 = State("State 1")
        stateQ3 = State("State 2")
        stateQ1.add_transition(one, stateQ2)
        stateQ1.add_transition(zero, stateQ3)
        stateQ2.add_transition(one, stateQ3)
        stateQ2.add_transition(zero, stateQ1)
        stateQ3.add_transition(one, stateQ1)
        stateQ3.add_transition(zero, stateQ2)
        
        comparator = DFAComparator()
        return DeterministicFiniteAutomaton(binaryAlphabet, stateQ1,
                               set([stateQ1, stateQ2, stateQ3]), comparator, "Tomita's grammar 6 automaton")

    @staticmethod
    def get_automaton_7():
        """
        Method with specification of the automaton 7 from the paper

        The seventh Tomita's grammargrammar is defined as the regular expresion: 0*1*0*1*
        Returns
        -------
        DeterministicFiniteAutomaton
            automaton 7 from the paper
        """
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
        
        comparator = DFAComparator()
        return DeterministicFiniteAutomaton(binaryAlphabet, stateQ1,
                               set([stateQ1, stateQ2, stateQ3, stateQ4, stateQ5]), comparator,
                               "Tomita's grammar 7 automaton")
