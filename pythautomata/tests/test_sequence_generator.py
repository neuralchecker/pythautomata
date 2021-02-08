from unittest import TestCase
import numpy as np

from base_types.symbol import SymbolChar
from base_types.alphabet import Alphabet
from base_types.sequence import Sequence
from sequence_generators.sequence_generator import SequenceGenerator

abcAlphabet = Alphabet(frozenset(
    [SymbolChar('a'), SymbolChar('b'), SymbolChar('c')]))


class TestSequenceGenerator(TestCase):

    def test_generate_word(self):
        word_len = 3
        generator = SequenceGenerator(abcAlphabet, word_len)
        sample_word = generator.generate_word(word_len)

        self.assertEqual(
            len(sample_word.value), word_len)

    def test_generate_many_times_same_word(self):
        word_len = 3
        generator = SequenceGenerator(abcAlphabet, word_len)
        number_of_words = 100
        list_words = []
        for _ in range(number_of_words):
            sample_word = generator.generate_word(word_len)
            generator.reset_seed()
            list_words.append(sample_word)

        for i in range(number_of_words):
            self.assertEqual(list_words[i], list_words[0])

    def test_generate_many_words(self):
        word_len = 3
        generator = SequenceGenerator(abcAlphabet, word_len)
        words = list(generator.generate_words(20))
        generator.reset_seed()
        words2 = list(generator.generate_words(20))
        self.assertEqual(words, words2)

    def test_pad(self):
        word_len = 5
        generator = SequenceGenerator(abcAlphabet, word_len)
        sample_word = Sequence([SymbolChar('a'), SymbolChar('b'), SymbolChar('c')])
        padded_word = generator.pad(sample_word, SymbolChar('d'))
        target_word = Sequence([SymbolChar('a'), SymbolChar('b'), SymbolChar('c'),
                                SymbolChar('d'), SymbolChar('d')])

        self.assertEqual(padded_word, target_word)

    def test_generate_many_words_with_padding(self):
        word_len = 3
        generator = SequenceGenerator(abcAlphabet, word_len)
        words = list(generator.generate_words_with_padding(20, SymbolChar('d')))
        generator.reset_seed()
        words2 = list(generator.generate_words_with_padding(20, SymbolChar('d')))

        self.assertEqual(words, words2)

    def test_generate_all_words_up_to_a_length(self):
        generator = SequenceGenerator(abcAlphabet, 3)
        words = generator.generate_all_words_up_to_max_length()
        generator.reset_seed()
        words2 = generator.generate_all_words_up_to_max_length()
        total_words = 40

        self.assertEqual(words, words2)
        self.assertEqual(len(words), total_words)

    def test_generate_word_longer_than_max(self):
        generator = SequenceGenerator(abcAlphabet, max_seq_length=10)
        with self.assertRaises(AssertionError):
            generator.generate_word(length=11)

    def test_generate_words_with_min_and_max(self):
        maximum = 15
        minimum = 10
        generator = SequenceGenerator(abcAlphabet, max_seq_length=maximum, min_seq_length=minimum)
        lengths = np.array(list(map(len, generator.generate_words(20))))
        self.assertTrue(np.array([lengths >= minimum] and [lengths <= maximum]).all())
