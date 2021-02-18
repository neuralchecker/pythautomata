from base_types.state import State
from base_types.alphabet import Alphabet
from functools import reduce
from automata.deterministic_finite_automaton import DeterministicFiniteAutomaton as DFA
from exceptions.non_deterministic_states_exception import NonDeterministicStatesException
from random import seed, getrandbits, choice
from model_exporters.encoded_file_exporting_strategy import EncodedFileExportingStrategy
from model_exporters.image_exporting_strategy import ImageExportingStrategy
from model_comparators.dfa_comparison_strategy import DFAComparisonStrategy as AutomataComparator

def generate_dfa(alphabet: Alphabet, number_of_states: int = 200, exporting_strategies=[ImageExportingStrategy()]) -> DFA:
    """
    Function returning a randomly generated DFA, with random transitions to other states and equal probability of being a final state or not.

    Args:
        alphabet (Alphabet): DFA alphabet.
        number_of_states (int, optional): Number of states the generated DFA.. Defaults to 200.
        exporting_strategies (list, optional): ExportingStrategy for the generated DFA. Defaults to [ImageExportingStrategy()].

    Returns:
        DFA: Random DFA with number of states = number_of_states and exporting strategies = exporting_strategies.
    """
    states = _generate_states(number_of_states)
    _add_dfa_transitions_to_states(states, alphabet.symbols)
    initial_state = next(iter(states))
    states = _remove_unreachable_states(initial_state, alphabet.symbols)    
    comparator = AutomataComparator()
    return DFA(alphabet, initial_state, states,comparator = comparator, exportingStrategies=exporting_strategies)
    
def _generate_states(number_of_states):
    states = []
    for index in range(number_of_states):        
        is_final = bool(getrandbits(1))
        generated_state = State(str(index), is_final)
        states.append(generated_state)
    return states

   
def _add_dfa_transitions_to_states(states, symbols):
    for state in states:
        for symbol in symbols:
            random_state = choice(states)
            state.add_transition(symbol, random_state)

def _remove_unreachable_states(initial_state, symbols):
    reachable_states = {initial_state}
    reachable_states = _get_reachable_states_from(
        initial_state, symbols, reachable_states)
    return reachable_states

def _get_reachable_states_from(state, symbols, reachable_states):
    for symbol in symbols:
        next_states = state.next_states_for(symbol)
        for next_state in next_states:
            if next_state not in reachable_states:
                reachable_states.add(next_state)
                reachable_states = _get_reachable_states_from(
                    next_state, symbols, reachable_states)
    return reachable_states
