from abc import ABC, abstractmethod
from typing import Union
from pythautomata.base_types.alphabet import Alphabet
from pythautomata.base_types.sequence import Sequence

class Model(ABC):

    @property
    @abstractmethod
    def name(self) -> str:
        raise NotImplementedError


    @property
    @abstractmethod
    def alphabet(self) -> Alphabet:
        raise NotImplementedError
    
    @property
    @abstractmethod
    def output_alphabet(self) -> Alphabet:
        raise NotImplementedError
    
    @abstractmethod
    def process_query(self, seq: Sequence) -> Union[Sequence, bool]:
        raise NotImplementedError