from pythautomata.base_types.symbol import SymbolStr
from pythautomata.base_types.alphabet import Alphabet
from pythautomata.automata.wheighted_automaton_definition.probabilistic_deterministic_finite_automaton import \
    ProbabilisticDeterministicFiniteAutomaton
from pythautomata.automata.wheighted_automaton_definition.weighted_state import WeightedState
from pythautomata.model_comparators.wfa_tolerance_comparison_strategy import WFAToleranceComparator

binaryAlphabet = Alphabet(frozenset((SymbolStr('0'), SymbolStr('1'))))
zero = binaryAlphabet['0']
one = binaryAlphabet['1']


class ZeroTransitionsExamples:
    """
    Class containing weighted (probabilistic) automata with zero valued transitions

    Methods
    -------   
    get_all_automata: list(ProbabilisticDeterministicFiniteAutomaton)
        returns a list containing all weigthed automata defined in this class

    get_automaton_1: ProbabilisticDeterministicFiniteAutomaton
        returns a automaton 1 

    get_automaton_2: ProbabilisticDeterministicFiniteAutomaton
        returns aautomaton 2

    get_automaton_3: ProbabilisticDeterministicFiniteAutomaton
        returns automaton 3 
    """

    @staticmethod
    def get_all_automata():
        """
        Method returning a list of all automata of the class

        Returns
        -------
        list(ProbabilisticDeterministicFiniteAutomaton)
            all automata defined in the class
        """
        return [
            ZeroTransitionsExamples.get_automaton_1(),
            ZeroTransitionsExamples.get_automaton_2(),
            ZeroTransitionsExamples.get_automaton_3(),
        ]

    @staticmethod
    def get_automaton_1():
        """
        method with specification of automaton 1      

        Returns
        -------
        ProbabilisticDeterministicFiniteAutomaton
            automaton 1
        """
        q0 = WeightedState("q0", 1, 0.2)
        q1 = WeightedState("q1", 0, 0.2)

        q0.add_transition(zero, q1, 0)
        q0.add_transition(one, q0, 0.8)
        q1.add_transition(zero, q1, 0.3)
        q1.add_transition(one, q1, 0.5)

        states = {q0, q1}
        comparator = WFAToleranceComparator()
        return ProbabilisticDeterministicFiniteAutomaton(binaryAlphabet, states, SymbolStr("$"), comparator, "ZeroTransitionsExample1")

    @staticmethod
    def get_automaton_2():
        """
        method with specification of automaton 2      

        Returns
        -------
        ProbabilisticDeterministicFiniteAutomaton
            automaton 2
        """
        q0 = WeightedState("q0", 1, 0.2)
        q1 = WeightedState("q1", 0, 0.2)

        q0.add_transition(zero, q1, 0)
        q0.add_transition(one, q0, 0.8)
        q1.add_transition(zero, q1, 0.1)
        q1.add_transition(one, q1, 0.7)

        states = {q0, q1}
        comparator = WFAToleranceComparator()
        return ProbabilisticDeterministicFiniteAutomaton(binaryAlphabet, states, SymbolStr("$"), comparator, "ZeroTransitionsExample2")

    @staticmethod
    def get_automaton_3():
        """
        method with specification of automaton 3      

        Returns
        -------
        ProbabilisticDeterministicFiniteAutomaton
            automaton 3
        """
        q0 = WeightedState("q0", 1, 0.2)
        q1 = WeightedState("q1", 0, 0.2)

        q0.add_transition(zero, q1, 0.05)
        q0.add_transition(one, q0, 0.75)
        q1.add_transition(zero, q1, 0.1)
        q1.add_transition(one, q1, 0.7)

        states = {q0, q1}
        comparator = WFAToleranceComparator()
        return ProbabilisticDeterministicFiniteAutomaton(binaryAlphabet, states, SymbolStr("$"), comparator, "ZeroTransitionsExample3")