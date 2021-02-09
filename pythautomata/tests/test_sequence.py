from unittest import TestCase
from base_types.symbol import SymbolStr
from base_types.alphabet import Alphabet
from base_types.sequence import Sequence

abcAlphabet = Alphabet(frozenset(
    [SymbolStr('a'), SymbolStr('b'), SymbolStr('c')]))


class TestSequence(TestCase):

    def test_word(self):
        sequence = Sequence([SymbolStr('a'), SymbolStr('b'), SymbolStr('c')])
        self.assertEqual(len(sequence.value), 3)

    def test_word_iteration(self):
        sequence = Sequence([SymbolStr('a'), SymbolStr('b'), SymbolStr('c')])
        sequence += SymbolStr('b')
        self.assertEqual(len(sequence.value), 4)

    def test_word_iteration_2(self):
        sequence = Sequence([SymbolStr('a'), SymbolStr('b'), SymbolStr('c')])
        sequence += Sequence([SymbolStr('b'), SymbolStr('c')])
        self.assertEqual(len(sequence.value), 5)
