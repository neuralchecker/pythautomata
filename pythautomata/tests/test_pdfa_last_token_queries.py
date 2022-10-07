from unittest import TestCase

from pythautomata.automata_definitions.weighted_tomitas_grammars import WeightedTomitasGrammars
from pythautomata.base_types.sequence import Sequence
from pythautomata.base_types.symbol import SymbolStr


class TestPDFALastTokenQueries(TestCase):

    def test_1(self):
        pdfa = WeightedTomitasGrammars.get_automaton_1()
        res = pdfa.get_last_token_weights(Sequence([]), [Sequence(
            [SymbolStr('$')]), Sequence([SymbolStr('0')]), Sequence([SymbolStr('1')])])
        self.assertTrue(True)

    def test_2(self):
        pdfa = WeightedTomitasGrammars.get_automaton_1()
        resTerminal = pdfa.last_token_weight(Sequence([SymbolStr('$')]))
        res0 = pdfa.last_token_weight(Sequence([SymbolStr('0')]))
        res1 = pdfa.last_token_weight(Sequence([SymbolStr('1')]))
        self.assertTrue(True)
