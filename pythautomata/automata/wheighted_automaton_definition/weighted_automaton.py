import uuid
import math

import numpy as np

#from sequence_generators.sequence_generator import SequenceGenerator
from .weighted_state import WeightedState
from itertools import chain
from base_types.alphabet import Alphabet
from base_types.sequence import Sequence
from model_exporters.wfa_image_exporter import WFAImageExporter
from decimal import Decimal

from .wfa_queryable_model import WFAQueryableModel

epsilon = Sequence()


class WeightedAutomaton(WFAQueryableModel):

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value

    @property
    def terminal_symbol(self):
        return self._terminal_symbol

    @terminal_symbol.setter
    def terminal_symbol(self, value):
        self._terminal_symbol = value

    @property
    def alphabet(self):
        return self._alphabet

    @alphabet.setter
    def alphabet(self, value):
        self._alphabet = value

    def __init__(self, alphabet: Alphabet, weighted_states: set, terminal_symbol, name=None,
                 export_strategies=[WFAImageExporter()]):
        if name is None:
            self.name = 'WFA - ' + str(uuid.uuid4().hex)
        else:
            self.name = name
        self.terminal_symbol = Sequence() + terminal_symbol
        self.alphabet = alphabet
        self.weighted_states = weighted_states
        self.__exporting_strategies = export_strategies

    def is_deterministic(self):
        for weighted_state in self.weighted_states:
            for symbol in self.alphabet.symbols:
                transitions_for_symbol = weighted_state.transitions_dict_for(symbol)
                if len(transitions_for_symbol) > 1:
                    return False

        return True

    def sequence_weight(self, sequence: Sequence):
        return float(sum(map(lambda x: self._sequence_weight_from(sequence.value, x, x.initial_weight),
                             self.weighted_states)))

    def _sequence_weight_from(self, sequence_value, weighted_state: WeightedState, weight):
        if weight == 0:
            return Decimal(0)
        else:
            if sequence_value == ():
                return Decimal(weight)
            else:
                if sequence_value[0] == self.terminal_symbol[0]:
                    return Decimal(weight * weighted_state.final_weight)
                else:
                    transitions = weighted_state.transitions_list_for(sequence_value[0])
                    transitions_unzipped = list(zip(*transitions))
                    next_states = transitions_unzipped[0]
                    weights = transitions_unzipped[1]
                    return sum(map(lambda x, y: Decimal(weight) * self._sequence_weight_from(sequence_value[1:], x, y),
                                   next_states, weights))

    def log_sequence_weight(self, sequence: Sequence):
        return float(sum(filter(lambda x: x != float('inf'),
                                map(lambda x: self._log_sequence_weight_from(sequence.value, x, x.initial_weight),
                                    self.weighted_states))))

    def _log_sequence_weight_from(self, sequence_value, weighted_state: WeightedState, weight):
        if weight == 0:
            return float('inf')
        else:
            if sequence_value == ():
                return np.log(weight)
            else:
                if sequence_value[0] == self.terminal_symbol[0]:
                    return np.log(weight) + np.log(weighted_state.final_weight)
                else:
                    transitions = weighted_state.transitions_list_for(sequence_value[0])
                    transitions_unzipped = list(zip(*transitions))
                    next_states = transitions_unzipped[0]
                    weights = transitions_unzipped[1]
                    return sum(map(lambda x, y: np.log(weight) +
                                                self._log_sequence_weight_from(sequence_value[1:], x, y),
                                   next_states, weights))

    def last_token_weight(self, sequence: Sequence):
        return list(filter(self._is_positive, chain.from_iterable(
            map(lambda x: self._last_token_weight_from(sequence.value, x, x.initial_weight),
                self.weighted_states))))

    def _last_token_weight_from(self, sequence_value, state: WeightedState, weight):
        if weight == 0:
            return [0]
        else:
            if sequence_value == ():
                return [weight]
            else:
                if sequence_value[0] == self.terminal_symbol[0]:
                    return [state.final_weight]
                else:
                    transitions = state.transitions_list_for(sequence_value[0])
                    transitions_unzipped = list(zip(*transitions))
                    next_states = transitions_unzipped[0]
                    weights = transitions_unzipped[1]
                    return chain.from_iterable(map(lambda x, y: self._last_token_weight_from(sequence_value[1:], x, y),
                                                   next_states, weights))

    def get_last_token_weights(self, sequence, required_suffixes):
        weights = list()
        for suffix in required_suffixes:
            new_seq = sequence + suffix
            weight = self.last_token_weight(new_seq)
            if len(weight) > 0:
                weights.append(weight[0])
            else:
                weights.append(0)
        return weights

    def _is_positive(self, x):
        return x > 0

    def export(self, path):
        for strategy in self.__exporting_strategies:
            strategy.export(self, path)

    # Methods assuming PDFA (one initial state, one transition per state per symbol, prob dist for all transitions)
    # def get_representative_sample(self, sample_size):
    #     sample = list()
    #     for i in range(sample_size):
    #         sample.append(self.__get_representative_word())
    #     return sample
    #
    # def _get_representative_word(self):
    #     word = Sequence()
    #     first_state = list(filter(lambda x: x.initial_weight == 1, self.weighted_states))[0]
    #     symbols, weights, next_states = first_state.get_all_symbol_weights(self.terminal_symbol)
    #     next_symbol = numpy.random.choice(symbols, p=weights)
    #     while next_symbol != self.terminal_symbol:
    #         word += next_symbol
    #         i = symbols.index(next_symbol)
    #         next_state = next_states[i]
    #         symbols, weights, next_states = next_state.get_all_symbol_weights(self.terminal_symbol)
    #         next_symbol = numpy.random.choice(symbols, p=weights)
    #     return Sequence(word[:-1])

    #TODO: CHECK IF SEQUENCE GENERATOR IS REALLY NECESSARY
    # def get_representative_sample(self, sample_size):
    #     sample = list()
    #     sq = SequenceGenerator(self.alphabet, len(self.weighted_states) + 1)
    #     seqs = (sq.generate_all_words_up_to_max_length()),
    #     seqs2 = seqs[0]
    #     for seq in seqs2:
    #         seq2 = seq + self.terminal_symbol
    #         prob = self.sequence_weight(seq2)
    #         sample += [seq] * math.floor(sample_size * prob)
    #     return sample

    def __eq__(self, other):
        if not isinstance(other, WeightedAutomaton):
            return False
        if self.alphabet != other.alphabet:
            return False
        else:
            self_first_state = self.get_first_state()
            other_first_state = other.get_first_state()
            return self_first_state == other_first_state

    def get_first_state(self):
        for state in self.weighted_states:
            if state.initial_weight == 1:
                return state
