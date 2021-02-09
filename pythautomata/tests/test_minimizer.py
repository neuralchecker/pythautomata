from base_types.state import State
from unittest import TestCase
from automata.deterministic_finite_automaton import DeterministicFiniteAutomaton
from utilities.dfa_minimizer import DFAMinimizer
from tests.automata_definitions.other_automata import OtherAutomata


class TestMinimizer(TestCase):

    def test_minimization_1(self):
        automaton = OtherAutomata.get_automaton_1()
        minimized_automaton = DFAMinimizer(automaton).minimize()
        expected_minimized_automaton = OtherAutomata.get_automaton_1_minimized()
        self.assertEqual(minimized_automaton, expected_minimized_automaton)

    def test_minimization_2(self):
        non_minimizable_automaton = OtherAutomata.get_non_minimizable_automaton_1()
        minimized_automaton = DFAMinimizer(
            non_minimizable_automaton).minimize()
        expected_minimized_automaton = OtherAutomata.get_non_minimizable_automaton_1()
        self.assertEqual(minimized_automaton, expected_minimized_automaton)

    def test_minimization_3(self):
        non_minimizable_automaton = OtherAutomata.get_non_minimizable_automaton_2()
        minimized_automaton = DFAMinimizer(
            non_minimizable_automaton).minimize()
        expected_minimized_automaton = OtherAutomata.get_non_minimizable_automaton_2()
        self.assertEqual(minimized_automaton, expected_minimized_automaton)

    def test_minimization_4(self):
        automaton = OtherAutomata.get_automaton_2()
        minimized_automaton = DFAMinimizer(automaton).minimize()
        expected_minimized_automaton = OtherAutomata.get_automaton_2_minimized()
        self.assertEqual(minimized_automaton, expected_minimized_automaton)

    def test_minimization_5(self):
        automaton = OtherAutomata.get_automaton_3()
        minimized_automaton = DFAMinimizer(automaton).minimize()
        expected_minimized_automaton = OtherAutomata.get_automaton_3_minimized()
        self.assertEqual(minimized_automaton, expected_minimized_automaton)

    def test_minimization_6(self):
        non_minimizable_automaton = OtherAutomata.get_non_minimizable_automaton_3()
        minimized_automaton = DFAMinimizer(
            non_minimizable_automaton).minimize()
        expected_minimized_automaton = OtherAutomata.get_non_minimizable_automaton_3()
        self.assertEqual(minimized_automaton, expected_minimized_automaton)

    def test_minimization_7(self):
        automaton = OtherAutomata.get_automaton_4()
        minimized_automaton = DFAMinimizer(automaton).minimize()
        expected_minimized_automaton = OtherAutomata.get_automaton_4_minimized()
        self.assertEqual(minimized_automaton, expected_minimized_automaton)
