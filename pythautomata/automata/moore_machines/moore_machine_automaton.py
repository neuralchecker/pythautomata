from genericpath import exists
import uuid
from pythautomata.abstract.boolean_model import BooleanModel

from .moore_state import MooreState

from pythautomata.base_types.alphabet import Alphabet
from pythautomata.base_types.sequence import Sequence
from pythautomata.base_types.symbol import Symbol

from pythautomata.abstract.finite_automaton import FiniteAutomaton, FiniteAutomataComparator
from pythautomata.exceptions.unknown_symbols_exception import UnknownSymbolsException
from pythautomata.exceptions.non_deterministic_states_exception import NonDeterministicStatesException
from pythautomata.model_exporters.encoded_file_exporting_strategy import EncodedFileExportingStrategy

class MooreMachineAutomaton(FiniteAutomaton):

    def __init__(self, input_alphabet: Alphabet, output_alphabet: Alphabet, initial_state: MooreState, states: set[MooreState],
                 comparator: FiniteAutomataComparator, name: str = None,
                 exportingStrategies: list = [EncodedFileExportingStrategy()], hole: MooreState = MooreState("Hole")):
        
        self.states = states
        for state in self.states:
            self._verify_state(state, input_alphabet, output_alphabet)
            state.add_hole_transition(hole)

        self._name = 'Moore Machine - ' + str(uuid.uuid4().hex) if name is None else name
        self._alphabet = input_alphabet
        self._outputAlphabet = output_alphabet
        self.initial_state = initial_state
        self._set_hole(hole)
        self._exporting_strategies = exportingStrategies
        super(MooreMachineAutomaton, self).__init__(comparator)

    def last_symbol(self, sequence: Sequence) -> Symbol: 
        actual_state = self.initial_state
        for symbol in sequence.value:
            actual_state = actual_state.next_state_for(symbol)
        return actual_state.value

    def transduce(self, sequence: Sequence) -> Sequence:
        actual_state = self.initial_state
        output = Sequence()
        output.append(actual_state.value)
        for symbol in sequence.value:
            actual_state = actual_state.next_state_for(symbol)
            output.append(actual_state.value)
        return output

    @property
    def initial_states(self) -> frozenset:
        return frozenset([self.initial_state])

    @property
    def hole(self):
        return self._hole

    def _set_hole(self, hole: MooreState) -> None:
        self._hole = hole
        # hole's hole state is itself
        self._hole.add_hole_transition(self.hole)
    
    def _verify_state(self, state: MooreState, alphabet: Alphabet, outputAlphabet: Alphabet) -> None:
        self._verify_symbols_in_output_alphabet(state, outputAlphabet)
        self._verify_transition_symbols_in_alphabet(
            state.transitions, alphabet)
        self._verify_state_is_deterministic(state)

    def _verify_transition_symbols_in_alphabet(self, transitions: dict[Symbol, set['MooreState']], alphabet: Alphabet) -> \
            None:
        if not all(symbol in alphabet for symbol in transitions):
            raise UnknownSymbolsException()
    
    def _verify_symbols_in_output_alphabet(self, state: MooreState, outputAlphabet: Alphabet) -> \
            None:
        if not state.value in outputAlphabet:
            raise UnknownSymbolsException()

    def _verify_state_is_deterministic(self, state: MooreState) -> None:
        if not state.is_deterministic:
            raise NonDeterministicStatesException()
