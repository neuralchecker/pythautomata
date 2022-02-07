from collections import abc
from pythautomata.base_types.symbol import Symbol
from typing import Union
from pythautomata.exceptions.unexpected_type_exception import UnexpectedTypeException


class Sequence():
    """Ordered collection of Symbols.
    """

    def __init__(self, value: list = []):
        if isinstance(value, abc.Sequence):
            self._value = list(value)
        else:
            self._value = [value]

    @property
    def value(self) -> list[Symbol]:
        return self._value

    def get_prefixes(self) -> list['Sequence']:
        result = list()
        for i in range(1, len(self.value) + 1):
            result.append(Sequence(self.value[:i]))
        return result

    def get_suffixes(self) -> list['Sequence']:
        result = list()
        for i in range(0, len(self.value)):
            result.append(Sequence(self.value[i:]))
        return result

    def append(self, symbol_to_append: Symbol):
        value = list(self.value)
        value.append(symbol_to_append)
        return Sequence(value)

    def __getitem__(self, key):
        return self.value[key]

    def __len__(self):
        return len(self.value)

    def __add__(self, other: Union['Sequence', Symbol]) -> 'Sequence':
        if isinstance(other, Sequence):
            return Sequence(self.value + other.value)
        if isinstance(other, Symbol):
            return Sequence(self.value + [other])
        raise UnexpectedTypeException()

    def __radd__(self, other: Union['Sequence', Symbol]) -> 'Sequence':
        if isinstance(other, Sequence):
            return Sequence(other.value + self.value)
        if isinstance(other, Symbol):
            return Sequence([other] + self.value)
        raise UnexpectedTypeException()

    def __repr__(self):
        return "ϵ" if self.value == () else "".join(map(lambda x: str(x), self.value))

    def __lt__(self, other: 'Sequence') -> bool:
        if len(self.value) == len(other.value):
            return self.__repr__() < other.__repr__()
        else:
            return len(self.value) < len(other.value)

    def __iter__(self):
        return self.value.__iter__()

    def __eq__(self, other: 'Sequence') -> bool:
        if isinstance(other, Sequence):
            return self.value == other.value
        return False

    def __hash__(self):
        result = 0
        i = 0
        for v in self._value:
            result += hash(v) * i
            i += 1
        return result
