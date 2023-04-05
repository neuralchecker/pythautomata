from unittest import TestCase
from collections import OrderedDict

from pythautomata.automata.fast_implementations.fast_pdfa import FastProbabilisticDeterministicFiniteAutomaton
from pythautomata.automata.fast_implementations.fast_pdfa_converter import FastProbabilisticDeterministicFiniteAutomatonConverter
from pythautomata.automata_definitions.tomitas_grammars import TomitasGrammars
from pythautomata.utilities import pdfa_generator
from pythautomata.utilities.uniform_word_sequence_generator import UniformWordSequenceGenerator
from pythautomata.base_types.sequence import Sequence


class TestFastPDFAConverter(TestCase):
    def _seq_to_list_of_ints(self, sequence):
        return [int(x.value) for x in sequence]

    def test_1(self):
        dfa = TomitasGrammars.get_automaton_1()
        pdfa = pdfa_generator.pdfa_from_dfa(dfa, terminal_symbol="3")
        fast_pdfa = FastProbabilisticDeterministicFiniteAutomatonConverter().to_fast_pdfa(pdfa)
        symbols = sorted(list(pdfa.alphabet.symbols))
        symbols = symbols + [pdfa.terminal_symbol]
        int_symbols = [int(x.value) for x in symbols]
        sequences = UniformWordSequenceGenerator(
            pdfa.alphabet, 100).generate_words(1000)

        for seq in sequences:
            seq_int = self._seq_to_list_of_ints(seq)
            pdfa_res = pdfa.last_token_probabilities(seq, symbols)
            pdfa_res = OrderedDict(zip(int_symbols, pdfa_res))
            fast_pdfa_res = fast_pdfa.next_token_probabilities(seq_int)
            pdfa_prob = pdfa.sequence_probability(seq)
            fast_pdfa_prob = fast_pdfa.sequence_probability(seq_int)
            self.assertEqual(pdfa_res, fast_pdfa_res)
            self.assertTrue(abs(pdfa_prob - fast_pdfa_prob) < 0.000001)

    # def test_2(self):
    #     dfa = TomitasGrammars.get_automaton_2()
    #     pdfa = pdfa_generator.pdfa_from_dfa(dfa)
    #     self.assertEqual(pdfa, pdfa)

    # def test_3(self):
    #     dfa = TomitasGrammars.get_automaton_3()
    #     pdfa = pdfa_generator.pdfa_from_dfa(dfa)
    #     self.assertEqual(pdfa, pdfa)

    # def test_4(self):
    #     dfa = TomitasGrammars.get_automaton_4()
    #     pdfa = pdfa_generator.pdfa_from_dfa(dfa)
    #     self.assertEqual(pdfa, pdfa)

    # def test_5(self):
    #     dfa = TomitasGrammars.get_automaton_5()
    #     pdfa = pdfa_generator.pdfa_from_dfa(dfa)
    #     self.assertEqual(pdfa, pdfa)

    # def test_6(self):
    #     dfa = TomitasGrammars.get_automaton_6()
    #     pdfa = pdfa_generator.pdfa_from_dfa(dfa)
    #     self.assertEqual(pdfa, pdfa)

    # def test_7(self):
    #     dfa = TomitasGrammars.get_automaton_7()
    #     pdfa = pdfa_generator.pdfa_from_dfa(dfa)
    #     self.assertEqual(pdfa, pdfa)

    # # def test_8(self):
    # #     dfa = TomitasGrammars.get_automaton_7()
    # #     pdfa = pdfa_generator.pdfa_from_dfa(dfa, distributions=3, max_shift=0)
    # #     self.assertEqual(pdfa, pdfa)

    # # def test_9(self):
    # #     dfa = TomitasGrammars.get_automaton_7()
    # #     pdfa = pdfa_generator.pdfa_from_dfa(
    # #         dfa, distributions=1, max_shift=0.1)
    # #     self.assertEqual(pdfa, pdfa)
