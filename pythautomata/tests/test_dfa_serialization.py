import pickle
from unittest import TestCase

from pythautomata.automata_definitions.tomitas_grammars import TomitasGrammars


class TestDFASerialization(TestCase):

    def test_1(self):
        dfa = TomitasGrammars.get_automaton_1()
        data = pickle.dumps(dfa)
        dfa2 = pickle.loads(data)
        self.assertEqual(dfa, dfa2)

    def test_2(self):
        dfa = TomitasGrammars.get_automaton_2()
        data = pickle.dumps(dfa)
        dfa2 = pickle.loads(data)
        self.assertEqual(dfa, dfa2)

    def test_3(self):
        dfa = TomitasGrammars.get_automaton_3()
        data = pickle.dumps(dfa)
        dfa2 = pickle.loads(data)
        self.assertEqual(dfa, dfa2)

    def test_4(self):
        dfa = TomitasGrammars.get_automaton_4()
        data = pickle.dumps(dfa)
        dfa2 = pickle.loads(data)
        self.assertEqual(dfa, dfa2)

    def test_5(self):
        dfa = TomitasGrammars.get_automaton_5()
        data = pickle.dumps(dfa)
        dfa2 = pickle.loads(data)
        self.assertEqual(dfa, dfa2)

    def test_6(self):
        dfa = TomitasGrammars.get_automaton_6()
        data = pickle.dumps(dfa)
        dfa2 = pickle.loads(data)
        self.assertEqual(dfa, dfa2)

    def test_7(self):
        dfa = TomitasGrammars.get_automaton_7()
        data = pickle.dumps(dfa)
        dfa2 = pickle.loads(data)
        self.assertEqual(dfa, dfa2)
