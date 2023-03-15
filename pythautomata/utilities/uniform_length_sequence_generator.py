import numpy as np
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

    def generate_word(self, length):
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

    def generate_all_words_up_to_max_length(self):
        ret = [Sequence([])]
        list_symbols = list(self._alphabet.symbols)
        list_symbols.sort()
        for counter in range(self._max_seq_length):
            ret_aux = ret.copy()
            for i in range(len(ret)):
                for symbol in list_symbols:
                    if len(ret[i].value) >= counter:
                        value = list(ret[i].value)
                        value.append(symbol)
                        extension = Sequence(value)
                        ret_aux.append(extension)
            ret = ret_aux
        return ret

    def generate_all_words(self):
        list_symbols = list(self._alphabet.symbols)
        list_symbols.sort()
        ret = [Sequence([])]
        while len(ret) > 0:
            result = ret.pop(0)
            yield result
            for symbol in list_symbols:
                value = list(result.value)
                value.append(symbol)
                extension = Sequence(value)
                ret.append(extension)
