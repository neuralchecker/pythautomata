import random

from pythautomata.automata.deterministic_finite_automaton import DeterministicFiniteAutomaton
from pythautomata.automata.wheighted_automaton_definition.weighted_automaton import WeightedAutomaton
from pythautomata.automata.wheighted_automaton_definition.weighted_state import WeightedState
from pythautomata.base_types.sequence import Sequence


def pdfa_from_dfa(dfa: DeterministicFiniteAutomaton) -> WeightedAutomaton:
    """
    Function that transforms a DFA to a PDFA with random probability distributions for each state.

    Parameters
    ----------
    dfa : DeterministicFiniteAutomaton

    Returns
    -------
    WeightedAutomaton

    """
    alphabet_length = len(dfa.alphabet)
    wfa_states_dict = {state.name: __dfa_state_to_pdfa_state(state.name, state.name == dfa.initial_state.name) for state
                       in dfa.states}
    for state in dfa.states:
        __add_transitions(alphabet_length, state, wfa_states_dict)
    terminal_symbol = Sequence(['$'])
    return WeightedAutomaton(dfa.alphabet, set(wfa_states_dict.values()), terminal_symbol)


def __dfa_state_to_pdfa_state(name, initial):
    initial_prob = 1 if initial else 0
    final_prob = __get_prob_not_zero(0)
    wfa_state = WeightedState(name, initial_prob, final_prob)
    return wfa_state


def __add_transitions(alphabet_length, state, wfa_states_dict: dict[any, WeightedState]):
    wfa_state = wfa_states_dict[state.name]
    probs = []
    total_prob = wfa_state.final_weight
    for i in range(alphabet_length):
        prob = 1 - total_prob if i == alphabet_length - 1 else __get_prob_not_zero(total_prob)
        probs.append(prob)
        total_prob += prob
    for i, (symbol, next_state) in enumerate(state.transitions.items()):
        next_state = next(iter(next_state))
        wfa_state.add_transition(symbol, wfa_states_dict[next_state.name], probs[i])


def __get_prob_not_zero(total_prob):
    prob = random.triangular(0.0, 1.0 - total_prob)
    while not prob:
        prob = random.triangular(0.0, 1.0 - total_prob)
    return prob
