import uuid
from typing import Any

from pythautomata.abstract.pdfa_model_exporting_strategy import PDFAModelExportingStrategy
from pythautomata.abstract.probabilistic_model import ProbabilisticModel
from pythautomata.automata.wheighted_automaton_definition.weighted_automaton import WeightedAutomaton
from pythautomata.automata.wheighted_automaton_definition.weighted_state import WeightedState
from pythautomata.base_types.alphabet import Alphabet
from pythautomata.base_types.sequence import Sequence
from pythautomata.base_types.symbol import Symbol, SymbolStr
from pythautomata.model_exporters.image_exporters.wfa_image_exporter import WFAImageExporter
from pythautomata.abstract.finite_automaton import FiniteAutomataComparator


def is_probabilistic(weighted_states: set[WeightedState], alphabet: Alphabet, max_error=0.3) -> bool:
    initial_states = list(
        filter(lambda state: state.initial_weight != 0, weighted_states))
    if len(initial_states) != 1:
        print('Assertion Error: len(initial_states) != 1')
        return False
    for weighted_state in weighted_states:
        total_weight = weighted_state.final_weight
        for symbol in alphabet.symbols:
            transitions_for_symbol = weighted_state.transitions_list[symbol]
            if len(transitions_for_symbol) > 1:
                print('Assertion Error:len(transitions_for_symbol) > 1')
                print('weighted_state:', weighted_state.name)
                return False
            total_weight += transitions_for_symbol[0][1]
        if abs(total_weight-1.0) > max_error:
            print('Assertion Error: abs(total_weight-1.0) > max_error')
            print('weighted_state:', weighted_state.name)
            print('total_weight:', total_weight)
            return False
    return True


class ProbabilisticDeterministicFiniteAutomaton(WeightedAutomaton, ProbabilisticModel):

    def __init__(self, alphabet: Alphabet, weighted_states: set, terminal_symbol: Symbol,
                 comparator: FiniteAutomataComparator,
                 name=None,
                 export_strategies: list[PDFAModelExportingStrategy] = None, check_is_probabilistic=True):
        if check_is_probabilistic:
            assert is_probabilistic(
                weighted_states, alphabet), "Trying to instantiate a non probabilisitic DFA"
        if export_strategies is None:
            export_strategies = [WFAImageExporter()]
        if name is None:
            name = 'PDFA - ' + str(uuid.uuid4().hex)
        super().__init__(alphabet, weighted_states,
                         terminal_symbol, comparator, name, export_strategies)

    def log_sequence_probability(self, sequence: Sequence) -> float:
        return self.log_sequence_weight(sequence)

    def last_token_probability(self, sequence: Sequence) -> float:
        return self.last_token_weight(sequence)[0]

    def sequence_probability(self, sequence: Sequence) -> float:
        return self.sequence_weight(sequence)

    def __eq__(self, other: Any) -> bool:
        return isinstance(other, ProbabilisticDeterministicFiniteAutomaton) and self._comparator.are_equivalent(self,
                                                                                                                other)

    def get_first_state(self):
        for state in self.weighted_states:
            if state.initial_weight == 1:
                return state

    def __getstate__(self):
        lines = f'Name\n{self.name}\n'
        lines += f'Terminal Symbol\n{self.terminal_symbol}\n'
        lines += 'Alphabet\n' + \
            ' '.join(
                map(lambda symbol: f'{str(symbol)}', self.alphabet.symbols)) + '\n'
        lines += ''.join(map(self.__encode_state, self.weighted_states))
        lines += ''.join(map(self.__encode_transitions_for_state,
                         self.weighted_states))
        return lines

    def __encode_state(self, state):
        return f'State\n{state.name} {state.initial_weight} {state.final_weight}\n'

    def __encode_transitions_for_state(self, state):
        if not state.transitions_list:
            return ''
        transitions_lines = ''.join(map(lambda x: self.__encode_transitions_for_state_symbol(state.name, x),
                                        state.transitions_list.items()))
        return transitions_lines

    def __encode_transitions_for_state_symbol(self, origin, transitions):
        symbol, transition_list = transitions
        transitions_lines = ''.join(map(lambda x: self.__encode_transition(origin, symbol, x),
                                        transition_list))
        return transitions_lines

    def __encode_transition(self, origin, symbol, transition):
        next_state, weight = transition
        return f'Transition\n{origin} {next_state.name} {symbol} {weight}\n'

    def __setstate__(self, state):
        elements = {'states': dict()}
        lines = str.split(str(state), '\n')[:-1]
        for i in range(0, len(lines), 2):
            self.decode(lines[i], lines[i + 1], elements)
        self._name = elements['name']
        self._alphabet = elements['alphabet']
        self._terminal_symbol = elements['terminal_symbol']
        self.weighted_states = set(elements['states'].values())

    def decode(self, key, value, acc):
        {'Name': lambda x: self.decode_name(value, x),
         'Terminal Symbol': lambda x: self.decode_terminal_symbol(value, x),
         'Alphabet': lambda x: self.decode_alphabet(value, x),
         'State': lambda x: self.decode_state(value, x),
         'Transition': lambda x: self.decode_transition(value, x)}[key](acc)

    def decode_name(self, value, acc):
        acc['name'] = value

    def decode_terminal_symbol(self, value, acc):
        acc['terminal_symbol'] = SymbolStr(value)

    def decode_alphabet(self, value, acc):
        symbols = value.split(' ')
        acc['alphabet'] = Alphabet(frozenset(map(SymbolStr, symbols)))

    def decode_state(self, value, acc):
        state_elements = value.split(' ')
        acc['states'][state_elements[0]] = (WeightedState(state_elements[0],
                                                          float(
                                                              state_elements[1]),
                                                          float(state_elements[2])))

    def decode_transition(self, value, acc):
        transition_elements = value.split(' ')
        acc['states'][transition_elements[0]].add_transition(SymbolStr(transition_elements[2]),
                                                             acc['states'][transition_elements[1]],
                                                             float(transition_elements[3]))
