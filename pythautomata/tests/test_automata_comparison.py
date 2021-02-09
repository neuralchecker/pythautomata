from itertools import chain
from unittest import TestCase
from model_comparators.hopcroft_karp_comparison_strategy import HopcroftKarpComparisonStrategy as AutomataComparator
from tests.automata_definitions.other_automata import OtherAutomata
from tests.automata_definitions.tomitas_grammars import TomitasGrammars
from tests.automata_definitions.omlin_giles_automata import OmlinGilesAutomata
from tests.automata_definitions.tomitas_grammars import TomitasGrammars


class TestAutomataComparison(TestCase):

    def test_equivalence_reflexiveness(self):
        mergedAutomata = list(chain(TomitasGrammar.get_all_automata(),
                                    OmlinGilesAutomata.get_all_automata(),
                                    OtherAutomata.get_all_automata()))
        for automaton in mergedAutomata:
            self.assertAreEquivalent(automaton, automaton)

    def test_equivalence_minimized_automaton_1(self):
        automaton = OtherAutomata.get_automaton_1()
        minimized_automaton = OtherAutomata.get_automaton_1_minimized()
        self.assertAreEquivalent(automaton, minimized_automaton)

    def test_equivalence_minimized_automaton_2(self):
        automaton = OtherAutomata.get_automaton_2()
        minimized_automaton = OtherAutomata.get_automaton_2_minimized()
        self.assertAreEquivalent(automaton, minimized_automaton)

    def test_equivalence_minimized_automaton_3(self):
        automaton = OtherAutomata.get_automaton_3()
        minimized_automaton = OtherAutomata.get_automaton_3_minimized()
        self.assertAreEquivalent(automaton, minimized_automaton)

    def test_equivalence_minimized_automaton_4(self):
        automaton = OtherAutomata.get_automaton_4()
        minimized_automaton = OtherAutomata.get_automaton_4_minimized()
        self.assertAreEquivalent(automaton, minimized_automaton)

    def test_dfa_ndfa_equivalence_1(self):
        dfa = OtherAutomata.get_nfa_1()
        ndfa = OtherAutomata.get_dfa_1()
        self.assertAreEquivalent(dfa, ndfa)

    def test_dfa_ndfa_equivalence_2(self):
        dfa = OtherAutomata.get_nfa_2()
        ndfa = OtherAutomata.get_dfa_2()
        self.assertAreEquivalent(dfa, ndfa)

    def test_dfa_ndfa_equivalence_3(self):
        dfa = OtherAutomata.get_nfa_3()
        ndfa = OtherAutomata.get_dfa_3()
        self.assertAreEquivalent(dfa, ndfa)

    def test_dfa_ndfa_equivalence_4(self):
        dfa = OtherAutomata.get_nfa_4()
        ndfa = OtherAutomata.get_dfa_4()
        self.assertAreEquivalent(dfa, ndfa)

    def test_dfa_ndfa_equivalence_5(self):
        dfa = OtherAutomata.get_nfa_5()
        ndfa = OtherAutomata.get_dfa_5()
        self.assertAreEquivalent(dfa, ndfa)

    def test_e_commerce_equivalent_to_itself(self):
        e_commerce_automata = OtherAutomata.get_reduced_ecommerce_automaton()
        self.assertAreEquivalent(e_commerce_automata, e_commerce_automata)

    def test_e_commerce_equivalence_with_reduced_version(self):
        e_commerce_automata = OtherAutomata.get_reduced_ecommerce_automaton()
        reduced_e_commerce_automata = OtherAutomata.get_reduced_ecommerce_automaton()
        self.assertAreEquivalent(
            e_commerce_automata, reduced_e_commerce_automata)

    def test_comparator_equivalency_when_different_1(self):
        automaton = OtherAutomata.get_nfa_1()
        nonEquivalentDfa = OtherAutomata.get_dfa_2()
        areEquivalent = AutomataComparator.are_equivalent(
            automaton, nonEquivalentDfa)
        self.assertFalse(areEquivalent)

    def test_comparator_equivalency_when_different_2(self):
        automaton = OtherAutomata.get_nfa_2()
        nonEquivalentDfa = OtherAutomata.get_dfa_1()
        areEquivalent = AutomataComparator.are_equivalent(
            automaton, nonEquivalentDfa)
        self.assertFalse(areEquivalent)

    def test_comparator_equivalency_through_counterexample(self):
        automaton = OtherAutomata.get_nfa_1()
        equivalentDfa = OtherAutomata.get_dfa_1()
        counterexample = AutomataComparator.get_counterexample_between(
            automaton, equivalentDfa)
        self.assertIsNone(counterexample)

    def test_comparator_returns_valid_counterexample(self):
        automaton = OtherAutomata.get_nfa_1()
        nonEquivalentDfa = OtherAutomata.get_dfa_2()
        counterexample = AutomataComparator.get_counterexample_between(
            automaton, nonEquivalentDfa)
        self.assertIsNotNone(counterexample)
        self.assertTrue(automaton.accepts(counterexample) !=
                        nonEquivalentDfa.accepts(counterexample))

    def test_comparator_returns_valid_counterexample_2(self):
        ecommerce_automaton = OtherAutomata.get_ecommerce_automaton()
        different_ecommerce_automaton = OtherAutomata.get_different_ecommerce_automaton()
        counterexample = AutomataComparator.get_counterexample_between(
            ecommerce_automaton, different_ecommerce_automaton)
        self.assertIsNotNone(counterexample)
        self.assertTrue(ecommerce_automaton.accepts(counterexample) !=
                        different_ecommerce_automaton.accepts(counterexample))

    def assertAreEquivalent(self, automaton1, automaton2):
        areEquivalent = AutomataComparator.are_equivalent(
            automaton1, automaton2)
        self.assertTrue(areEquivalent)
