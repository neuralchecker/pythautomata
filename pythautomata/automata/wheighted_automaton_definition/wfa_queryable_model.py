from abc import ABC, abstractmethod

from base_types.sequence import Sequence
from base_types.alphabet import Alphabet
from base_types.symbol import Symbol


class WFAQueryableModel(ABC):

    @property
    @abstractmethod
    def alphabet(self) -> Alphabet:
        raise NotImplementedError

    @property
    @abstractmethod
    def terminal_symbol(self) -> Symbol:
        raise NotImplementedError

    @property
    @abstractmethod
    def name(self):
        raise NotImplementedError

    @abstractmethod
    def sequence_weight(self, sequence: Sequence):
        raise NotImplementedError

    @abstractmethod
    def get_last_token_weights(self, sequence, required_suffixes):
        raise NotImplementedError

    @abstractmethod
    def log_sequence_weight(self, sequence):
        raise NotImplementedError
