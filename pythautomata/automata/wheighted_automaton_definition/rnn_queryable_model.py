import uuid

from base_types.sequence import Sequence
from neural_networks.rnn_language_models.last_token_language_model import LastTokenLanguageModel
from queryable_models.wheighted_automaton_definition.wfa_queryable_model import WFAQueryableModel


class WFARNNQueryable(WFAQueryableModel):

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value

    @property
    def alphabet(self):
        return self.__language_model.alphabet

    @property
    def terminal_symbol(self):
        return self._terminal_symbol

    @terminal_symbol.setter
    def terminal_symbol(self, value):
        self._terminal_symbol = value

    def __init__(self, language_model: LastTokenLanguageModel, name=None):
        if name is None:
            self.name = 'RNN - ' + str(uuid.uuid4().hex)
        else:
            self.name = name
        self.__language_model = language_model
        self.terminal_symbol = Sequence() + language_model.terminal_symbol

    def sequence_weight(self, sequence):
        return self.__language_model.sequence_probability(sequence)[0]

    def log_sequence_weight(self, sequence):
        return self.__language_model.sequence_probability(sequence)[1]

    def get_last_token_weights(self, sequence, required_suffixes):
        weights = list()
        alphabet_symbols_weights = self.__language_model.next_symbol_probas(sequence)
        alphabet_symbols_weights = {Sequence() + k: alphabet_symbols_weights[k] for k in alphabet_symbols_weights.keys()}
        for suffix in required_suffixes:
            if suffix in alphabet_symbols_weights:
                weights.append(alphabet_symbols_weights[suffix])
            else:
                new_sequence = sequence + suffix
                new_prefix = Sequence(new_sequence[:-1])
                new_suffix = new_sequence[-1]
                next_symbol_weights = self.__language_model.next_symbol_probas(new_prefix)
                weights.append(next_symbol_weights[new_suffix])
        return weights

