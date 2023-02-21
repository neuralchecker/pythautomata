from unittest import TestCase

from pythautomata.automata_definitions.sample_mealy_machines import SampleMealyMachines
from pythautomata.model_exporters.standard_dot_exporting_mealy_strategy import StandardDotExportingMealyStrategy


class TestMealyExporting(TestCase):

    def test_1(self):
        mealy = SampleMealyMachines.get_3_states_mealy_machine()
        StandardDotExportingMealyStrategy().export(mealy, "./output_models/tests")

    def test_2(self):
        mealy = SampleMealyMachines.get_tomitas_automaton_1()
        StandardDotExportingMealyStrategy().export(mealy, "./output_models/tests")
