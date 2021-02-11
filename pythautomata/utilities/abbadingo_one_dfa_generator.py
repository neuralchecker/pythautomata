from base_types.state import State
from functools import reduce
from automata.deterministic_finite_automaton import DeterministicFiniteAutomaton as DFA
from exceptions.non_deterministic_states_exception import NonDeterministicStatesException
from random import seed, getrandbits, choice
from model_exporters.encoded_file_exporting_strategy import EncodedFileExportingStrategy
from model_exporters.image_exporting_strategy import ImageExportingStrategy
from model_comparators.hopcroft_karp_comparison_strategy import HopcroftKarpComparisonStrategy as AutomataComparator
import simple_dfa_generator

def generate_dfa(alphabet, nominal_size, seed = 42):
    number_of_states = math.ceil((5*nominal_size)/4)
    dfa = simple_dfa_generator.generate_dfa(alphabet, number_of_states, seed)
    dfa_depth = _compute_depth(dfa)
    seed = seed + 1
    while dfa_depth != math.ceil(2*math.log(nominal_size,2)-2):
        dfa = simple_dfa_generator.generate_dfa(alphabet,  number_of_states, seed)
        dfa_depth = _compute_depth(dfa)     
        seed = seed + 1       
    return dfa
 
def _compute_depth(dfa):
    all_states = dfa.states
    initial_state = dfa.initial_state
    to_visit = [(initial_state,0)]
    depths = {}
    while len(to_visit) > 0:            
        state, depth = to_visit[-1]
        to_visit.pop()
        depths[state] = depth           
        for symbol in dfa.alphabet.symbols:
            next_states = state.next_states_for(symbol)
            for next_state in next_states:
                if next_state not in [i[0] for i in to_visit] and next_state not in depths:
                    to_visit.append((next_state, depth+1))
    
    assert(len(depths)==len(all_states))
    max_depth = max(depths.values())
    return max_depth
