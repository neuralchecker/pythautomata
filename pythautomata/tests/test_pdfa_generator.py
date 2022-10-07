from unittest import TestCase

from pythautomata.automata_definitions.tomitas_grammars import TomitasGrammars
from pythautomata.utilities import pdfa_generator


class TestPDFAGenerator(TestCase):

    def test_1(self):
        dfa = TomitasGrammars.get_automaton_1()
        pdfa = pdfa_generator.pdfa_from_dfa(dfa)
        self.assertEqual(pdfa, pdfa)

    def test_2(self):
        dfa = TomitasGrammars.get_automaton_2()
        pdfa = pdfa_generator.pdfa_from_dfa(dfa)
        self.assertEqual(pdfa, pdfa)

    def test_3(self):
        dfa = TomitasGrammars.get_automaton_3()
        pdfa = pdfa_generator.pdfa_from_dfa(dfa)
        self.assertEqual(pdfa, pdfa)

    def test_4(self):
        dfa = TomitasGrammars.get_automaton_4()
        pdfa = pdfa_generator.pdfa_from_dfa(dfa)
        self.assertEqual(pdfa, pdfa)

    def test_5(self):
        dfa = TomitasGrammars.get_automaton_5()
        pdfa = pdfa_generator.pdfa_from_dfa(dfa)
        self.assertEqual(pdfa, pdfa)

    def test_6(self):
        dfa = TomitasGrammars.get_automaton_6()
        pdfa = pdfa_generator.pdfa_from_dfa(dfa)
        self.assertEqual(pdfa, pdfa)

    def test_7(self):
        dfa = TomitasGrammars.get_automaton_7()
        pdfa = pdfa_generator.pdfa_from_dfa(dfa)
        self.assertEqual(pdfa, pdfa)
