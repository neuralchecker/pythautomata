from unittest import TestCase
from collections import OrderedDict

from pythautomata.automata.fast_implementations.fast_pdfa import FastProbabilisticDeterministicFiniteAutomaton
from pythautomata.automata.fast_implementations.fast_pdfa_converter import FastProbabilisticDeterministicFiniteAutomatonConverter
from pythautomata.automata_definitions.tomitas_grammars import TomitasGrammars
from pythautomata.utilities import pdfa_generator
from pythautomata.utilities.uniform_word_sequence_generator import UniformWordSequenceGenerator
from pythautomata.base_types.sequence import Sequence
import time


class TestFastPDFAConverter(TestCase):
    def _seq_to_list_of_ints(self, sequence):
        return [int(x.value) for x in sequence]

    def _test_from_dfa(self, dfa):
        pdfa = pdfa_generator.pdfa_from_dfa(dfa, terminal_symbol="3")
        fast_pdfa = FastProbabilisticDeterministicFiniteAutomatonConverter().to_fast_pdfa(pdfa)
        symbols = sorted(list(pdfa.alphabet.symbols))
        symbols = symbols + [pdfa.terminal_symbol]
        int_symbols = [int(x.value) for x in symbols]
        sequences = UniformWordSequenceGenerator(
            pdfa.alphabet, 100).generate_words(10)

        for seq in sequences:
            seq_int = self._seq_to_list_of_ints(seq)
            pdfa_res = pdfa.last_token_probabilities(seq, symbols)
            pdfa_res = OrderedDict(zip(int_symbols, pdfa_res))
            fast_pdfa_res = fast_pdfa.next_token_probabilities(seq_int)
            pdfa_prob = pdfa.sequence_probability(seq)
            fast_pdfa_prob = fast_pdfa.sequence_probability(seq_int)
            self.assertEqual(pdfa_res, fast_pdfa_res)
            self.assertTrue(abs(pdfa_prob - fast_pdfa_prob) < 0.000001)

    def test_tomitas(self):
        for dfa in TomitasGrammars().get_all_automata():
            self._test_from_dfa(dfa)

    # def test_speed(self):
    #     dfa = TomitasGrammars().get_automaton_7()
    #     pdfa = pdfa_generator.pdfa_from_dfa(dfa, terminal_symbol="3")
    #     fast_pdfa = FastProbabilisticDeterministicFiniteAutomatonConverter().to_fast_pdfa(pdfa)
    #     symbols = sorted(list(pdfa.alphabet.symbols))
    #     symbols = symbols + [pdfa.terminal_symbol]
    #     int_symbols = [int(x.value) for x in symbols]
    #     sequences = UniformWordSequenceGenerator(
    #         pdfa.alphabet, 100).generate_words(100)
    #     seqs_int = [self._seq_to_list_of_ints(seq) for seq in sequences]
    #     start = time.time()
    #     for i in range(10):
    #         for seq in sequences:
    #             pdfa_prob = pdfa.sequence_probability(seq)
    #     end = time.time()
    #     print(end - start)
    #     start = time.time()
    #     for i in range(10):
    #         for seq_int in seqs_int:
    #             fast_pdfa_prob = fast_pdfa.sequence_probability(seq_int)
    #     end = time.time()
    #     print(end - start)
