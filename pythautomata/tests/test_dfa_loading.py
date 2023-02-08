from unittest import TestCase

from pythautomata.automata_definitions.tomitas_grammars import TomitasGrammars
from pythautomata.model_exporters.standard_dot_exporting_strategy import StandardDotExportingStrategy
from pythautomata.utilities.standard_dot_notation_importer import StandardDotNotationImporter


class TestDFALoading(TestCase):

    def test_1(self):
        for dfa in TomitasGrammars.get_all_automata():
            name = dfa.name
            dfa.name = name + "_standard"
            StandardDotExportingStrategy().export(dfa, "./output_models/tests")
            path = './output_models/tests'+'/'+dfa.name+'.dot'
            loaded_dfa = StandardDotNotationImporter.import_automata(path)
            self.assertEqual(dfa, loaded_dfa)

    def test2(self):
        name = "DFArandomChamparnaudParanthon_1000States_20Inputs_0"
        path = './output_models/tests'+'/'+name+'.dot'
        loaded_dfa = StandardDotNotationImporter.import_automata(path)
        loaded_dfa.name += "2"
        StandardDotExportingStrategy().export(loaded_dfa, "./output_models/tests")
        path = './output_models/tests'+'/'+loaded_dfa.name+'.dot'
        loaded_dfa2 = StandardDotNotationImporter.import_automata(path)
        self.assertEqual(loaded_dfa, loaded_dfa2)
