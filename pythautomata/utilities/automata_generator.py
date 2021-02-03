from base_types.state import State
from functools import reduce
from automata.deterministic_finite_automaton import DeterministicFiniteAutomaton as DFA
from automata.non_deterministic_finite_automaton import NondeterministicFiniteAutomaton as NFA
from exceptions.non_deterministic_states_exception import NonDeterministicStatesException
from random import seed, getrandbits, choice
from model_exporters.encoded_file_exporting_strategy import EncodedFileExportingStrategy

from model_exporters.image_exporting_strategy import ImageExportingStrategy

#TODO this shouldn't be a class, but an exported function
class AutomataGenerator():

    @staticmethod
    def generate_fa(alphabet, numberOfStates=200, exportingStrategies=[ImageExportingStrategy()], try_dfa: bool = True):
        states = AutomataGenerator._generate_states(numberOfStates)
        AutomataGenerator._add_dfa_transitions_to_states(
            states, alphabet.symbols)
        initial_state = next(iter(states))
        states = AutomataGenerator._remove_unreachable_states(initial_state, alphabet.symbols)
        if try_dfa:
            try:
                return DFA(alphabet, frozenset([initial_state]),states, exportingStrategies=exportingStrategies)
            except NonDeterministicStatesException:
                print("could not build dfa, defaulting to nfa")
        return NFA(alphabet, frozenset([initial_state]),states, exportingStrategies=exportingStrategies)

    @staticmethod
    def _generate_states(number_of_states):
        states = []
        for index in range(number_of_states):
            if number_of_states == 1:
                is_final = True
            else:
                is_final = bool(getrandbits(1))
            generated_state = State(str(index), is_final)
            states.append(generated_state)
        return states

    @staticmethod
    def _add_dfa_transitions_to_states(states, symbols):
        for state in states:
            for symbol in symbols:
                random_state = choice(states)
                state.add_transition(symbol, random_state)

    @staticmethod
    def _remove_unreachable_states(initial_state, symbols):
        reachable_states = {initial_state}
        reachable_states = AutomataGenerator._get_reachable_states_from(
            initial_state, symbols, reachable_states)
        return reachable_states

    @staticmethod
    def _get_reachable_states_from(state, symbols, reachable_states):
        for symbol in symbols:
            next_states = state.next_states_for(symbol)
            for next_state in next_states:
                if next_state not in reachable_states:
                    reachable_states.add(next_state)
                    reachable_states = AutomataGenerator._get_reachable_states_from(
                        next_state, symbols, reachable_states)
        return reachable_states
