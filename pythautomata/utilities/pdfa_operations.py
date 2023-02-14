from pythautomata.base_types.sequence import Sequence
from pythautomata.automata.wheighted_automaton_definition.probabilistic_deterministic_finite_automaton import \
    ProbabilisticDeterministicFiniteAutomaton as PDFA
import numpy as np


def get_representative_sample(pdfa: PDFA, sample_size: int):
    assert (sample_size >= 0)
    sample = list()
    for i in range(sample_size):
        sample.append(_get_representative_word(pdfa))
    return sample


def _get_representative_word(pdfa: PDFA):
    word = Sequence()
    first_state = list(filter(lambda x: x.initial_weight ==
                       1, pdfa.weighted_states))[0]
    symbols, weights, next_states = first_state.get_all_symbol_weights()
    next_symbol = np.random.choice(symbols, p=weights)
    while next_symbol != pdfa.terminal_symbol:
        word += next_symbol
        i = symbols.index(next_symbol)
        next_state = next_states[i]
        symbols, weights, next_states = next_state.get_all_symbol_weights()
        next_symbol = np.random.choice(symbols, p=weights)
    return word
