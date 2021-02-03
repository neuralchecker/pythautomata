from collections import abc
from base_types.symbol import Symbol
from typing import Union
from exceptions.unexpected_type_exception import UnexpectedTypeException

class Sequence():

    def __init__(self, value:list=[]):
        if isinstance(value, abc.Sequence):
            self._value = list(value)
        else:
            self._value = [value]

    @property
    def value(self) -> list[Symbol]:
        return self._value

    def get_prefixes(self) -> set[Sequence]:
        result = set()
        for i in range(1, len(self.value) + 1):
            result.add(Sequence(self.value[:i]))
        return result

    def get_suffixes(self) -> set[Sequence]:
        result = set()
        for i in range(0, len(self.value)):
            result.add(Sequence(self.value[i:]))
        return result

    def append(self, symbol_to_append: Symbol):
        value = list(self.value)
        value.append(symbol_to_append)
        return Sequence(value)


    def __add__(self, other: Union[Sequence, Symbol]) -> Sequence:
        if isinstance(other, Sequence):
            return Sequence(self.value + other.value)
        if isinstance(other, Symbol):
            return Sequence(self.value + [other])
        raise UnexpectedTypeException()

    def __radd__(self, other: Union[Sequence, Symbol]) -> Sequence:
        if isinstance(other, Sequence):
            return Sequence(other.value + self.value)
        if isinstance(other, Symbol):
            return Sequence([other] + self.value)
        raise UnexpectedTypeException()

    def __repr__(self):
        return "ϵ" if self.value == () else "".join(map(lambda x: str(x), self.value))

    def __lt__(self, other: Sequence) -> bool:
        if len(self.value) == len(other.value):
            return self.__repr__() < other.__repr__()
        else:
            return len(self.value) < len(other.value)