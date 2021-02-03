import uuid
from itertools import product
from collections import namedtuple, deque

from base_types.state import State
from base_types.alphabet import Alphabet
from base_types.sequence import Sequence

from typing import Any

import utilities.automata_comparator as AutomataComparator
import sys


ExecutionState = namedtuple("ExecutionState", "state sequence")

from abc import ABC, abstractmethod, abstractproperty

class FiniteAutomaton(ABC):
    _alphabet: Alphabet
    _exporting_strategies: list

    @property
    def name(self) -> str:
        return self._name

    @name.setter
    def name(self, value: str) -> None:
        self._name = value

    @property
    def alphabet(self) -> Alphabet:
        return self._alphabet

    def find_first_difference_with(self, other: Any) -> Sequence:
        return AutomataComparator.get_counterexample_between(self, other)

    def __eq__(self, other: Any) -> bool:
        return isinstance(other, FiniteAutomaton) and AutomataComparator.are_equivalent(self, other)

    def export(self, path=None) -> None:
        for strategy in self._exporting_strategies:
            try:
                strategy.export(self, path)
            except:
                print("Unexpected excption when exporting " + str(self._name) + ": " + str(sys.exc_info()[0]))

