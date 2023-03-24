import numpy as np
import random
import math

from pythautomata.base_types.symbol import Symbol
from pythautomata.base_types.sequence import Sequence
from pythautomata.base_types.alphabet import Alphabet
from typing import List
from pythautomata.utilities.sequence_generator import SequenceGenerator


class UniformWordSequenceGenerator(SequenceGenerator):

    def __init__(self, alphabet: Alphabet, max_seq_length: int, random_seed: int = 21, min_seq_length: int = 0):
        super().__init__(alphabet, max_seq_length, random_seed, min_seq_length)
        self._probs = {x:self._prob_by_word_length(x) for x in range(min_seq_length, max_seq_length)}
    
    def generate_words(self, number_of_words: int):
        result = np.empty(number_of_words, dtype=Sequence)
        for index in range(number_of_words):
            length = self._select_random_length()
            result[index] = self.generate_single_word(length)
        return result

    def generate_single_word(self, length):
        if length > self._max_seq_length:
            raise AssertionError("Param length cannot exceed max_seq_length")
        if length < self._min_seq_length:
            raise AssertionError("Param length cannot be less than max_seq_length")

        value = []
        list_symbols = list(self._alphabet.symbols)
        list_symbols.sort()
        for _ in range(length):
            position = random.randint(0, len(list_symbols) - 1)
            symbol = list_symbols[position]
            value.append(symbol)
        return Sequence(value)

    def _prob_by_word_length(self, length):
        s = len(self._alphabet)
        n = self._max_seq_length
        m = self._min_seq_length

        si = math.pow(s,length)
        sn_plus_1 = math.pow(s,n+1)
        sm = math.pow(s, m)

        proba = si*(s-1)/(sn_plus_1-sm)
        return proba

    def _select_random_length(self):
        length = random.choices(list(self._probs.keys()), weights = self._probs.values(),k=1)[0]
        return length

    