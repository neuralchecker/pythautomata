from unittest import TestCase

from pythautomata.base_types.sequence import Sequence
from pythautomata.automata_definitions.sample_moore_machines import SampleMooreMachines
from pythautomata.base_types.symbol import SymbolStr
from pythautomata.utilities.automata_converter import AutomataConverter
from pythautomata.model_comparators.moore_machine_comparison_strategy import MooreMachineComparisonStrategy
from pythautomata.automata_definitions.tomitas_grammars import TomitasGrammars as Tomitas

class TestDFAToMooreMachine(TestCase):
    def test_dfa_to_moore_machine_tomitas_automaton_1(self):
        moore_machine = SampleMooreMachines.get_tomitas_automaton_1()
        dfa = Tomitas.get_automaton_1()
        converted_dfa = AutomataConverter.convert_dfa_to_moore_machine(dfa)

        return self.assertEqual(moore_machine, converted_dfa)
    
    def test_dfa_to_moore_machine_tomitas_automaton_2(self):
        moore_machine = SampleMooreMachines.get_tomitas_automaton_2()
        dfa = Tomitas.get_automaton_2()
        converted_dfa = AutomataConverter.convert_dfa_to_moore_machine(dfa)

        return self.assertEqual(moore_machine, converted_dfa)


