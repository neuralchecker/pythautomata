import sys
import uuid

from pythautomata.abstract.model import Model
from pythautomata.abstract.finite_automaton import FiniteAutomaton
from pythautomata.base_types.alphabet import Alphabet
from pythautomata.base_types.mealy_state import MealyState
from pythautomata.base_types.sequence import Sequence
from pythautomata.base_types.symbol import Symbol
from pythautomata.exceptions.non_deterministic_states_exception import NonDeterministicStatesException
from pythautomata.exceptions.unknown_symbols_exception import UnknownSymbolsException
from pythautomata.model_exporters.standard_exporters.mealy_standard_dot_exporting_strategy import MealyStandardDotExportingStrategy

class MealyMachine(Model, FiniteAutomaton):
    """
    Implementation of Mealy Machines.

    Attributes
    ----------
    states: set[MealyState]
        Set of states of the machine.
    initial_state: MealyState
        Initial state of the machine. Also included in "states".
    input_alphabet: Alphabet
        Set of Symbols that defines the Symbols that can be used as inputs.
    output_alphabet: Alphabet
        Set of Symbols that defines the Symbols that can be used as output.
    name: str
        Name of the machine.
    exporting_strategies: list
        List of exporting strategies that can be used to export the machine.
    """

    def __init__(self, input_alphabet: Alphabet, output_alphabet: Alphabet,
                 initial_state: MealyState, states: set[MealyState], comparator,
                 name: str = None, exporting_strategies: list = [MealyStandardDotExportingStrategy()],
                 hole: MealyState = MealyState("\u22A5")):
        self.states = states
        for state in self.states:
            self._verify_state(state, input_alphabet, output_alphabet)
            state.add_hole_transition(hole)

        self._name = ("Mealy Machine - " + str(uuid.uuid4().hex)
                      if name is None else name)
        self._alphabet = input_alphabet
        self._output_alphabet = output_alphabet
        self.initial_state = initial_state
        self._set_hole(hole)
        self._exporting_strategies = exporting_strategies
        self._comparator = comparator
        self._actual_state = initial_state

    @property
    def initial_states(self) -> frozenset:
        return frozenset([self.initial_state])

    @property
    def hole(self):
        return self._hole
    
    @property
    def name(self) -> Alphabet:
        return self._name

    @property
    def alphabet(self) -> Alphabet:
        return self._alphabet

    @property
    def output_alphabet(self) -> Alphabet:
        return self._output_alphabet

    def __eq__(self, other):
        return isinstance(other, MealyMachine) and self._comparator.are_equivalent(self, other)

    def step(self, symbol):
        output = self._actual_state.outputs[symbol]
        self._actual_state = self._actual_state.next_state_for(symbol)

        return output

    def reset(self):
        self._actual_state = self.initial_state

    def last_symbol(self, sequence: Sequence) -> Symbol:
        actual_state = self.initial_state
        output = Symbol()
        for symbol in sequence.value:
            output = actual_state.outputs[symbol]
            actual_state = actual_state.next_state_for(symbol)
        return output

    def process_query(self, sequence: Sequence) -> Symbol:
        return self.last_symbol(sequence)

    def transduce(self, sequence: Sequence) -> Sequence:
        actual_state = self.initial_state
        output = Sequence()
        for symbol in sequence.value:
            output.append(actual_state.outputs[symbol])
            actual_state = actual_state.next_state_for(symbol)
        return output

    def export(self, path=None):
        for strategy in self._exporting_strategies:
            try:
                strategy.export(self, path)
            except:
                print("Unexpected exception when exporting " +
                      str(self._name) + ": " + str(sys.exc_info()[0]))

    def _set_hole(self, hole: MealyState) -> None:
        self._hole = hole
        self.hole.add_hole_transition(hole)

    def _verify_state(self, state: MealyState, input_alphabet: Alphabet,
                      output_alphabet: Alphabet) -> None:
        self.verify_transitions(state, input_alphabet)
        self.verify_output(state, output_alphabet)
        self.verify_state_is_deterministic(state)

    def verify_transitions(self, state: MealyState, input_alphabet: Alphabet):
        for symbol in state.transitions:
            if symbol not in input_alphabet:
                raise UnknownSymbolsException()

    def verify_output(self, state: MealyState, output_alphabet: Alphabet):
        for _, symbol in state.outputs.items():
            if symbol not in output_alphabet:
                raise UnknownSymbolsException()

    def verify_state_is_deterministic(self, state: MealyState):
        if not state.is_deterministic:
            raise NonDeterministicStatesException()
