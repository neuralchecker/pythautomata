from pythautomata.abstract.model_exporting_strategy import \
    ModelExportingStrategy
from pythautomata.automata.deterministic_finite_automaton import \
    DeterministicFiniteAutomaton as DFA
from pythautomata.automata.non_deterministic_finite_automaton import \
    NondeterministicFiniteAutomaton as NFA
from pythautomata.automata.symbolic_finite_automaton import \
    SymbolicFiniteAutomaton as SFA
from pythautomata.base_types.guard import Guard
from pythautomata.base_types.state import State
from pythautomata.base_types.symbol import Symbol
from pythautomata.base_types.symbolic_state import SymbolicState
from pythautomata.boolean_algebra_learner.boolean_algebra_learner import \
    BooleanAlgebraLearner as BAL
from pythautomata.model_comparators.dfa_comparison_strategy import \
    DFAComparisonStrategy as DFAComparator
from pythautomata.model_comparators.hopcroft_karp_comparison_strategy import \
    HopcroftKarpComparisonStrategy as HopcroftKarpComparison


class AutomataConverter():\

    @staticmethod
    def convert_nfa_to_dfa(non_deterministic_finite_automaton: NFA) -> DFA:
        """
        Converts a given non deterministic finite automaton into a deterministic finite automaton.

        Args:
            non_deterministic_finite_automaton (NFA): Input non deterministic finite automaton.

        Returns:
            DFA: DFA equivalent to the inputted NFA.
        """
        initial_states = list(
            non_deterministic_finite_automaton.initial_states)
        symbols = list(non_deterministic_finite_automaton.alphabet.symbols)
        next_states_after_initial = AutomataConverter._get_next_states_from_state(
            non_deterministic_finite_automaton, initial_states)
        new_transitions: dict[frozenset[State], list[list[State]]] = {
            frozenset(initial_states): next_states_after_initial}

        # TODO extract func
        completed = False
        while not completed:
            for states in new_transitions.copy().keys():
                for next_states in new_transitions[states]:
                    if len(next_states) > 0 and not frozenset(next_states) in new_transitions:
                        next_states_after_this = AutomataConverter._get_next_states_from_state(
                            non_deterministic_finite_automaton, next_states)
                        new_transitions[frozenset(
                            next_states)] = next_states_after_this
            completed = True

            for next_states_by_symbol in new_transitions.values():
                for next_states in next_states_by_symbol:
                    if len(next_states) > 0 and not frozenset(next_states) in new_transitions.keys():
                        completed = False
                        break

        # TODO extract func
        new_states_pairs = []
        for states in new_transitions.keys():
            stateName = " and ".join([state.name for state in states])
            is_final = any([state.is_final for state in states])
            new_state = State(stateName, is_final)
            if states == set(initial_states):
                new_initial_state = new_state
            new_states_pairs.append((new_state, states))

        # TODO extract func
        for (new_state, dict_key) in new_states_pairs:
            for ind_symbol, next_states in enumerate(new_transitions[dict_key]):
                if len(next_states) > 0:
                    symbol = symbols[ind_symbol]

                    next_new_state = AutomataConverter._find_state(
                        next_states, new_states_pairs)

                    if next_new_state is not None:
                        new_state.add_transition(symbol, next_new_state)

        comparator = DFAComparator()
        return DFA(
            non_deterministic_finite_automaton.alphabet,
            new_initial_state,
            set((new_state for (new_state, dict_key) in new_states_pairs)),
            comparator=comparator
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

    @staticmethod
    def convert_dfa_to_sfa(dfa: DFA, b_a_learner: BAL, exportingStrategies: list[ModelExportingStrategy] = []) -> SFA:
        """
        Converts a given deterministic finite automaton into a symbolic finite automaton.

        Args:
            automaton (DFA): Input deterministic finite automaton.

        Returns:
            DFA: DFA equivalent to the inputted NFA.
        """
        initial_state: SymbolicState
        states: dict[str, SymbolicState] = {}
        # get all states and convert them to symbolic state
        for state in dfa.states:
            new_state: SymbolicState = SymbolicState(
                state.name, state.is_final)
            if new_state.name == dfa.initial_state.name:
                initial_state = new_state
            states[new_state.name] = new_state

        for state in dfa.states:
            # for each state, get the multimap that has the next state as key, and a list of symbols as value
            multidict: dict[SymbolicState, list[Symbol]] = {}
            for symbol, state_set in state.transitions.items():
                current_state = list(state_set).pop()
                transition_state = states[current_state.name]
                if transition_state in multidict:
                    multidict[transition_state].append(symbol)
                else:
                    multidict[transition_state] = [symbol]
            guard_state_list: list[tuple[Guard, SymbolicState]
                                   ] = b_a_learner.learn(multidict)
            for guard, s in guard_state_list:
                states[state.name].add_transition(guard, s)

        name = None if dfa.name == None else "SFA_"+dfa.name
        return SFA(dfa.alphabet, initial_state, set(states.values()), name, exportingStrategies)
