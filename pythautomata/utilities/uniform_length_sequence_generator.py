from random import seed
from random import randint

from pythautomata.base_types.symbol import Symbol
from pythautomata.base_types.sequence import Sequence
from pythautomata.base_types.alphabet import Alphabet
from typing import List
from pythautomata.utilities.sequence_generator import SequenceGenerator


class UniformLengthSequenceGenerator(SequenceGenerator):

    def __init__(self, alphabet: Alphabet, max_seq_length: int, random_seed: int = 21, min_seq_length: int = 0):
        super().__init__(alphabet, max_seq_length, random_seed, min_seq_length)
    
    def generate_words(self, number_of_words: int):
        result = []
        for _ in range(number_of_words):
            length = randint(self._min_seq_length, self._max_seq_length)
            result.append(self.generate_single_word(length))
        return result

    def generate_single_word(self, length):
        if length > self._max_seq_length:
            raise AssertionError("Param length cannot exceed max_seq_length")

        value = []
        list_symbols = list(self._alphabet.symbols)
        list_symbols.sort()
        for _ in range(length):
            position = randint(0, len(list_symbols) - 1)
            symbol = list_symbols[position]
            value.append(symbol)
        return Sequence(value)

    