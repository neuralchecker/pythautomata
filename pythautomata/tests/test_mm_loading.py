from unittest import TestCase

from pythautomata.automata_definitions.sample_moore_machines import SampleMooreMachines
from pythautomata.model_exporters.standard_dot_exporting_mm_strategy import StandardDotMMExportingStrategy
from pythautomata.utilities.standard_dot_notation_mm_importer import StandardDotMMNotationImporter
class TestMMLoading(TestCase):

    def test_1(self):
        for mm in SampleMooreMachines.get_all_automata():
            StandardDotMMExportingStrategy().export(mm, "./output_models/tests")
            path = './output_models/tests'+'/Standard '+mm._name+'.dot'
            loaded_mm = StandardDotMMNotationImporter.import_automata(path)
            self.assertEqual(mm, loaded_mm)