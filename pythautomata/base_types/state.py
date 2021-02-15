from base_types.symbol import Symbol
from exceptions.none_state_exception import NoneStateException

class State:
    """Representation of NFA or DFA states.

    Attributes
    ----------
    name: str
        State name.
    is_final: bool
        Determines if the state is final.
    transitions: dict[Symbol, set['State']]
        For any given symbol represents the next state (or set of states in the case of NFA).
    hole:
        Hole state, state containing all transitions directed to itself. 
        It is used as default when a symbol is not present as transition key.
    """
    
    hole: 'State'

    def __init__(self, name: str, is_final: bool = False):
        self.name = name
        self.is_final = is_final
        self.transitions: dict[Symbol, set['State']] = {}
        self._is_deterministic: bool = True

    @property
    def is_deterministic(self) -> bool:
        return self._is_deterministic

    def add_transition(self, symbol: Symbol, next_state: 'State') -> None:
        if next_state is None:
            raise NoneStateException()
        if symbol not in self.transitions:
            self.transitions[symbol] = set()
        else:
            self._is_deterministic = False
        self.transitions[symbol].add(next_state)

    def add_multiple_transitions(self, symbol: Symbol, next_states: list['State']) -> None:
        for next_state in next_states:
            self.add_transition(symbol, next_state)

    def next_states_for(self, symbol: Symbol) -> set['State']:
        if symbol not in self.transitions:
            return {self.hole}
        return self.transitions[symbol]

    def next_state_for(self, symbol: Symbol) -> 'State':
        next_states = list(self.next_states_for(symbol))
        assert(len(next_states) == 1)
        return next_states[0]

    def add_hole_transition(self, hole: 'State') -> None:
        self.hole = hole

    def __eq__(self, other):
        return isinstance(other, State) and self.name == other.name

    def __hash__(self):
        return hash(self.name)

    def __str__(self):
        return repr(self)

    def __repr__(self):
        return str(self.name) + (" (Final)" if self.is_final else " (Non-final)")
