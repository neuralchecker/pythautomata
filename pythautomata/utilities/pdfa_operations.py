from pythautomata.base_types.sequence import Sequence
from pythautomata.automata.wheighted_automaton_definition.probabilistic_deterministic_finite_automaton import \
    ProbabilisticDeterministicFiniteAutomaton as PDFA
import numpy as np

from pythautomata.utilities.moore_machine_minimizer import MooreMachineMinimizer
from pythautomata.automata.moore_machine_automaton import MooreMachineAutomaton
from pythautomata.base_types.moore_state import MooreState
from pythautomata.base_types.symbol import SymbolStr
from pythautomata.base_types.alphabet import Alphabet
from pythautomata.model_comparators.moore_machine_comparison_strategy import MooreMachineComparisonStrategy as MooreMachineComparison
from pythautomata.automata.wheighted_automaton_definition.weighted_state import WeightedState
import math


def get_representative_sample(pdfa: PDFA, sample_size: int, max_length: int = None):
    assert (sample_size >= 0)
    sample = list()
    if max_length is None:
        max_length = math.inf
    for i in range(sample_size):
        sample.append(_get_representative_word(pdfa, max_length))
    return sample


def _get_representative_word(pdfa: PDFA, max_length: int):
    word = Sequence()
    first_state = list(filter(lambda x: x.initial_weight ==
                       1, pdfa.weighted_states))[0]
    symbols, weights, next_states = first_state.get_all_symbol_weights()
    next_symbol = np.random.choice(symbols, p=weights)
    total_length = 0
    while next_symbol != pdfa.terminal_symbol and total_length < max_length:
        word += next_symbol
        i = symbols.index(next_symbol)
        next_state = next_states[i]
        symbols, weights, next_states = next_state.get_all_symbol_weights()
        if np.sum(weights)!=1:
            weights = weights/np.sum(weights)
        next_symbol = np.random.choice(symbols, p=weights)
        total_length+=1
    return word


def check_is_minimal(pdfa: PDFA):
    #Build Moore Machine
    moore_states_dict = dict()
    output_symbols = set()
    for state in pdfa.weighted_states:
        _, weights, _ = state.get_all_symbol_weights()
        output_symbol = SymbolStr(str(weights))
        output_symbols.add(output_symbol)
        moore_state = MooreState(state.name, value = output_symbol)
        moore_states_dict[state.name]= moore_state

    output_alphabet = Alphabet(output_symbols)

    for state in pdfa.weighted_states:
        for symbol in pdfa.alphabet.symbols:
            next_state = min(state.next_states_for(symbol))
            moore_states_dict[state.name].add_transition(symbol, moore_states_dict[next_state.name])

    initial_state = moore_states_dict[min(pdfa.initial_states).name]

    moore_machine = MooreMachineAutomaton(input_alphabet=pdfa.alphabet, 
                                          output_alphabet= output_alphabet, 
                                          initial_state= initial_state, 
                                          states = set(moore_states_dict.values()), 
                                          comparator = MooreMachineComparison())

    #Minimize
    minimal_machine = MooreMachineMinimizer(moore_machine).minimize()

    #Compare sizes
    return len(minimal_machine.states) == len(moore_machine.states)


def make_absorbent(pdfa: PDFA,  epsilon: float = 0.02):
    """
    Make the PDFA absorbent by adding a hole state and make zero probabilities transitions got to it.

    Parameters
    ----------
    pdfa : ProbabilisticDeterministicFiniteAutomaton
        The PDFA to be made absorbent.
    epsilon : float, optional
        The threshold for considering a transition weight as zero, by default 0.02

    Returns
    -------
    ProbabilisticDeterministicFiniteAutomaton
        The modified PDFA with an absorbent state.
    """
    
    symbols = list(pdfa.alphabet.symbols)
    symbols.sort()
    added_transitions = 0
    terminal_symbol = pdfa.terminal_symbol

    hole = WeightedState("HOLE", 0, 1, terminal_symbol=terminal_symbol)

    for symbol in symbols:
        hole.add_transition(symbol, hole, 0)
    
    new_weighted_states = pdfa.weighted_states.copy()

    for state in new_weighted_states:
        symbols, weights, next_states = state.get_all_symbol_weights()
        for symbol, weight in zip(symbols, weights):
            if abs(weight) < epsilon and symbol != terminal_symbol:
                state.transitions_set[symbol] = set()
                state.transitions_list[symbol] = list()
                state.add_transition(symbol, hole, 0)
                added_transitions +=1
    if added_transitions > 0:
        new_weighted_states.add(hole)

    visited_states = set()
    states_to_visit = [pdfa.get_first_state()]    
    while states_to_visit:
        state = states_to_visit.pop(0)
        visited_states.add(state)
        for symbol in pdfa.alphabet.symbols:
            next_state = min(state.next_states_for(symbol))
            if next_state and next_state not in visited_states:                
                states_to_visit.append(next_state)
    for state in pdfa.weighted_states:
        if state not in visited_states:
            new_weighted_states.remove(state)
    
    return PDFA(pdfa.alphabet, new_weighted_states, pdfa.terminal_symbol, pdfa.comparator, pdfa.name+"_absorbent")
