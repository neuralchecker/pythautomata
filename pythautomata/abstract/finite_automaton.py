from abc import ABC, abstractmethod
import sys
from collections import namedtuple
from typing import Any, Optional, Union

from pythautomata.base_types.alphabet import Alphabet
from pythautomata.base_types.sequence import Sequence
from pythautomata.base_types.symbol import SymbolStr
from pythautomata.base_types.state import State
from pythautomata.base_types.moore_state import MooreState
from pythautomata.base_types.mealy_state import MealyState

ExecutionState = namedtuple("ExecutionState", "state sequence")


class FiniteAutomaton(ABC):
    _alphabet: Alphabet
    _exporting_strategies: list

    def __init__(self, comparator: 'FiniteAutomataComparator', calculate_access_strings: bool = False):
        self._comparator = comparator
        if calculate_access_strings:
            self.calculate_access_strings()

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
    
    def calculate_access_strings(self):
        for state in self.states:
            state.access_string = self.get_access_string(state)

    def __eq__(self, other: Any) -> bool:
        return isinstance(other, FiniteAutomaton) and self._comparator.are_equivalent(self, other)
    
    def get_access_string(self, target: Union[State, MooreState, MealyState]) -> Sequence:
        initial_state = list(self.initial_states)[0]
        if target == initial_state:
            return Sequence([])
        
        explored_states = set()
        queue = [(initial_state, [])]

        while queue:
            actual_state, seq = queue.pop(0)
            if actual_state not in explored_states:
                neighbours = set()
                for symbol, next_states in actual_state.transitions.items():
                    seq_copy = seq.copy()
                    seq_copy.append(SymbolStr(symbol))
                    next_state = list(next_states)[0]
                    if next_state == target:
                        return Sequence(seq_copy)

                    if next_state not in neighbours:
                        neighbours.add(next_state)
                        queue.append((next_state, seq_copy))
                    
            explored_states.add(actual_state)

        return Sequence([])

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
