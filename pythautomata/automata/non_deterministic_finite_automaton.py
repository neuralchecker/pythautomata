import uuid
from base_types.state import State
from base_types.alphabet import Alphabet
from base_types.sequence import Sequence
from base_types.symbol import Symbol
from collections import deque, namedtuple
from abstract.finite_automaton import FiniteAutomaton
from model_exporters.encoded_file_exporting_strategy import EncodedFileExportingStrategy

ExecutionState = namedtuple("ExecutionState", ["state", "sequence"])

class NondeterministicFiniteAutomaton(FiniteAutomaton):
    def __init__(self, alphabet: Alphabet, initial_states: frozenset[State], states: set[State], name: str = None,
                 exportingStrategies: list = [EncodedFileExportingStrategy()], hole: State = State("Hole")):
        self.states = states
        for state in self.states:
            assert all(symbol in self.alphabet for symbol in state.transitions)
            state.add_hole_transition(hole)
        
        self._name = 'NFA - ' + str(uuid.uuid4().hex) if name is None else name
        self._alphabet = alphabet
        self.initial_states = initial_states
        self._set_hole(hole)
        self._exporting_strategies = exportingStrategies

    def accepts(self, sequence: Sequence) -> bool:
        toVisit = deque(ExecutionState(state, sequence) for state in self.initial_states)
        while toVisit:
            executionState = toVisit.pop()
            state = executionState.state
            value = executionState.sequence.value
            if value != ():
                suffix = Sequence(value[1:])
                for destination in state.next_states_for(value[0]):
                    if destination != self.hole:
                        toVisit.appendleft(ExecutionState(destination, suffix))
            elif state.is_final:
                return True
        return False

    def _setHole(self, hole: State) -> None:
        self.hole = hole
        #hole's hole is itself
        self.hole.add_hole_transition(self.hole)