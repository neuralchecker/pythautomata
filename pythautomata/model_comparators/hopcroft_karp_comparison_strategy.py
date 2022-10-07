from typing import Union

from pythautomata.abstract.finite_automaton import FiniteAutomataComparator
from pythautomata.abstract.finite_automaton import FiniteAutomaton as FA
from pythautomata.base_types.sequence import Sequence
from pythautomata.base_types.state import State
from pythautomata.base_types.symbol import Symbol
from pythautomata.base_types.symbolic_state import SymbolicState


class HopcroftKarpComparisonStrategy(FiniteAutomataComparator):
    def are_equivalent(self, automaton1: FA, automaton2: FA) -> bool:
        try:
            return self._inner_are_equivalent(automaton1, automaton2) is None
        except ValueError:
            return False

    def get_counterexample_between(self, automaton1: FA, automaton2: FA) -> Union[Sequence, None]:
        counterexample = self._inner_are_equivalent(automaton1, automaton2)
        return counterexample

    def equivalent_output(self, observation1, observation2) -> bool:
        return observation1 == observation2

    def _inner_are_equivalent(self, fa1: FA, fa2: FA) -> Union[Sequence, None]:
        if fa1.has_full_alphabet and fa2.has_full_alphabet:
            if not fa1.alphabet == fa2.alphabet:
                raise ValueError('Alphabets are not equivalent.')

        # symbols is the union of both finite automata's alphabets
        # because one or both of the automata might not have a full alphabet
        symbols = list(fa1.alphabet.symbols | fa2.alphabet.symbols)
        aut1_new_transitions = self._generate_initial_table(fa1, symbols)
        aut2_new_transitions = self._generate_initial_table(fa2, symbols)
        should_be_equivalent_states = {(
            fa1.initial_states, fa2.initial_states): Sequence()}

        checked_equivalence = dict()

        aut1_completed = False
        aut2_completed = False

        while len(should_be_equivalent_states) > 0 or not (aut1_completed and aut2_completed):

            for state_pair, sequence in should_be_equivalent_states.copy().items():
                (aut1_states, aut2_states) = state_pair

                checked_equivalence[frozenset(
                    aut1_states)] = frozenset(aut2_states)

                if not frozenset(aut1_states) in aut1_new_transitions:
                    aut1_next_states = [None for _ in symbols]
                else:
                    aut1_next_states = aut1_new_transitions[frozenset(
                        aut1_states)]

                if not frozenset(aut2_states) in aut2_new_transitions:
                    aut2_next_states = [None for _ in symbols]
                else:
                    aut2_next_states = aut2_new_transitions[frozenset(
                        aut2_states)]

                for sym_index, symbol in enumerate(symbols):
                    aut1_next_states_for_sym = aut1_next_states[sym_index]
                    aut2_next_states_for_sym = aut2_next_states[sym_index]

                    if aut1_next_states_for_sym is None:
                        aut1_next_states_for_sym = self._fill_transitions_for(
                            list(aut1_states), symbol, fa1.hole)

                    if aut2_next_states_for_sym is None:
                        aut2_next_states_for_sym = self._fill_transitions_for(
                            list(aut2_states), symbol, fa2.hole)

                    aut1_reaches_final = self._reaches_final_state(
                        aut1_next_states_for_sym)
                    aut2_reaches_final = self._reaches_final_state(
                        aut2_next_states_for_sym)
                    if aut1_reaches_final != aut2_reaches_final:
                        return sequence + symbol

                    aut1_next_states[sym_index] = aut1_next_states_for_sym
                    aut2_next_states[sym_index] = aut2_next_states_for_sym

                    if self._has_key_or_diff_content(aut1_next_states_for_sym, checked_equivalence, aut2_next_states_for_sym):
                        should_be_equivalent_states[(frozenset(aut1_next_states_for_sym), frozenset(
                            aut2_next_states_for_sym))] = sequence + symbol

                if frozenset(aut1_states) in checked_equivalence:
                    if (aut1_states, checked_equivalence[frozenset(aut1_states)]) in should_be_equivalent_states:
                        del should_be_equivalent_states[(
                            aut1_states, checked_equivalence[frozenset(aut1_states)])]

                aut1_new_transitions[frozenset(aut1_states)] = aut1_next_states
                aut2_new_transitions[frozenset(aut2_states)] = aut2_next_states

            aut1_completed = self._check_table_is_completed(
                aut1_new_transitions)
            aut2_completed = self._check_table_is_completed(
                aut2_new_transitions)
        return None

    def _has_key_or_diff_content(self, aut1_next_states_for_sym, checked_equivalence, aut2_next_states_for_sym):
        contains_key_or_has_different_content = frozenset(aut1_next_states_for_sym) not in checked_equivalence or \
            (checked_equivalence[frozenset(aut1_next_states_for_sym)] != frozenset(
                aut2_next_states_for_sym))
        return contains_key_or_has_different_content

    def _check_table_is_completed(self, new_transitions):
        completed = True
        for next_states in new_transitions.values():
            for next_state_for_symb in next_states:
                if len(next_state_for_symb) > 0 and not frozenset(next_state_for_symb) in new_transitions.keys():
                    completed = False
                    break
        return completed

    def _reaches_final_state(self, next_states_for_sym):
        return any(True for state in next_states_for_sym if state.is_final)

    def _generate_initial_table(self, automaton, symbols: list[Symbol]) -> dict[frozenset[list[Union[State, SymbolicState]]], list[Union[State, SymbolicState]]]:
        initial_states = list(automaton.initial_states)
        next_states_after_initial = self._get_next_states_from_state(
            automaton, initial_states, symbols)
        new_transitions = {
            frozenset(initial_states): next_states_after_initial}
        return new_transitions

    def _get_next_states_from_state(self, fa, states: list[Union[State, SymbolicState]], symbols: list[Symbol]) -> list[list[Union[State, SymbolicState]]]:
        aut_result = list(map(lambda symbol: self._fill_transitions_for(
            states, symbol, fa.hole), symbols))
        return aut_result

    def _fill_transitions_for(self, states: list[Union[State, SymbolicState]], symbol, hole):
        result: list[Union[State, SymbolicState]] = []
        for state in states:
            next_states = state.next_states_for(symbol)
            if not hole in next_states:
                result.extend(next_state for next_state in next_states
                              if next_state not in result)
        return [hole] if len(result) == 0 else result
