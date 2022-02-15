from unittest import TestCase

from pythautomata.automata_definitions.weighted_tomitas_grammars import WeightedTomitasGrammars
from utilities.pdfa_operations import get_representative_sample


class TestPDFAOperations(TestCase):

    def test_1(self):
        pdfa = WeightedTomitasGrammars.get_automaton_1()
        sample = get_representative_sample(pdfa, 10)
        self.assertTrue(True)

    def test_2(self):
        pdfa = WeightedTomitasGrammars.get_automaton_2()
        sample = get_representative_sample(pdfa, 20)
        self.assertTrue(True)

    def test_3(self):
        pdfa = WeightedTomitasGrammars.get_automaton_3()
        sample = get_representative_sample(pdfa, 30)
        self.assertTrue(True)

    def test_4(self):
        pdfa = WeightedTomitasGrammars.get_automaton_4()
        sample = get_representative_sample(pdfa, 400)
        self.assertTrue(True)

    def test_5(self):
        pdfa = WeightedTomitasGrammars.get_automaton_5()
        sample = get_representative_sample(pdfa, 0)
        self.assertTrue(True)

    def test_6(self):
        pdfa = WeightedTomitasGrammars.get_automaton_6()
        sample = get_representative_sample(pdfa, 1)
        self.assertTrue(True)

    def test_7(self):
        pdfa = WeightedTomitasGrammars.get_automaton_7()
        self.assertRaises(AssertionError, get_representative_sample, pdfa, -1)
