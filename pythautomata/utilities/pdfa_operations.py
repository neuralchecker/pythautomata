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