from pythautomata.base_types.symbol import Symbol
from pythautomata.exceptions.none_state_exception import NoneStateException


class MealyState:
    """Representation of Mealy machine states.

    Attributes
    ----------
    name: str
        State name.
    transitions: dict[Symbol, set['State']]
        For any given symbol represents the next state (or set of states in the case of NFA).
    outputs: dict[Symbol, Symbol]
        For any given symbol represents the output symbol.
    hole:
        Hole state, state containing all transitions directed to itself.
        It is used as default when a symbol is not present as transition key.
    """

    def __init__(self, name: str):
        self.name = name
        self.transitions: dict[Symbol, set('MealyState')] = {}
        self.outputs: dict[Symbol, Symbol] = {}
        self._is_deterministic: bool = True

    @property
    def is_deterministic(self) -> bool:
        return self._is_deterministic

    def add_transition(self, symbol: Symbol, next_state: 'MealyState', output: Symbol) -> None:
        if next_state is None:
            raise NoneStateException()
        if symbol not in self.transitions:
            self.transitions[symbol] = set()
        else:
            self._is_deterministic = False

        self.transitions[symbol].add(next_state)
        self.outputs[symbol] = output

    def next_states_for(self, symbol: Symbol) -> set['MealyState']:
        if symbol not in self.transitions:
            return set()
        return self.transitions[symbol]

    def next_state_for(self, symbol: Symbol) -> 'MealyState':
        next_states = list(self.next_states_for(symbol))
        assert (len(next_states) == 1)
        return next_states[0]

    def add_hole_transition(self, hole: 'MealyState') -> None:
        self.hole = hole

    def __eq__(self, other):
        return isinstance(other, MealyState) and self.name == other.name

    def __hash__(self):
        return hash(self.name)

    def __str__(self):
        return repr(self)

    def __repr__(self):
        return str(self.name)
