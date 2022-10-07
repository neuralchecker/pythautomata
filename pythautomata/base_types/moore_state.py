from pythautomata.base_types.symbol import Symbol
from pythautomata.exceptions.none_state_exception import NoneStateException

class MooreState:
    """Representation of Moore machine states.

    Attributes
    ----------
    name: str
        State name.
    value: Symbol
        Is an element of an alphabet associated with the state.
    transitions: dict[Symbol, set['State']]
        For any given symbol represents the next state (or set of states in the case of NFA).
    hole:
        Hole state, state containing all transitions directed to itself. 
        It is used as default when a symbol is not present as transition key.
    """

    def __init__(self, name: str, value: Symbol = ""):
        self.name = name
        self.value = value
        self.transitions: dict[Symbol, set['MooreState']] = {}
        self._is_deterministic: bool = True

    @property
    def is_deterministic(self) -> bool:
        return self._is_deterministic

    def add_transition(self, symbol: Symbol, next_state: 'MooreState') -> None:
        if next_state is None:
            raise NoneStateException()
        if symbol not in self.transitions:
            self.transitions[symbol] = set()
        else:
            self._is_deterministic = False
        self.transitions[symbol].add(next_state)

    def add_multiple_transitions(self, symbol: Symbol, next_states: list['MooreState']) -> None:
        for next_state in next_states:
            self.add_transition(symbol, next_state)

    def next_states_for(self, symbol: Symbol) -> set['MooreState']:
        if symbol not in self.transitions:
            return {self.hole}
        return self.transitions[symbol]

    def next_state_for(self, symbol: Symbol) -> 'MooreState':
        next_states = list(self.next_states_for(symbol))
        assert(len(next_states) == 1)
        return next_states[0]

    def add_hole_transition(self, hole: 'MooreState') -> None:
        self.hole = hole

    def __eq__(self, other):
        return isinstance(other, MooreState) and self.name == other.name

    def __hash__(self):
        return hash(self.name)

    def __str__(self):
        return repr(self)

    def __repr__(self):
        return str(self.name) + " : " + str(self.value)