from pythautomata.abstract.boolean_model import BooleanModel
from pythautomata.abstract.finite_automaton import FiniteAutomataComparator, FiniteAutomaton
from pythautomata.abstract.model_exporting_strategy import ModelExportingStrategy
from pythautomata.base_types.symbolic_state import SymbolicState
from pythautomata.base_types.sequence import Sequence
from pythautomata.base_types.alphabet import Alphabet
import uuid

from pythautomata.model_comparators.hopcroft_karp_comparison_strategy import HopcroftKarpComparisonStrategy


class SymbolicFiniteAutomaton(FiniteAutomaton, BooleanModel):
    """Implementation of a Symbolic Automaton

    Attributes
    ----------
    states: set[State]
        Set containing the SFA's states
    initial_state: State
        Initial state of the SFA. Also included in "states"
    """

    def __init__(self, alphabet: Alphabet, initial_state: SymbolicState, states: set[SymbolicState], name: str = None,
                 exportingStrategies: list[ModelExportingStrategy] = [], hole: SymbolicState = SymbolicState("Hole"),
                 comparator: FiniteAutomataComparator = HopcroftKarpComparisonStrategy()):
        self._name = 'DFA - ' + str(uuid.uuid4().hex) if name is None else name
        self._alphabet = alphabet
        self.initial_state = initial_state
        self.states = states
        self._set_hole(hole)
        self._exporting_strategies = exportingStrategies

    def _set_hole(self, hole: SymbolicState) -> None:
        self._hole = hole
        # hole's hole state is itself
        self._hole.add_hole_transition(self.hole)
        for state in self.states:
            state.add_hole_transition(hole)

    @property
    def hole(self):
        return self._hole

    @property
    def initial_states(self) -> frozenset:
        return frozenset([self.initial_state])

    def accepts(self, sequence: Sequence) -> bool:
        actual_state = self.initial_state
        for symbol in sequence:
            actual_state = actual_state.next_state_for(symbol)
        return actual_state.is_final

    @property
    def has_full_alphabet(self) -> bool:
        return False
