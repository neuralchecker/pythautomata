import unittest
from pythautomata.utilities import pdfa_metrics
from pythautomata.utilities.sequence_generator import SequenceGenerator
from pythautomata.automata_definitions.weighted_tomitas_grammars import WeightedTomitasGrammars


class TestPDFAMetrics(unittest.TestCase):

    def test_same_pdfa(self):
        pdfa1 = WeightedTomitasGrammars.get_automaton_3()
        pdfa2 = pdfa1
        sg = SequenceGenerator(pdfa1.alphabet, 20, 42)
        test_sequences = sg.generate_words(500)
        m1 = pdfa_metrics.log_probability_error(pdfa1, pdfa2, test_sequences)
        m2 = pdfa_metrics.wer_avg(pdfa1, pdfa2, test_sequences)
        m3 = pdfa_metrics.ndcg_score_avg(pdfa1, pdfa2, test_sequences)
        m4 = pdfa_metrics.out_of_partition_elements(
            pdfa1, pdfa2, test_sequences, 10)
        m5 = pdfa_metrics.out_of_tolerance_elements(
            pdfa1, pdfa2, test_sequences, 0.1)
        self.assertEqual(m1, 0)
        self.assertEqual(m2, 0)
        self.assertEqual(m3, 1)
        self.assertEqual(m4, 0)
        self.assertEqual(m5, 0)

    def test_different_pdfa(self):
        pdfa1 = WeightedTomitasGrammars.get_automaton_3()
        pdfa2 = WeightedTomitasGrammars.get_automaton_7()
        sg = SequenceGenerator(pdfa1.alphabet, 20, 42)
        test_sequences = sg.generate_words(500)
        m1 = pdfa_metrics.log_probability_error(pdfa1, pdfa2, test_sequences)
        m2 = pdfa_metrics.wer_avg(pdfa1, pdfa2, test_sequences)
        m3 = pdfa_metrics.ndcg_score_avg(pdfa1, pdfa2, test_sequences)
        m4 = pdfa_metrics.out_of_partition_elements(
            pdfa1, pdfa2, test_sequences, 10)
        m5 = pdfa_metrics.out_of_tolerance_elements(
            pdfa1, pdfa2, test_sequences, 0.1)
        self.assertNotEqual(m1, 0)
        self.assertNotEqual(m2, 0)
        self.assertNotEqual(m3, 1)
        self.assertNotEqual(m4, 0)
        self.assertNotEqual(m5, 0)
