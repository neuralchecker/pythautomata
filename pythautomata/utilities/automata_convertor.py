from base_types.state import State
from automata.deterministic_finite_automaton import DeterministicFiniteAutomaton as DFA
from automata.non_deterministic_finite_automaton import NondeterministicFiniteAutomaton as NFA
from model_comparators.nfa_hopcroft_karp_comparison_strategy import NFAHopcroftKarpComparisonStrategy as NFAComparator
from model_comparators.dfa_comparison_strategy import DFAComparisonStrategy as DFAComparator


class AutomataConvertor():

    @staticmethod
    def convert_nfa_to_dfa(non_deterministic_finite_automaton: NFA) -> DFA:
        """
        Converts a given non deterministic finite automaton into a deterministic finite automaton.

        Args:
            non_deterministic_finite_automaton (NFA): Input non deterministic finite automaton.

        Returns:
            DFA: DFA equivalent to the inputted NFA.
        """
        initial_states = list(non_deterministic_finite_automaton.initial_states)
        symbols = list(non_deterministic_finite_automaton.alphabet.symbols)
        next_states_after_initial = AutomataConvertor._get_next_states_from_state(non_deterministic_finite_automaton, initial_states)
        new_transitions: dict[frozenset[State], list[list[State]]] = {frozenset(initial_states): next_states_after_initial}

        #TODO extract func
        completed = False
        while not completed:
            for states in new_transitions.copy().keys():
                for next_states in new_transitions[states]:
                    if len(next_states) > 0 and not frozenset(next_states) in new_transitions:
                        next_states_after_this = AutomataConvertor._get_next_states_from_state(non_deterministic_finite_automaton, next_states)
                        new_transitions[frozenset(next_states)] = next_states_after_this
            completed = True

            for next_states_by_symbol in new_transitions.values():
                for next_states in next_states_by_symbol:
                    if len(next_states) > 0 and not frozenset(next_states) in new_transitions.keys():
                        completed = False
                        break

        #TODO extract func
        new_states_pairs = []
        for states in new_transitions.keys():
            stateName = " and ".join([state.name for state in states])
            is_final = any([state.is_final for state in states])
            new_state = State(stateName, is_final)
            if states == set(initial_states):
                new_initial_state = new_state
            new_states_pairs.append((new_state, states))

        #TODO extract func
        for (new_state, dict_key) in new_states_pairs:
            for ind_symbol, next_states in enumerate(new_transitions[dict_key]):
                if len(next_states) > 0:
                    symbol = symbols[ind_symbol]

                    next_new_state = AutomataConvertor._find_state(
                        next_states, new_states_pairs)

                    if next_new_state is not None:
                        new_state.add_transition(symbol, next_new_state)

        comparator = DFAComparator()
        return DFA(
            non_deterministic_finite_automaton.alphabet,
            new_initial_state,
            set((new_state for (new_state, dict_key) in new_states_pairs)), 
            comparator = comparator
            )

    @staticmethod
    def _find_state(next_states, new_states_pairs):
        for (new_state, dict_key) in new_states_pairs:
            if dict_key == frozenset(next_states):
                return new_state

    @staticmethod
    def _get_next_states_from_state(automaton, states: list[State]) -> list[list[State]]:
        symbols = automaton.alphabet.symbols
        result: list[list[State]] = [[] for sym in symbols]

        for state in states:
            for sym_index, symbol in enumerate(symbols):
                next_states = state.next_states_for(symbol)
                if automaton.hole not in next_states:
                    result[sym_index].extend(next_state for next_state in next_states
                                             if next_state not in result[sym_index])

        return result
