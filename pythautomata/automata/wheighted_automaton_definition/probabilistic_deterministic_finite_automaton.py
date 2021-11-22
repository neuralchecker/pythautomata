import uuid

from pythautomata.abstract.pdfa_model_exporting_strategy import PDFAModelExportingStrategy
from pythautomata.abstract.probabilistic_model import ProbabilisticModel
from pythautomata.automata.wheighted_automaton_definition.weighted_automaton import WeightedAutomaton
from pythautomata.automata.wheighted_automaton_definition.weighted_state import WeightedState
from pythautomata.base_types.alphabet import Alphabet
from pythautomata.base_types.sequence import Sequence
from pythautomata.base_types.symbol import Symbol
from pythautomata.model_exporters.wfa_image_exporter import WFAImageExporter


def is_probabilistic(weighted_states: set[WeightedState], alphabet: Alphabet) -> bool:
    initial_states = list(filter(lambda state: state.initial_weight != 0, weighted_states))
    if len(initial_states) != 1:
        return False
    for weighted_state in weighted_states:
        total_weight = weighted_state.final_weight
        for symbol in alphabet.symbols:
            transitions_for_symbol = weighted_state.transitions_list[symbol]
            if len(transitions_for_symbol) > 1:
                return False
            total_weight += transitions_for_symbol[0][1]
        if round(total_weight, 5) != 1:
            return False
    return True


class ProbabilisticDeterministicFiniteAutomaton(WeightedAutomaton, ProbabilisticModel):

    def __init__(self, alphabet: Alphabet, weighted_states: set, terminal_symbol: Symbol, name=None,
                 export_strategies: list[PDFAModelExportingStrategy] = None):
        assert is_probabilistic(weighted_states, alphabet)
        if export_strategies is None:
            export_strategies = [WFAImageExporter()]
        if name is None:
            name = 'PDFA - ' + str(uuid.uuid4().hex)
        super().__init__(alphabet, weighted_states, terminal_symbol, name, export_strategies)

    def log_sequence_probability(self, sequence: Sequence) -> float:
        return self.log_sequence_weight(sequence)

    def last_token_probability(self, sequence: Sequence) -> float:
        return self.last_token_weight(sequence)

    def last_token_probabilities(self, sequence: Sequence, required_suffixes: list[Sequence]) -> list[float]:
        return self.get_last_token_weights(sequence, required_suffixes)

    def sequence_probability(self, sequence: Sequence) -> float:
        return self.sequence_weight(sequence)

    def __eq__(self, other):
        if not isinstance(other, ProbabilisticDeterministicFiniteAutomaton):
            return False
        if self.alphabet != other.alphabet:
            return False
        else:
            self_first_state = self.get_first_state()
            other_first_state = other.get_first_state()
            return self_first_state == other_first_state

    def get_first_state(self):
        for state in self.weighted_states:
            if state.initial_weight == 1:
                return state
