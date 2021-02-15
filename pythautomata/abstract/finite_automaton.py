import uuid
from itertools import product
from collections import namedtuple, deque

from base_types.state import State
from base_types.alphabet import Alphabet
from base_types.sequence import Sequence

from typing import Any

from abstract.finite_automata_comparator import FiniteAutomataComparator as FAComparator
import sys


ExecutionState = namedtuple("ExecutionState", "state sequence")

from abc import ABC, abstractmethod, abstractproperty

#TODO: Define what to do with this class and add docstrings to this and/or subclases
class FiniteAutomaton(ABC):
    _alphabet: Alphabet
    _exporting_strategies: list

    def __init__(self, comparator: FAComparator):
        self._comparator = comparator

    @property
    def name(self) -> str:
        return self._name

    @name.setter
    def name(self, value: str) -> None:
        self._name = value

    @property
    def comparator(self) -> FAComparator:
        return self._comparator

    @comparator.setter
    def comparator(self, value: FAComparator):
        self._comparator = value

    @property
    def alphabet(self) -> Alphabet:
        return self._alphabet

    def find_first_difference_with(self, other: Any) -> Sequence:
        return self.comparator.get_counterexample_between(self, other)

    def __eq__(self, other: Any) -> bool:
        return isinstance(other, FiniteAutomaton) and self._comparator.are_equivalent(self, other)

    def export(self, path=None) -> None:
        for strategy in self._exporting_strategies:
            try:
                strategy.export(self, path)
            except:
                print("Unexpected excption when exporting " + str(self._name) + ": " + str(sys.exc_info()[0]))

