from unittest import TestCase

from pythautomata.automata_definitions.sample_mealy_machines import SampleMealyMachines
from pythautomata.model_exporters.standard_exporters.mealy_standard_dot_exporting_strategy import MealyStandardDotExportingStrategy
from pythautomata.utilities.standard_dot_notation_mealy_importer import StandardDotNotationMealyImporter


class TestMealyLoading(TestCase):

    def test_1(self):
        for mealy_machine in SampleMealyMachines.get_all_mealy_machines():
            name = mealy_machine._name
            mealy_machine._name = name + "_standard"

            MealyStandardDotExportingStrategy().export(
                mealy_machine, "./output_models/tests")

            path = './output_models/tests'+'/'+mealy_machine._name+'.dot'
            loaded_mealy = StandardDotNotationMealyImporter().import_automata(path)

            self.assertEqual(mealy_machine, loaded_mealy)
