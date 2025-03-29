from unittest import TestCase

from pythautomata.automata_definitions.tomitas_grammars import TomitasGrammars
from pythautomata.utilities import pdfa_generator
from pythautomata.utilities import nicaud_dfa_generator
from pythautomata.base_types.alphabet import Alphabet
from pythautomata.base_types.symbol import SymbolStr

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

    def test_8(self):
        dfa = TomitasGrammars.get_automaton_7()
        pdfa = pdfa_generator.pdfa_from_dfa(dfa, distributions=3, max_shift=0)
        self.assertEqual(pdfa, pdfa)

    def test_9(self):
        dfa = TomitasGrammars.get_automaton_7()
        pdfa = pdfa_generator.pdfa_from_dfa(
            dfa, distributions=1, max_shift=0.1)
        self.assertEqual(pdfa, pdfa)

    def test_10(self):
        dfa = TomitasGrammars.get_automaton_7()
        pdfa = pdfa_generator.pdfa_from_dfa(
            dfa, distributions=1, max_shift=0.1, zero_probability=0.2)
        self.assertEqual(pdfa, pdfa)
    
    def test_11(self):
        dfa = TomitasGrammars.get_automaton_5()
        pdfa = pdfa_generator.pdfa_from_dfa(
            dfa, distributions=1, max_shift=0.1, zero_probability=0.5)
        self.assertEqual(pdfa, pdfa)
    
    def test_12(self):
        dfa = TomitasGrammars.get_automaton_5()
        pdfa = pdfa_generator.pdfa_from_dfa(
            dfa, distributions=1, max_shift=0.1, zero_probability=1)
        self.assertEqual(pdfa, pdfa)
    
    def test_13(self):
        symbols = []
        for i in range(10):
            symbols.append(SymbolStr(str(i)))
        mediumAlphabet = Alphabet(frozenset(symbols))
        generated_automata = nicaud_dfa_generator.generate_dfa(
            mediumAlphabet, 200)
        dfa = generated_automata
        pdfa = pdfa_generator.pdfa_from_dfa(
            dfa, distributions=100, max_shift=0.3, zero_probability=0.5, make_absorbent=True)
        self.assertEqual(pdfa, pdfa)
