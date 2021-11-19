import numpy

from pythautomata.base_types.sequence import Sequence


def get_representative_sample(self, sample_size):
    sample = list()
    for i in range(sample_size):
        sample.append(self.__get_representative_word())
    return sample


def _get_representative_word(self):
    word = Sequence()
    first_state = list(filter(lambda x: x.initial_weight == 1, self.weighted_states))[0]
    symbols, weights, next_states = first_state.get_all_symbol_weights(self.terminal_symbol)
    next_symbol = numpy.random.choice(symbols, p=weights)
    while next_symbol != self.terminal_symbol:
        word += next_symbol
        i = symbols.index(next_symbol)
        next_state = next_states[i]
        symbols, weights, next_states = next_state.get_all_symbol_weights(self.terminal_symbol)
        next_symbol = numpy.random.choice(symbols, p=weights)
    return word
