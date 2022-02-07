import uuid
import numpy as np

from pythautomata.automata.wheighted_automaton_definition.weighted_state import WeightedState
from itertools import chain
from pythautomata.base_types.alphabet import Alphabet
from pythautomata.base_types.sequence import Sequence
from decimal import Decimal

from pythautomata.abstract.pdfa_model_exporting_strategy import PDFAModelExportingStrategy
from pythautomata.model_exporters.wfa_image_exporter import WFAImageExporter
from pythautomata.base_types.symbol import Symbol
from pythautomata.abstract.finite_automaton import FiniteAutomataComparator, FiniteAutomaton
from typing import Any

epsilon = Sequence()


class WeightedAutomaton(FiniteAutomaton):

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value

    @property
    def terminal_symbol(self):
        return self._terminal_symbol

    @terminal_symbol.setter
    def terminal_symbol(self, value):
        self._terminal_symbol = value

    @property
    def alphabet(self):
        return self._alphabet

    @alphabet.setter
    def alphabet(self, value):
        self._alphabet = value

    def __init__(self, alphabet: Alphabet, weighted_states: set, terminal_symbol: Symbol, comparator: FiniteAutomataComparator, name=None,
                 export_strategies: list[PDFAModelExportingStrategy] = None):
        if export_strategies is None:
            export_strategies = [WFAImageExporter()]
        if name is None:
            self.name = 'WFA - ' + str(uuid.uuid4().hex)
        else:
            self._name = name
        self._terminal_symbol = terminal_symbol
        self._alphabet = alphabet
        self.weighted_states = weighted_states
        self._comparator = comparator
        self.__exporting_strategies = export_strategies

    @property
    def hole(self):
        return None

    @property
    def initial_states(self) -> frozenset:
        initial_states = list(
            filter(lambda state: state.initial_weight != 0, self.weighted_states))
        return frozenset(initial_states)

    def sequence_weight(self, sequence: Sequence):
        return float(sum(map(lambda x: self._sequence_weight_from(sequence.value, x, x.initial_weight),
                             self.weighted_states)))

    def _sequence_weight_from(self, sequence_value, weighted_state: WeightedState, weight):
        if weight == 0:
            return Decimal(0)
        else:
            if not sequence_value:
                return Decimal(weight)
            else:
                if sequence_value[0] == self.terminal_symbol:
                    return Decimal(weight * weighted_state.final_weight)
                else:
                    transitions = weighted_state.transitions_list_for(
                        sequence_value[0])
                    transitions_unzipped = list(zip(*transitions))
                    next_states = transitions_unzipped[0]
                    weights = transitions_unzipped[1]
                    return sum(map(lambda x, y: Decimal(weight) * self._sequence_weight_from(sequence_value[1:], x, y),
                                   next_states, weights))

    def log_sequence_weight(self, sequence: Sequence):
        return float(sum(filter(lambda x: x != float('inf'),
                                map(lambda x: self._log_sequence_weight_from(sequence.value, x, x.initial_weight),
                                    self.weighted_states))))

    def _log_sequence_weight_from(self, sequence_value, weighted_state: WeightedState, weight):
        if weight == 0:
            return float('inf')
        else:
            if not sequence_value:
                return np.log(weight)
            else:
                if sequence_value[0] == self.terminal_symbol:
                    return np.log(weight) + np.log(weighted_state.final_weight)
                else:
                    transitions = weighted_state.transitions_list_for(
                        sequence_value[0])
                    transitions_unzipped = list(zip(*transitions))
                    next_states = transitions_unzipped[0]
                    weights = transitions_unzipped[1]
                    return sum(map(lambda x, y: np.log(weight) +
                                   self._log_sequence_weight_from(
                                       sequence_value[1:], x, y),
                                   next_states, weights))

    def last_token_weight(self, sequence: Sequence):
        return list(filter(lambda x: x > 0, chain.from_iterable(
            map(lambda x: self._last_token_weight_from(sequence.value, x, x.initial_weight),
                self.weighted_states))))

    def _last_token_weight_from(self, sequence_value, state: WeightedState, weight):
        if weight == 0:
            return [0]
        else:
            if not sequence_value:
                return [weight]
            else:
                if sequence_value[0] == self.terminal_symbol:
                    return [state.final_weight]
                else:
                    transitions = state.transitions_list_for(sequence_value[0])
                    transitions_unzipped = list(zip(*transitions))
                    next_states = transitions_unzipped[0]
                    weights = transitions_unzipped[1]
                    return chain.from_iterable(map(lambda x, y: self._last_token_weight_from(sequence_value[1:], x, y),
                                                   next_states, weights))

    def get_last_token_weights(self, sequence, required_suffixes):
        weights = list()
        for suffix in required_suffixes:
            new_seq = sequence + suffix
            weight = self.last_token_weight(new_seq)
            if len(weight) > 0:
                weights.append(weight[0])
            else:
                weights.append(0)
        return weights

    def __eq__(self, other: Any) -> bool:
        return isinstance(other, WeightedAutomaton) and self._comparator.are_equivalent(self, other)

    def export(self, path):
        for strategy in self.__exporting_strategies:
            strategy.export(self, path)
