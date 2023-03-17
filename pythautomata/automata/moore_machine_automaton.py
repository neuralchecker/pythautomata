import sys
import uuid
from typing import Any
from pythautomata.abstract.finite_automaton import FiniteAutomaton

from pythautomata.abstract.model import Model
from pythautomata.base_types.moore_state import MooreState
from pythautomata.base_types.alphabet import Alphabet
from pythautomata.base_types.sequence import Sequence
from pythautomata.base_types.symbol import Symbol

from pythautomata.exceptions.unknown_symbols_exception import UnknownSymbolsException
from pythautomata.exceptions.non_deterministic_states_exception import NonDeterministicStatesException
from pythautomata.model_exporters.standard_exporters.moore_standard_dot_exporting_strategy import MooreStandardDotExportingStrategy
from pythautomata.model_exporters.dot_exporters.moore_dot_exporting_strategy import MooreDotExportingStrategy

class MooreMachineAutomaton(Model, FiniteAutomaton):
    """
    Implementation of Moore Machines.

    Attributes
    ----------
    states: set[MooreState]
        Set containing the Moore Machines states
    initial_state: State
        Initial state of the Moore Machine. Also included in "states"
    input_alphabet: Alphabet
        Set of Symbols that defines the Symbols that can be used as inputs
    output_alphabet: Alphabet
        Set of Symbols that defines the Symbols that can be used as output 

    Definition of Moore Machines is based on:
        Author, Georgios Giantamidis, Author, Stavros Tripakis (2016). 
            Learning Moore Machines from Input-Output Traces
    Link del artículo: https://arxiv.org/pdf/1605.07805.pdf
    """

    def __init__(self, input_alphabet: Alphabet, output_alphabet: Alphabet,
                 initial_state: MooreState, states: set[MooreState],
                 comparator, name: str = None,
                 exportingStrategies: list = [
                     MooreDotExportingStrategy(), MooreStandardDotExportingStrategy()],
                 hole: MooreState = MooreState('\u22A5')):

        self.states = states
        for state in self.states:
            self._verify_state(state, input_alphabet, output_alphabet)
            state.add_hole_transition(hole)

        self._name = 'Moore Machine - ' + \
            str(uuid.uuid4().hex) if name is None else name
        self._alphabet = input_alphabet
        self._output_alphabet = output_alphabet
        self.initial_state = initial_state
        self._set_hole(hole)
        self._exporting_strategies = exportingStrategies
        self._comparator = comparator
        self._actual_state = initial_state

    @property
    def name(self):
        return self._name

    @property
    def alphabet(self) -> Alphabet:
        return self._alphabet
    
    @property
    def output_alphabet(self) -> Alphabet:
        return self._output_alphabet

    def step(self, symbol):
        self._actual_state = self._actual_state.next_state_for(symbol)

        return self._actual_state.value

    def reset(self):
        self._actual_state = self.initial_state

    def last_symbol(self, sequence: Sequence) -> Symbol:
        actual_state = self.initial_state
        for symbol in sequence.value:
            actual_state = actual_state.next_state_for(symbol)
        return actual_state.value

    def process_query(self, sequence: Sequence) -> Symbol:
        return self.last_symbol(sequence)

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

    def __eq__(self, other: Any) -> bool:
        return isinstance(other, MooreMachineAutomaton) and self._comparator.are_equivalent(self, other)

    def export(self, path=None) -> None:
        for strategy in self._exporting_strategies:
            try:
                strategy.export(self, path)
            except:
                print("Unexpected exception when exporting " +
                      str(self._name) + ": " + str(sys.exc_info()[0]))

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
