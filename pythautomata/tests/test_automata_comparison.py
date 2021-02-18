from itertools import chain
from unittest import TestCase
from model_comparators.nfa_hopcroft_karp_comparison_strategy import NFAHopcroftKarpComparisonStrategy as NFAComparator
from model_comparators.dfa_comparison_strategy import DFAComparisonStrategy as DFAComparator
from tests.automata_definitions.other_automata import OtherAutomata
from tests.automata_definitions.tomitas_grammars import TomitasGrammars
from tests.automata_definitions.omlin_giles_automata import OmlinGilesAutomata
from tests.automata_definitions.bollig_habermehl_kern_leucker_automata import BolligHabermehlKernLeuckerAutomata
from automata.deterministic_finite_automaton import DeterministicFiniteAutomaton as DFA
from automata.non_deterministic_finite_automaton import NondeterministicFiniteAutomaton as NFA
from utilities.automata_convertor import AutomataConvertor


class TestAutomataComparison(TestCase):

    def test_equivalence_reflexiveness(self):
        mergedAutomata = list(chain(TomitasGrammars.get_all_automata(),
                                    OmlinGilesAutomata.get_all_automata(),
                                    OtherAutomata.get_all_automata()))
        for automaton in mergedAutomata:
            self.assertAreEquivalentFAs(automaton, automaton)

    def test_equivalence_minimized_automaton_1(self):
        automaton = OtherAutomata.get_automaton_1()
        minimized_automaton = OtherAutomata.get_automaton_1_minimized()
        self.assertAreEquivalentFAs(automaton, minimized_automaton)

    def test_equivalence_minimized_automaton_2(self):
        automaton = OtherAutomata.get_automaton_2()
        minimized_automaton = OtherAutomata.get_automaton_2_minimized()
        self.assertAreEquivalentFAs(automaton, minimized_automaton)

    def test_equivalence_minimized_automaton_3(self):
        automaton = OtherAutomata.get_automaton_3()
        minimized_automaton = OtherAutomata.get_automaton_3_minimized()
        self.assertAreEquivalentFAs(automaton, minimized_automaton)

    def test_equivalence_minimized_automaton_4(self):
        automaton = OtherAutomata.get_automaton_4()
        minimized_automaton = OtherAutomata.get_automaton_4_minimized()
        self.assertAreEquivalentFAs(automaton, minimized_automaton)

    def test_dfa_ndfa_equivalence_1(self):
        dfa = OtherAutomata.get_nfa_1()
        ndfa = OtherAutomata.get_dfa_1()
        self.assertAreEquivalentFAs(dfa, ndfa)

    def test_dfa_ndfa_equivalence_2(self):
        dfa = OtherAutomata.get_nfa_2()
        ndfa = OtherAutomata.get_dfa_2()
        self.assertAreEquivalentFAs(dfa, ndfa)

    def test_dfa_ndfa_equivalence_3(self):
        dfa = OtherAutomata.get_nfa_3()
        ndfa = OtherAutomata.get_dfa_3()
        self.assertAreEquivalentFAs(dfa, ndfa)

    def test_dfa_ndfa_equivalence_4(self):
        dfa = OtherAutomata.get_nfa_4()
        ndfa = OtherAutomata.get_dfa_4()
        self.assertAreEquivalentFAs(dfa, ndfa)

    def test_dfa_ndfa_equivalence_5(self):
        dfa = OtherAutomata.get_nfa_5()
        ndfa = OtherAutomata.get_dfa_5()
        self.assertAreEquivalentFAs(dfa, ndfa)

    def test_e_commerce_equivalent_to_itself(self):
        e_commerce_automata = OtherAutomata.get_reduced_ecommerce_automaton()
        self.assertAreEquivalentFAs(e_commerce_automata, e_commerce_automata)

    def test_e_commerce_equivalence_with_reduced_version(self):
        e_commerce_automata = OtherAutomata.get_reduced_ecommerce_automaton()
        reduced_e_commerce_automata = OtherAutomata.get_reduced_ecommerce_automaton()
        self.assertAreEquivalentFAs(e_commerce_automata, reduced_e_commerce_automata)

    def test_comparator_equivalency_when_different_1(self):
        automaton = OtherAutomata.get_nfa_1()
        nonEquivalentDfa = OtherAutomata.get_dfa_2()
        self.assertAreNotEquivalentFAs(automaton, nonEquivalentDfa)

    def test_comparator_equivalency_when_different_2(self):
        automaton = OtherAutomata.get_nfa_2()
        nonEquivalentDfa = OtherAutomata.get_dfa_1()
        self.assertAreNotEquivalentFAs(automaton, nonEquivalentDfa)

    def test_comparator_equivalency_through_counterexample(self):
        automaton = OtherAutomata.get_nfa_1()
        equivalentDfa = OtherAutomata.get_dfa_1()
        comparator = DFAComparator()
        automaton = AutomataConvertor.convert_nfa_to_dfa(automaton)
        counterexample = comparator.get_counterexample_between(
            automaton, equivalentDfa)
        self.assertIsNone(counterexample)

    def test_comparator_returns_valid_counterexample(self):
        nfa = OtherAutomata.get_nfa_1()
        nonEquivalentDfa = OtherAutomata.get_dfa_2()
        transformedNfa = AutomataConvertor.convert_nfa_to_dfa(nfa)                
        comparator = DFAComparator()
        counterexample = comparator.get_counterexample_between(
            transformedNfa, nonEquivalentDfa)
        self.assertIsNotNone(counterexample)
        self.assertTrue(transformedNfa.accepts(counterexample) !=
                        nonEquivalentDfa.accepts(counterexample))

    def test_comparator_returns_valid_counterexample_2(self):
        ecommerce_automaton = OtherAutomata.get_ecommerce_automaton()
        different_ecommerce_automaton = OtherAutomata.get_different_ecommerce_automaton_NFA()
        different_ecommerce_automaton = AutomataConvertor.convert_nfa_to_dfa(different_ecommerce_automaton)     
        comparator = DFAComparator()
        counterexample = comparator.get_counterexample_between(
            ecommerce_automaton, different_ecommerce_automaton)
        self.assertIsNotNone(counterexample)
        self.assertTrue(ecommerce_automaton.accepts(counterexample) !=
                        different_ecommerce_automaton.accepts(counterexample))

    def test_nfa_learning_FAs(self):
        dfa = BolligHabermehlKernLeuckerAutomata.get_first_example_DFA()
        nfa = BolligHabermehlKernLeuckerAutomata.get_first_example_NFA()
        self.assertAreEquivalentFAs(dfa, nfa)
        self.assertAreEquivalentFAs(nfa, dfa)

    def _areEquivalentFAs(self, automaton1, automaton2):        
        if type(automaton1) == DFA and type(automaton2) == DFA:
            comparator = DFAComparator()
        elif type(automaton1) == NFA and type(automaton2)== NFA:
            comparator = NFAComparator()
        else:
            if type(automaton1) == DFA:
                automaton2 = AutomataConvertor.convert_nfa_to_dfa(automaton2)                
            else:
                automaton1 = AutomataConvertor.convert_nfa_to_dfa(automaton1)    
            comparator = DFAComparator()
        areEquivalent = comparator.are_equivalent(automaton1, automaton2)
        return areEquivalent

    def assertAreEquivalentFAs(self, automaton1, automaton2):        
        assert(self._areEquivalentFAs(automaton1, automaton2))

    def assertAreNotEquivalentFAs(self, automaton1, automaton2):        
        self.assertFalse(self._areEquivalentFAs(automaton1, automaton2))
