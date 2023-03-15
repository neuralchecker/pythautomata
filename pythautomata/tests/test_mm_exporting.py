from unittest import TestCase

from pythautomata.automata_definitions.sample_moore_machines import SampleMooreMachines
from pythautomata.model_exporters.dot_exporters.moore_dot_exporting_strategy import MooreDotExportingStrategy
from pythautomata.model_exporters.standard_exporters.moore_standard_dot_exporting_strategy import MooreStandardDotExportingStrategy


class TestMMExporting(TestCase):

    def test_1(self):
        mm = SampleMooreMachines.get_3_states_automaton()
        MooreDotExportingStrategy().export(mm, "./output_models/tests")
        MooreStandardDotExportingStrategy().export(mm, "./output_models/tests")

    def test_2(self):
        mm = SampleMooreMachines.get_tomitas_automaton_1()
        MooreDotExportingStrategy().export(mm, "./output_models/tests")
        MooreStandardDotExportingStrategy().export(mm, "./output_models/tests")

    def test_3(self):
        mm = SampleMooreMachines.get_tomitas_automaton_2()
        MooreDotExportingStrategy().export(mm, "./output_models/tests")
        MooreStandardDotExportingStrategy().export(mm, "./output_models/tests")
