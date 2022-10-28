from unittest import TestCase

from pythautomata.base_types.sequence import Sequence
from pythautomata.automata_definitions.sample_moore_machines import SampleMooreMachines
from pythautomata.base_types.symbol import SymbolStr



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
