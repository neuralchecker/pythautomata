from unittest import TestCase

from pythautomata.automata_definitions.sample_moore_machines import SampleMooreMachines
from pythautomata.model_exporters.dot_exporting_mm_strategy import DotExportingMMStrategy
from pythautomata.model_exporters.standard_dot_exporting_mm_strategy import StandardDotMMExportingStrategy


class TestMMExporting(TestCase):

    def test_1(self):
        mm = SampleMooreMachines.get_3_states_automaton()
        DotExportingMMStrategy().export(mm, "./output_models/tests")
        StandardDotMMExportingStrategy().export(mm, "./output_models/tests")

    def test_2(self):
        mm = SampleMooreMachines.get_tomitas_automaton_1()
        DotExportingMMStrategy().export(mm, "./output_models/tests")
        StandardDotMMExportingStrategy().export(mm, "./output_models/tests")

    def test_3(self):
        mm = SampleMooreMachines.get_tomitas_automaton_2()
        DotExportingMMStrategy().export(mm, "./output_models/tests")
        StandardDotMMExportingStrategy().export(mm, "./output_models/tests")