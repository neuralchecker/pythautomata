from __future__ import annotations
from pythautomata.automata.wheighted_automaton_definition.weighted_transition import WeightedTransition
from pythautomata.base_types.symbol import Symbol
from pythautomata.exceptions.none_state_exception import NoneStateException
from pythautomata.exceptions.non_deterministic_states_exception import NonDeterministicStatesException
from typing import Union


class WeightedState:

    def __init__(self, name, initial_weight, final_weight):
        self.name = name
        self.transitions_set: dict[Symbol, set[WeightedTransition]] = dict()
        self.transitions_list: dict[Symbol, list[tuple[WeightedState, float]]] = dict()
        self.initial_weight: float = initial_weight
        self.final_weight: float = final_weight

    def add_transition(self, symbol: Symbol, next_state: WeightedState, weight: float) -> None:
        if next_state is None:
            raise NoneStateException()
        if symbol not in self.transitions_set:
            self.transitions_set[symbol] = set()
            self.transitions_list[symbol] = list()
        transition = WeightedTransition(next_state, weight)
        if transition not in self.transitions_set[symbol]:
            self.transitions_set[symbol].add(WeightedTransition(next_state, weight))
            self.transitions_list[symbol].append((next_state, weight))

    def transitions_set_for(self, symbol: Symbol) -> set[WeightedTransition]:
        if symbol not in self.transitions_set:
            raise Exception(f'No transition for symbol: {symbol}')
        return self.transitions_set[symbol]

    def transitions_list_for(self, symbol) -> list[tuple[WeightedState, float]]:
        if symbol not in self.transitions_list.keys():
            raise Exception(f'No transition for symbol: {symbol}')
        return self.transitions_list[symbol]

    def next_states_for(self, symbol: Symbol) -> set['WeightedState']:
        if symbol not in self.transitions_list.keys():
            raise NonDeterministicStatesException()
        return set(t[0] for t in self.transitions_list[symbol])

    def get_all_symbol_weights(self, terminal_symbol) -> tuple[list[Symbol], list[float], list[WeightedState]]:
        symbols = list()
        weights = list()
        next_states = list()
        for symbol, weighted_transition_set in self.transitions_set.items():
            for weighted_transition in weighted_transition_set:
                symbols.append(symbol)
                weights.append(weighted_transition.weight)
                next_states.append(weighted_transition.next_state)
        weights.append(self.final_weight)
        next_states.append(None)
        symbols.append(terminal_symbol)
        return symbols, weights, next_states

    def __eq__(self, other):
        if not isinstance(other, WeightedState):
            return False
        else:
            r1 = self.initial_weight == other.initial_weight
            r2 = self.final_weight == other.final_weight
            r3 = self.check_transitions(other, set())
            return r1 and r2 and r3

    def equals(self, other, visited):
        if (self.name, other.name) in visited:
            return True
        visited.add((self.name, other.name))
        r1 = self.initial_weight == other.initial_weight
        r2 = self.final_weight == other.final_weight
        r3 = self.check_transitions(other, visited)
        return r1 and r2 and r3

    def check_transitions(self, other, visited):
        if (self.name, other.name) in visited:
            return True
        ret = True
        visited.add((self.name, other.name))
        for symbol, transitions in self.transitions_list.items():
            other_transitions = other.transitions_list[symbol]
            if len(transitions) > 1 or len(other_transitions) > 1:
                # TODO custom exception
                raise Exception("Eq method supported only for Deterministic Weighted FA")
            transition = transitions[0]
            other_transition = other_transitions[0]
            ret = ret and transition[1] == other_transition[1] \
                  and transition[0].equals(other_transition[0], visited)
        return ret

    def __hash__(self):
        return hash(self.name)

    def __str__(self):
        return repr(self)

    def __repr__(self):
        return str(self.name)
