from unittest import TestCase
from base_types.symbol import SymbolChar
from base_types.alphabet import Alphabet
from base_types.sequence import Sequence
from sequence_generators.sequence_generator import SequenceGenerator

abcAlphabet = Alphabet(frozenset(
    [SymbolChar('a'), SymbolChar('b'), SymbolChar('c')]))


class TestSequence(TestCase):

    def test_word(self):
        sequence = Sequence([SymbolChar('a'), SymbolChar('b'), SymbolChar('c')])
        self.assertEqual(len(sequence.value), 3)

    def test_word_iteration(self):
        sequence = Sequence([SymbolChar('a'), SymbolChar('b'), SymbolChar('c')])
        sequence += SymbolChar('b')
        self.assertEqual(len(sequence.value), 4)

    def test_word_iteration_2(self):
        sequence = Sequence([SymbolChar('a'), SymbolChar('b'), SymbolChar('c')])
        sequence += Sequence([SymbolChar('b'), SymbolChar('c')])
        self.assertEqual(len(sequence.value), 5)
