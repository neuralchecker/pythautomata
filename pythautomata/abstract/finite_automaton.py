from abc import ABC, abstractmethod
import sys
from collections import namedtuple
from typing import Any, Optional

from pythautomata.base_types.alphabet import Alphabet
from pythautomata.base_types.sequence import Sequence

ExecutionState = namedtuple("ExecutionState", "state sequence")


class FiniteAutomaton(ABC):
    _alphabet: Alphabet
    _exporting_strategies: list

    def __init__(self, comparator: 'FiniteAutomataComparator'):
        self._comparator = comparator

    @property
    def name(self) -> str:
        return self._name

    @name.setter
    def name(self, value: str) -> None:
        self._name = value

    @property
    def comparator(self) -> 'FiniteAutomataComparator':
        return self._comparator

    @comparator.setter
    def comparator(self, value: 'FiniteAutomataComparator'):
        self._comparator = value

    @property
    def alphabet(self) -> Alphabet:
        return self._alphabet

    @property
    def output_alphabet(self):
        return [True, False]

    @property
    @abstractmethod
    def hole(self):
        raise NotImplementedError

    @property
    @abstractmethod
    def initial_states(self) -> frozenset:
        raise NotImplementedError

    @property
    def has_full_alphabet(self) -> bool:
        """Whether or not the automaton has the complete alphabet or not. For example, symbolic automaton might not have the full alphabet if it works with intervals

        Returns:
            bool: True by defauult, should be overriden if you want a different result
        """
        return True

    def find_first_difference_with(self, other: Any) -> Optional[Sequence]:
        return self.comparator.get_counterexample_between(self, other)

    def __eq__(self, other: Any) -> bool:
        return isinstance(other, FiniteAutomaton) and self._comparator.are_equivalent(self, other)

    def export(self, path=None) -> None:
        for strategy in self._exporting_strategies:
            try:
                strategy.export(self, path)
            except:
                print("Unexpected exception when exporting " +
                      str(self._name) + ": " + str(sys.exc_info()[0]))


class FiniteAutomataComparator(ABC):

    @abstractmethod
    def are_equivalent(self, model1: 'FiniteAutomaton', model2: 'FiniteAutomaton') -> bool:
        # Returns true iif both models are equivalent (i.e. they recongize the same
        # set of symbol sequences).
        raise NotImplementedError

    @abstractmethod
    def get_counterexample_between(self, model1: 'FiniteAutomaton', model2: 'FiniteAutomaton') -> Optional[Sequence]:
        # Should return a counterexample sequence (one that is recognized by one and only
        # one of both models) if parameters are not equivalent, or None if they are
        raise NotImplementedError

    @abstractmethod
    def equivalent_output(self, observation1, observation2) -> bool:
        # Returns true iif both observations are equivalent (according to the comparator criteria).
        raise NotImplementedError
