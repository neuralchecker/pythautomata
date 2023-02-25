import uuid
from pythautomata.abstract.boolean_model import BooleanModel

from pythautomata.base_types.state import State
from pythautomata.base_types.alphabet import Alphabet
from pythautomata.base_types.sequence import Sequence
from pythautomata.base_types.symbol import Symbol
from pythautomata.abstract.finite_automaton import (
    FiniteAutomaton,
    FiniteAutomataComparator,
)
from pythautomata.exceptions.unknown_symbols_exception import UnknownSymbolsException
from pythautomata.exceptions.non_deterministic_states_exception import (
    NonDeterministicStatesException,
)
from pythautomata.model_exporters.encoded_file_exporting_strategy import (
    EncodedFileExportingStrategy,
)
from pythautomata.model_exporters.encoded_string_exporting_strategy import (
    EncodedStringExportingStrategy,
)
from pythautomata.utilities.encoded_string_importer import EncodedStringImporter
from pythautomata.utilities.encoded_file_importer import EncodedFileImporter


class DeterministicFiniteAutomaton(FiniteAutomaton, BooleanModel):
    """
    Implementation of DFA.

    Attributes
    ----------
    states: set[State]
        Set containing the DFA's states
    initial_state: State
        Initial state of the DFA. Also included in "states"
    """

    def __init__(
        self,
        alphabet: Alphabet,
        initial_state: State,
        states: set[State],
        comparator: FiniteAutomataComparator,
        name: str = None,
        exportingStrategies: list = [EncodedFileExportingStrategy()],
        hole: State = State("Hole"),
    ):
        self.states = states
        for state in self.states:
            self._verify_state(state, alphabet)
            state.add_hole_transition(hole)

        self._name = "DFA - " + str(uuid.uuid4().hex) if name is None else name
        self._alphabet = alphabet
        self.initial_state = initial_state
        self._set_hole(hole)
        self._exporting_strategies = exportingStrategies
        self._actual_state = self.initial_state
        super(DeterministicFiniteAutomaton, self).__init__(comparator)

    def accepts(self, sequence: Sequence) -> bool:
        actual_state = self.initial_state
        for symbol in sequence.value:
            actual_state = actual_state.next_state_for(symbol)
        return actual_state.is_final

    def process_query(self, sequence: Sequence) -> bool:
        return self.accepts(sequence)

    @property
    def initial_states(self) -> frozenset:
        return frozenset([self.initial_state])

    @property
    def hole(self):
        return self._hole

    def step(self, symbol):
        self._actual_state = self._actual_state.next_state_for(symbol)
        return self._actual_state.is_final

    def reset(self):
        self._actual_state = self.initial_state

    def clone(self) -> "DeterministicFiniteAutomaton":
        return DeterministicFiniteAutomaton(
            self.alphabet, self.initial_state, self.states, self.comparator, self.name
        )

    def _set_hole(self, hole: State) -> None:
        self._hole = hole
        # hole's hole state is itself
        self._hole.add_hole_transition(self.hole)

    def _verify_state(self, state: State, alphabet: Alphabet) -> None:
        self._verify_transition_symbols_in_alphabet(
            state.transitions, alphabet)
        self._verify_state_is_deterministic(state)

    def _verify_transition_symbols_in_alphabet(
        self, transitions: dict[Symbol, set["State"]], alphabet: Alphabet
    ) -> None:
        if not all(symbol in alphabet for symbol in transitions):
            raise UnknownSymbolsException()

    def _verify_state_is_deterministic(self, state: State) -> None:
        if not state.is_deterministic:
            raise NonDeterministicStatesException()

    def __getstate__(self):
        # dump a string
        lines = EncodedStringExportingStrategy().export(self)
        return lines

    def __setstate__(self, state):
        attrs = EncodedStringImporter().import_automata_attributes(str(state))
        alphabet, initialStates, states, modelName = attrs
        self.name = modelName
        self._alphabet = alphabet
        self.initial_state = list(initialStates)[0]
        self.states = states
        hole = State("Hole")
        self._set_hole(hole)
        for state in self.states:
            assert all(
                symbol in self.alphabet for symbol in state.transitions.keys())
            state.add_hole_transition(self.hole)
        self._queryable_self = self
