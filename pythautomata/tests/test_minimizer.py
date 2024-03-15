from unittest import TestCase

from pythautomata.automata_definitions.other_automata import OtherAutomata
from pythautomata.utilities.dfa_minimizer import DFAMinimizer
from pythautomata.utilities.moore_machine_minimizer import MooreMachineMinimizer
from pythautomata.utilities.automata_converter import AutomataConverter

class TestMinimizers(TestCase):

    def test_dfa_minimization_1(self):
        automaton = OtherAutomata.get_automaton_1()
        minimized_automaton = DFAMinimizer(automaton).minimize()
        expected_minimized_automaton = OtherAutomata.get_automaton_1_minimized()
        self.assertEqual(minimized_automaton, expected_minimized_automaton)

    def test_dfa_minimization_2(self):
        non_minimizable_automaton = OtherAutomata.get_non_minimizable_automaton_1()
        minimized_automaton = DFAMinimizer(
            non_minimizable_automaton).minimize()
        expected_minimized_automaton = OtherAutomata.get_non_minimizable_automaton_1()
        self.assertEqual(minimized_automaton, expected_minimized_automaton)

    def test_dfa_minimization_3(self):
        non_minimizable_automaton = OtherAutomata.get_non_minimizable_automaton_2()
        minimized_automaton = DFAMinimizer(
            non_minimizable_automaton).minimize()
        expected_minimized_automaton = OtherAutomata.get_non_minimizable_automaton_2()
        self.assertEqual(minimized_automaton, expected_minimized_automaton)

    def test_dfa_minimization_4(self):
        automaton = OtherAutomata.get_automaton_2()
        minimized_automaton = DFAMinimizer(automaton).minimize()
        expected_minimized_automaton = OtherAutomata.get_automaton_2_minimized()
        self.assertEqual(minimized_automaton, expected_minimized_automaton)

    def test_dfa_minimization_5(self):
        automaton = OtherAutomata.get_automaton_3()
        minimized_automaton = DFAMinimizer(automaton).minimize()
        expected_minimized_automaton = OtherAutomata.get_automaton_3_minimized()
        self.assertEqual(minimized_automaton, expected_minimized_automaton)

    def test_dfa_minimization_6(self):
        non_minimizable_automaton = OtherAutomata.get_non_minimizable_automaton_3()
        minimized_automaton = DFAMinimizer(
            non_minimizable_automaton).minimize()
        expected_minimized_automaton = OtherAutomata.get_non_minimizable_automaton_3()
        self.assertEqual(minimized_automaton, expected_minimized_automaton)

    def test_dfa_minimization_7(self):
        automaton = OtherAutomata.get_automaton_4()
        minimized_automaton = DFAMinimizer(automaton).minimize()
        expected_minimized_automaton = OtherAutomata.get_automaton_4_minimized()
        self.assertEqual(minimized_automaton, expected_minimized_automaton)

    def test_mm_minimization_1(self):
        moore_machine = AutomataConverter.convert_dfa_to_moore_machine(OtherAutomata.get_automaton_1())
        minimized_moore_machine = MooreMachineMinimizer(moore_machine).minimize()
        expected_minimized_moore_machine = AutomataConverter.convert_dfa_to_moore_machine(OtherAutomata.get_automaton_1_minimized())
        self.assertEqual(minimized_moore_machine, expected_minimized_moore_machine)

    def test_mm_minimization_2(self):
        non_minimizable_moore_machine = AutomataConverter.convert_dfa_to_moore_machine(OtherAutomata.get_non_minimizable_automaton_1())
        minimized_moore_machine = MooreMachineMinimizer(
            non_minimizable_moore_machine).minimize()
        expected_minimized_moore_machine = AutomataConverter.convert_dfa_to_moore_machine(OtherAutomata.get_non_minimizable_automaton_1())
        self.assertEqual(minimized_moore_machine, expected_minimized_moore_machine)

    def test_mm_minimization_3(self):
        non_minimizable_moore_machine = AutomataConverter.convert_dfa_to_moore_machine(OtherAutomata.get_non_minimizable_automaton_2())
        minimized_moore_machine = MooreMachineMinimizer(
            non_minimizable_moore_machine).minimize()
        expected_minimized_moore_machine = AutomataConverter.convert_dfa_to_moore_machine(OtherAutomata.get_non_minimizable_automaton_2())
        self.assertEqual(minimized_moore_machine, expected_minimized_moore_machine)

    def test_mm_minimization_4(self):
        moore_machine = AutomataConverter.convert_dfa_to_moore_machine(OtherAutomata.get_automaton_2())
        minimized_moore_machine = MooreMachineMinimizer(moore_machine).minimize()
        expected_minimized_moore_machine = AutomataConverter.convert_dfa_to_moore_machine(OtherAutomata.get_automaton_2_minimized())
        self.assertEqual(minimized_moore_machine, expected_minimized_moore_machine)

    def test_mm_minimization_5(self):
        moore_machine = AutomataConverter.convert_dfa_to_moore_machine(OtherAutomata.get_automaton_3())
        minimized_moore_machine = MooreMachineMinimizer(moore_machine).minimize()
        expected_minimized_moore_machine = AutomataConverter.convert_dfa_to_moore_machine(OtherAutomata.get_automaton_3_minimized())
        self.assertEqual(minimized_moore_machine, expected_minimized_moore_machine)

    def test_mm_minimization_6(self):
        non_minimizable_moore_machine = AutomataConverter.convert_dfa_to_moore_machine(OtherAutomata.get_non_minimizable_automaton_3())
        minimized_moore_machine = MooreMachineMinimizer(
            non_minimizable_moore_machine).minimize()
        expected_minimized_moore_machine = AutomataConverter.convert_dfa_to_moore_machine(OtherAutomata.get_non_minimizable_automaton_3())
        self.assertEqual(minimized_moore_machine, expected_minimized_moore_machine)

    def test_mm_minimization_7(self):
        moore_machine = AutomataConverter.convert_dfa_to_moore_machine(OtherAutomata.get_automaton_4())
        minimized_moore_machine = MooreMachineMinimizer(moore_machine).minimize()
        expected_minimized_moore_machine = AutomataConverter.convert_dfa_to_moore_machine(OtherAutomata.get_automaton_4_minimized())
        self.assertEqual(minimized_moore_machine, expected_minimized_moore_machine)
