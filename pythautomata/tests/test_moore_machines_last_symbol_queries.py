import random
from unittest import TestCase

from pythautomata.base_types.sequence import Sequence
from pythautomata.automata_definitions.sample_moore_machines import SampleMooreMachines
from pythautomata.base_types.symbol import SymbolStr
from pythautomata.utilities import simple_mm_generator
from pythautomata.base_types.alphabet import Alphabet

class TestMooreMachinesLastSymbolQueries(TestCase):

    def test_empty_sequence(self):
        moore_machine = SampleMooreMachines.get_3_states_automaton()
        emptySequence = Sequence()

        res = moore_machine.last_symbol(emptySequence)

        expected_result = moore_machine.initial_state.value

        return self.assertEqual(expected_result, res)

    def test_non_empty_sequence(self):
        moore_machine = SampleMooreMachines.get_3_states_automaton()
        a_a_symbols = [SymbolStr(SampleMooreMachines.get_a_symbol()), 
                        SymbolStr(SampleMooreMachines.get_a_symbol())]
        non_empty_sequence = Sequence(a_a_symbols)

        res = moore_machine.last_symbol(non_empty_sequence)

        expected_result = SymbolStr(SampleMooreMachines.get_c_symbol())

        return self.assertEqual(expected_result, res)
    
    def test_get_access_string(self):
        automaton = SampleMooreMachines.get_3_states_automaton()

        expected_state = random.choice(list(automaton.states))

        sequence = automaton.get_access_string(expected_state)

        value = automaton.process_query(sequence)

        return self.assertEqual(expected_state.value, value)
    
    def test_get_access_string_2(self):
        tripleAlphabet = Alphabet(
            frozenset([SymbolStr('a'), SymbolStr('b'), SymbolStr('c')]))
        out_alphabet = Alphabet(frozenset([SymbolStr(str(i)) for i in range(50)]))

        for _ in range(20):
            automaton = simple_mm_generator.generate_moore_machine(tripleAlphabet, out_alphabet, 50)

            expected_state = random.choice(list(automaton.states))

            sequence = automaton.get_access_string(expected_state)

            value = automaton.process_query(sequence)

            print(sequence)
            
            self.assertEqual(expected_state.value, value)
