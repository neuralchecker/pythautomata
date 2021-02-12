from base_types.state import State
from base_types.alphabet import Alphabet
from functools import reduce
from automata.deterministic_finite_automaton import DeterministicFiniteAutomaton as DFA
from exceptions.non_deterministic_states_exception import NonDeterministicStatesException
from random import seed, getrandbits, choice
from model_exporters.encoded_file_exporting_strategy import EncodedFileExportingStrategy
from model_exporters.image_exporting_strategy import ImageExportingStrategy
from model_comparators.dfa_comparison_strategy import DFAComparisonStrategy as AutomataComparator
import simple_dfa_generator
import math


def generate_dfa(alphabet: Alphabet, nominal_size: int, seed: int = 42) -> DFA:
    """
    Function returning a randomly generated DFA in the style of Abbadingo One Competition: 
        Kevin J. Lang, Barak A. Pearlmutter, and Rodney A. Price. 1998. 
        Results of the Abbadingo One DFA Learning Competition and a New Evidence-Driven State Merging Algorithm. 
        In Proceedings of the 4th International Colloquium on Grammatical Inference (ICGI '98). Springer-Verlag, Berlin, Heidelberg, 1–12.
    
    Args:
        alphabet (Alphabet): DFA alphabet.
        nominal_size (int): Target nominal size of the generated DFA.
        seed (int, optional): Random seed. Defaults to 42.

    Returns:
        DFA: Random DFA with nominal size = nominal_size.
    """
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
