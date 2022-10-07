import pickle
from unittest import TestCase

from pythautomata.automata_definitions.weighted_tomitas_grammars import WeightedTomitasGrammars


class TestPDFASerialization(TestCase):

    def test_1(self):
        pdfa = WeightedTomitasGrammars.get_automaton_1()
        data = pickle.dumps(pdfa)
        pdfa2 = pickle.loads(data)
        self.assertEqual(pdfa, pdfa2)

    def test_2(self):
        pdfa = WeightedTomitasGrammars.get_automaton_2()
        data = pickle.dumps(pdfa)
        pdfa2 = pickle.loads(data)
        self.assertEqual(pdfa, pdfa2)

    def test_3(self):
        pdfa = WeightedTomitasGrammars.get_automaton_3()
        data = pickle.dumps(pdfa)
        pdfa2 = pickle.loads(data)
        self.assertEqual(pdfa, pdfa2)

    def test_4(self):
        pdfa = WeightedTomitasGrammars.get_automaton_4()
        data = pickle.dumps(pdfa)
        pdfa2 = pickle.loads(data)
        self.assertEqual(pdfa, pdfa2)

    def test_5(self):
        pdfa = WeightedTomitasGrammars.get_automaton_5()
        data = pickle.dumps(pdfa)
        pdfa2 = pickle.loads(data)
        self.assertEqual(pdfa, pdfa2)

    def test_6(self):
        pdfa = WeightedTomitasGrammars.get_automaton_6()
        data = pickle.dumps(pdfa)
        pdfa2 = pickle.loads(data)
        self.assertEqual(pdfa, pdfa2)

    def test_7(self):
        pdfa = WeightedTomitasGrammars.get_automaton_7()
        data = pickle.dumps(pdfa)
        pdfa2 = pickle.loads(data)
        self.assertEqual(pdfa, pdfa2)
