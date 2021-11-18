from abc import ABC, abstractmethod

from pythautomata.base_types.alphabet import Alphabet
from pythautomata.base_types.sequence import Sequence
from pythautomata.base_types.symbol import Symbol


class ProbabilisticModel(ABC):

    @property
    @abstractmethod
    def name(self) -> str:
        raise NotImplementedError

    @property
    @abstractmethod
    def terminal_symbol(self) -> Symbol:
        raise NotImplementedError

    @property
    @abstractmethod
    def alphabet(self) -> Alphabet:
        raise NotImplementedError

    @abstractmethod
    def sequence_probability(self, sequence: Sequence) -> float:
        raise NotImplementedError

    @abstractmethod
    def log_sequence_probability(self, sequence: Sequence) -> float:
        raise NotImplementedError

    @abstractmethod
    def last_token_probability(self, sequence: Sequence) -> float:
        raise NotImplementedError

    @abstractmethod
    def last_token_probabilities(self, sequence: Sequence, required_suffixes: list[Sequence]) -> list[float]:
        raise NotImplementedError
