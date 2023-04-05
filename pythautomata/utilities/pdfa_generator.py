import random

from pythautomata.automata.deterministic_finite_automaton import DeterministicFiniteAutomaton
from pythautomata.automata.wheighted_automaton_definition.probabilistic_deterministic_finite_automaton import \
    ProbabilisticDeterministicFiniteAutomaton
from pythautomata.automata.wheighted_automaton_definition.weighted_state import WeightedState
from pythautomata.base_types.symbol import SymbolStr
from pythautomata.abstract.finite_automaton import FiniteAutomataComparator
from pythautomata.model_comparators.wfa_tolerance_comparison_strategy import WFAToleranceComparator
from typing import Any


def pdfa_from_dfa(dfa: DeterministicFiniteAutomaton, comparator: FiniteAutomataComparator = WFAToleranceComparator(),
                  distributions: int = None, max_shift: float = 0, terminal_symbol: str = '$') -> ProbabilisticDeterministicFiniteAutomaton:
    """
    Function that transforms a DFA to a PDFA with random probability distributions for each state.
    Distributions is a predefined integer that defines the number of different distributions states may have (infinite if None)
    And shift is a float definig the ammount of random noise that may be added to such predefined distributions (only used when distributions != None).

    Parameters
    ----------
    dfa : DeterministicFiniteAutomaton
    comparator : FiniteAutomataComparator
    distributions : int
    max_shift: float
    terminal_symbol: str

    Returns
    -------
    ProbabilisticDeterministicFiniteAutomaton

    """
    alphabet_length = len(dfa.alphabet)
    wfa_states_dict = {state.name: __dfa_state_to_pdfa_state(state.name, state.name == dfa.initial_state.name) for state
                       in dfa.states}
    if distributions is None:
        for state in dfa.states:
            __add_transitions(alphabet_length, state, wfa_states_dict)
    else:
        pool = __generate_pool_of_distributions(alphabet_length, distributions)
        for state in dfa.states:
            distribution = random.choice(pool)
            __add_shift(distribution, max_shift)
            __add_transitions(alphabet_length, state,
                              wfa_states_dict, probability_vector=distribution)

    terminal_symbol = SymbolStr(terminal_symbol)
    return ProbabilisticDeterministicFiniteAutomaton(dfa.alphabet, set(wfa_states_dict.values()), terminal_symbol,
                                                     comparator)


def __generate_pool_of_distributions(alphabet_length, distributions):
    result = []
    for i in range(distributions):
        dist = __generate_random_probability_vector(alphabet_length)
        result.append(dist)
    return result


def __add_shift(distribution, max_shift):
    shift = random.triangular(0, max_shift)
    sign = random.choice([-1, 1])
    total_shift = 0
    for i, elem in enumerate(distribution):
        if i < len(distribution)-1:
            total_shift += shift*sign
            distribution[i] = round(elem + shift*sign, 5)
            sign = sign*-1
            shift = random.triangular(0, max_shift)
        else:
            distribution[i] = round(elem + -1*total_shift, 5)


def __dfa_state_to_pdfa_state(name, initial):
    initial_prob = 1 if initial else 0
    final_prob = None
    wfa_state = WeightedState(name, initial_prob, final_prob)
    return wfa_state


def __generate_random_probability_vector(alphabet_length):
    final_prob = __get_prob(0)
    total_prob = final_prob
    probs = []
    for i in range(alphabet_length):
        prob = round(1.0 - total_prob, 5) if i == alphabet_length - \
            1 else __get_prob(total_prob)
        probs.append(prob)
        total_prob += prob
    probs.append(final_prob)
    return probs


def __add_transitions(alphabet_length, state, wfa_states_dict: dict[Any, WeightedState], probability_vector=None):
    wfa_state = wfa_states_dict[state.name]
    if probability_vector is None:
        probs = __generate_random_probability_vector(alphabet_length)
    else:
        probs = probability_vector
    for i, (symbol, next_state) in enumerate(state.transitions.items()):
        next_state = next(iter(next_state))
        wfa_state.add_transition(
            symbol, wfa_states_dict[next_state.name], probs[i])
    wfa_state.final_weight = probs[-1]


def __get_prob(total_prob):
    prob = random.triangular(0.0, 1.0 - total_prob)
    return round(prob, 5)
