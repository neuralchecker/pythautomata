from typing import Tuple

from pythautomata.base_types.guard import Guard
from pythautomata.base_types.symbol import Symbol
from pythautomata.exceptions.none_state_exception import NoneStateException


class SymbolicState:
    """Representation of SFA states.

        Attributes
        ----------
        name: str
            State name.
        is_final: bool
            Determines if the state is final.
        transitions: list[Tuple[Guard,SymbolicState]]
            A list containing guards associated with the next state
        hole:
            Hole state, state containing all transitions directed to itself. 
            It is used as default when a symbol is not present as transition key.
    """

    def __init__(self, name: str, is_final: bool = False):
        self.name = name
        self.is_final = is_final
        self.transitions: list[Tuple[Guard, SymbolicState]] = []

    @property
    def hole(self) -> 'SymbolicState':
        return self._hole

    def add_transition(self, guard: Guard, next_state: 'SymbolicState') -> None:
        """Adds a transition consisting of a guard and the next state

        Args:
            guard (Guard): A guard contains a predicate that receives a symbol
            next_state (SymbolicState): The state to go to when the guard is true

        Raises:
            NoneStateException: when next_state is None this exception is raised
        """
        if next_state is None:
            raise NoneStateException()
        self.transitions.append((guard, next_state))

    def next_state_for(self, symbol: Symbol) -> 'SymbolicState':
        for guard, state in self.transitions:
            if guard.matches(symbol):
                return state
        return self._hole

    def next_states_for(self, symbol: Symbol) -> list['SymbolicState']:
        return [self.next_state_for(symbol)]

    def add_hole_transition(self, hole: 'SymbolicState') -> None:
        self._hole = hole

    def __eq__(self, other):
        return isinstance(other, SymbolicState) and self.name == other.name

    def __hash__(self):
        return hash(self.name)

    def __str__(self):
        return repr(self)

    def __repr__(self):
        return str(self.name) + (" (Final)" if self.is_final else " (Non-final)")
