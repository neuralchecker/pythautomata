from unittest import TestCase

from pythautomata.other_models.probabilistic_filter_model import ProbabilisticFilterModel
from pythautomata.automata_definitions.weighted_tomitas_grammars import WeightedTomitasGrammars
from pythautomata.base_types.sequence import Sequence
from pythautomata.base_types.symbol import SymbolStr


class TestProbabilisticFilterModel(TestCase):

    def test_1(self):
        pdfa = WeightedTomitasGrammars.get_automaton_1()
        model = ProbabilisticFilterModel(pdfa, 2)
        seq1 = Sequence([])
        seq2 = Sequence([SymbolStr('0'), SymbolStr('1')])
        seq3 = Sequence([SymbolStr('0'), SymbolStr('1'), SymbolStr('$')])
        
        pdfa_res1 = pdfa.last_token_probability(seq1)        
        pdfa_res2 = pdfa.last_token_probability(seq2)        
        pdfa_res3 = pdfa.last_token_probability(seq3)

        model_res1 = model.last_token_probability(seq1)        
        model_res2 = model.last_token_probability(seq2)        
        model_res3 = model.last_token_probability(seq3)

        self.assertEqual(pdfa_res1,model_res1)
        self.assertEqual(pdfa_res2,model_res2)
        self.assertNotEqual(pdfa_res3, model_res3)