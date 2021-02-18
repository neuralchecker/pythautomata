import unittest
from utilities import dfa_operations
from tests.automata_definitions.other_automata import OtherAutomata

class TestDFAOperations(unittest.TestCase):

    def test_join_1(self):
        automatonA = OtherAutomata.get_uneven_number_of_as_automaton()
        automatonB = OtherAutomata.get_uneven_number_of_symbols_automaton()
        target_join = OtherAutomata.get_uneven_number_of_as_and_symbols_automaton()
        joinedAutomaton = dfa_operations.join_DFAs(automatonA,automatonB)
        self.assertEqual(target_join, joinedAutomaton)

    def test_join_2(self):
        automatonA = OtherAutomata.get_empty_automaton()
        automatonB = OtherAutomata.get_sigma_star_automaton()
        target_join = OtherAutomata.get_empty_automaton()
        joinedAutomaton = dfa_operations.join_DFAs(automatonA,automatonB)
        self.assertEqual(target_join, joinedAutomaton)    

    def test_union_1(self):
        automatonA = OtherAutomata.get_uneven_number_of_as_automaton()
        automatonB = OtherAutomata.get_uneven_number_of_symbols_automaton()
        target_union = OtherAutomata.get_uneven_number_of_as_or_symbols_automaton()
        unionAutomaton = dfa_operations.union_DFAs(automatonA,automatonB)
        self.assertEqual(target_union, unionAutomaton)  

    def test_union_2(self):
        automatonA = OtherAutomata.get_empty_automaton()
        automatonB = OtherAutomata.get_sigma_star_automaton()
        target_join = OtherAutomata.get_sigma_star_automaton()
        unionAutomaton = dfa_operations.union_DFAs(automatonA,automatonB)
        self.assertEqual(target_join, unionAutomaton)         