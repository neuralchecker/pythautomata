from unittest import TestCase

from pythautomata.automata_definitions.other_automata import OtherAutomata
from pythautomata.automata_definitions.sample_mealy_machines import SampleMealyMachines
from pythautomata.utilities.automata_converter import AutomataConverter
from pythautomata.automata_definitions.sample_moore_machines import SampleMooreMachines


class TestAutomataConvertor(TestCase):

    def test_conversion_1(self):
        automaton = OtherAutomata.get_nfa_1()
        automata_converted_to_dfa = AutomataConverter.convert_nfa_to_dfa(
            automaton)
        expected_converted_dfa = OtherAutomata.get_dfa_1()
        self.assertEqual(automata_converted_to_dfa, expected_converted_dfa)

    def test_conversion_2(self):
        automaton = OtherAutomata.get_nfa_2()
        automata_converted_to_dfa = AutomataConverter.convert_nfa_to_dfa(
            automaton)
        expected_converted_dfa = OtherAutomata.get_dfa_2()
        self.assertEqual(automata_converted_to_dfa, expected_converted_dfa)

    def test_conversion_3(self):
        automaton = OtherAutomata.get_nfa_3()
        automata_converted_to_dfa = AutomataConverter.convert_nfa_to_dfa(
            automaton)
        expected_converted_dfa = OtherAutomata.get_dfa_3()
        self.assertEqual(automata_converted_to_dfa, expected_converted_dfa)

    def test_conversion_4(self):
        automaton = OtherAutomata.get_nfa_4()
        automata_converted_to_dfa = AutomataConverter.convert_nfa_to_dfa(
            automaton)
        expected_converted_dfa = OtherAutomata.get_dfa_4()
        self.assertEqual(automata_converted_to_dfa, expected_converted_dfa)

    def test_conversion_5(self):
        automaton = OtherAutomata.get_nfa_5()
        automata_converted_to_dfa = AutomataConverter.convert_nfa_to_dfa(
            automaton)
        expected_converted_dfa = OtherAutomata.get_dfa_5()
        self.assertEqual(automata_converted_to_dfa, expected_converted_dfa)

    def test_conversion_6(self):
        machine = SampleMooreMachines.get_tomitas_automaton_1()
        converted_mealy_machine = AutomataConverter.convert_moore_machine_to_mealy_machine(
            machine)
        expected_converted_mealy_machine = SampleMealyMachines.get_tomitas_automaton_1()
        self.assertEqual(converted_mealy_machine,
                         expected_converted_mealy_machine)
