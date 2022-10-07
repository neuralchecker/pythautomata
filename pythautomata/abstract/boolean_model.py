from abc import ABC, abstractmethod

from pythautomata.base_types.alphabet import Alphabet
from pythautomata.base_types.sequence import Sequence


class BooleanModel(ABC):

    @property
    @abstractmethod
    def name(self) -> str:
        raise NotImplementedError
    
    @property
    @abstractmethod
    def alphabet(self) -> Alphabet:
        raise NotImplementedError

    @abstractmethod
    def accepts(self, sequence: Sequence) -> bool:
        raise NotImplementedError
