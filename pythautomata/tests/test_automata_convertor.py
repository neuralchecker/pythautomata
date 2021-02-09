from base_types.state import State
from unittest import TestCase
from abstract.finite_automaton import FiniteAutomaton
from utilities.automata_convertor import AutomataConvertor
from tests.automata_definitions.other_automata import OtherAutomata


class TestAutomataConvertor(TestCase):

    def test_conversion_1(self):
        automaton = OtherAutomata.get_nfa_1()
        automata_converted_to_dfa = AutomataConvertor.convert_nfa_to_dfa(
            automaton)
        expected_converted_dfa = OtherAutomata.get_dfa_1()
        self.assertEqual(automata_converted_to_dfa, expected_converted_dfa)

    def test_conversion_2(self):
        automaton = OtherAutomata.get_nfa_2()
        automata_converted_to_dfa = AutomataConvertor.convert_nfa_to_dfa(
            automaton)
        expected_converted_dfa = OtherAutomata.get_dfa_2()
        self.assertEqual(automata_converted_to_dfa, expected_converted_dfa)

    def test_conversion_3(self):
        automaton = OtherAutomata.get_nfa_3()
        automata_converted_to_dfa = AutomataConvertor.convert_nfa_to_dfa(
            automaton)
        expected_converted_dfa = OtherAutomata.get_dfa_3()
        self.assertEqual(automata_converted_to_dfa, expected_converted_dfa)

    def test_conversion_4(self):
        automaton = OtherAutomata.get_nfa_4()
        automata_converted_to_dfa = AutomataConvertor.convert_nfa_to_dfa(
            automaton)
        expected_converted_dfa = OtherAutomata.get_dfa_4()
        self.assertEqual(automata_converted_to_dfa, expected_converted_dfa)

    def test_conversion_5(self):
        automaton = OtherAutomata.get_nfa_5()
        automata_converted_to_dfa = AutomataConvertor.convert_nfa_to_dfa(
            automaton)
        expected_converted_dfa = OtherAutomata.get_dfa_5()
        self.assertEqual(automata_converted_to_dfa, expected_converted_dfa)
