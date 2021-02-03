import uuid
from base_types.state import State
from base_types.alphabet import Alphabet
from base_types.sequence import Sequence
from base_types.symbol import Symbol
from abstract.finite_automaton import FiniteAutomaton
from exceptions.unknown_symbols_exception import UnknownSymbolsException
from exceptions.non_deterministic_states_exception import NonDeterministicStatesException
from model_exporters.encoded_file_exporting_strategy import EncodedFileExportingStrategy

class DeterministicFiniteAutomaton(FiniteAutomaton):
    def __init__(self, alphabet: Alphabet, initial_states: frozenset[State], states: set[State], name: str = None,
                 exportingStrategies: list = [EncodedFileExportingStrategy()], hole: State = State("Hole")):
        self.states = states
        for state in self.states:
            self.veirfy_state(state, alphabet)
            state.add_hole_transition(hole)

        self._name = 'DFA - ' + str(uuid.uuid4().hex) if name is None else name
        self._alphabet = alphabet
        self.initial_states = initial_states
        self._setHole(hole)
        self._exporting_strategies = exportingStrategies

    def accepts(self, sequence: Sequence) -> bool:
        actual_state: State
        for actual_state in self.initial_states:
            for symbol in sequence.value:
                actual_state = actual_state.next_state_for(symbol)
                if actual_state.is_final:
                    return True
        return False

    def _setHole(self, hole: State) -> None:
        self.hole = hole
        # hole's hole state is itself
        self.hole.add_hole_transition(self.hole)

    def _veirify_state(self, state: State, alphabet: Alphabet) -> None:
        self.verify_transition_symbols_in_alphabet(state.transitions, alphabet)
        self.verify_state_is_deterministic(state)

    def _verify_transition_symbols_in_alphabet(self, transitions: set[Symbol], alphabet: Alphabet) -> None:
        if not all(symbol in alphabet for symbol in transitions):
            raise UnknownSymbolsException()

    def _verify_state_is_deterministic(self, state: State) -> None:
        if not state.is_deterministic:
            raise NonDeterministicStatesException()