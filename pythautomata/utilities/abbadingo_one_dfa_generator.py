from pythautomata.base_types.alphabet import Alphabet
from pythautomata.automata.deterministic_finite_automaton import DeterministicFiniteAutomaton as DFA
import pythautomata.utilities.simple_dfa_generator as simple_dfa_generator
import math


def generate_dfa(alphabet: Alphabet, nominal_size: int, seed: int = 42) -> DFA:
    """
    Function returning a randomly generated DFA in the style of Abbadingo One Competition, generated as described in: 
        Kevin J. Lang, Barak A. Pearlmutter, and Rodney A. Price. 1998. 
        Results of the Abbadingo One DFA Learning Competition and a New Evidence-Driven State Merging Algorithm. 
        In Proceedings of the 4th International Colloquium on Grammatical Inference (ICGI '98). Springer-Verlag, Berlin, Heidelberg, 1–12.
    
    Args:
        alphabet (Alphabet): DFA alphabet. It must have size exactly 2.
        nominal_size (int): Target nominal size of the generated DFA.
        seed (int, optional): Random seed. Defaults to 42.

    Returns:
        DFA: Random DFA with distribution of sizes centered near nominal_size and depth exactly ceil(2*log(nominal_size,2)-2).
    """
    # Alphabet Size should be 2 to get the desired nominal size
    # For bigger alphabets size use nicaud_dfa_generator
    assert(len(alphabet)==2) 

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
