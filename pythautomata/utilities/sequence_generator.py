import numpy as np
from random import seed
from random import randint

from pythautomata.base_types.symbol import Symbol
from pythautomata.base_types.sequence import Sequence
from pythautomata.base_types.alphabet import Alphabet
from typing import List
from abc import ABC, abstractmethod


class SequenceGenerator(ABC):

    def __init__(self, alphabet: Alphabet, max_seq_length: int, random_seed: int = 21, min_seq_length: int = 0):
        self._alphabet = alphabet
        self._min_seq_length = min_seq_length
        self._max_seq_length = max_seq_length
        self._seed = random_seed
        seed(self._seed)

    def reset_seed(self):
        seed(self._seed)

    @abstractmethod
    def generate_word(self, length):
        raise NotImplementedError

    def generate_words(self, number_of_words: int):
        result = np.empty(number_of_words, dtype=Sequence)
        for index in range(number_of_words):
            length = randint(self._min_seq_length, self._max_seq_length)
            result[index] = self.generate_word(length)
        return result

    def generate_words_with_padding(self, number_of_words: int, padding_symbol: Symbol):
        result = np.empty(number_of_words, dtype=Sequence)
        for index in range(number_of_words):
            length = randint(self._min_seq_length, self._max_seq_length)
            word = self.generate_word(length)
            result[index] = self.pad(word, padding_symbol)
        return result

    def pad(self, word: Sequence, padding_symbol: Symbol, max_len=None, padding_type='post'):
        if max_len is None:
            max_len = self._max_seq_length

        value = list(word.value)
        if len(value) > max_len:
            if padding_type == 'post':
                value = value[0:max_len]
            elif padding_type == 'pre':
                value = value[len(value) - max_len:len(value)]

        while len(value) < max_len:
            if padding_type == 'post':
                value.append(padding_symbol)
            elif padding_type == 'pre':
                value = [padding_symbol] + value
            else:
                raise Exception('Unknown padding type')
        return Sequence(value)

    def pad_sequences(self, words: List[Sequence], padding_symbol: Symbol, max_len=None, padding_type='post'):
        padded_sequences = list(map(lambda x: self.pad(
            x, padding_symbol, max_len, padding_type), words))
        return padded_sequences
