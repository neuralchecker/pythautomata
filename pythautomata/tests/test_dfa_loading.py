from unittest import TestCase

from pythautomata.automata_definitions.tomitas_grammars import TomitasGrammars
from pythautomata.model_exporters.standard_exporters.dfa_standard_dot_exporting_strategy import DfaStandardDotExportingStrategy
from pythautomata.utilities.standard_dot_notation_importer import StandardDotNotationImporter


class TestDFALoading(TestCase):

    def test_1(self):
        for dfa in TomitasGrammars.get_all_automata():
            name = dfa.name
            dfa.name = name + "_standard"
            DfaStandardDotExportingStrategy().export(dfa, "./output_models/tests")
            path = './output_models/tests'+'/'+dfa.name+'.dot'
            loaded_dfa = StandardDotNotationImporter.import_automata(path)
            self.assertEqual(dfa, loaded_dfa)
