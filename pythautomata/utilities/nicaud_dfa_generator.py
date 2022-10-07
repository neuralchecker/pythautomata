from pythautomata.base_types.alphabet import Alphabet
from pythautomata.automata.deterministic_finite_automaton import DeterministicFiniteAutomaton as DFA
import pythautomata.utilities.simple_dfa_generator as simple_dfa_generator
import math
from scipy.special import lambertw
from math import exp


def generate_dfa(alphabet: Alphabet, nominal_size: int, seed: int = 42) -> DFA:
    """
    Function returning a randomly generated DFA in the manner descbribed by Cyril Nicaud in: 
        Nicaud, Cyril. (2014). Random Deterministic Automata. 5-23. 10.1007/978-3-662-44522-8_2. 

    Args:
        alphabet (Alphabet): DFA alphabet.
        nominal_size (int): Target nominal size of the generated DFA.
        seed (int, optional): Random seed. Defaults to 42.

    Returns:
        DFA: Random DFA with distribution of sizes centered near nominal_size and depth centered near 2*log(nominal_size,2)-2
    """
    k = len(alphabet)
    ro_k = k + lambertw(-k * exp(-k))
    ro_k = ro_k.real
    v_k = ro_k/k
    number_of_states = math.ceil(nominal_size / v_k)
    dfa = simple_dfa_generator.generate_dfa(alphabet, number_of_states, seed)
    return dfa
