from math import exp
import math
from pythautomata.automata.moore_machine_automaton import MooreMachineAutomaton
from pythautomata.base_types.alphabet import Alphabet
from scipy.special import lambertw
import pythautomata.utilities.simple_mm_generator as simple_moore_machine_generator
from pythautomata.model_exporters.dot_exporters.moore_dot_exporting_strategy import MooreDotExportingStrategy


def generate_moore_machine(input_alphabet: Alphabet, output_alphabet: Alphabet, nominal_size: int, seed: int = None, exporting_strategies: list = [MooreDotExportingStrategy()]) -> MooreMachineAutomaton:
    """
    Function returning a randomly generated Moore Machine based on: 
        Nicaud, Cyril. (2014). Random Deterministic Automata. 5-23. 10.1007/978-3-662-44522-8_2. 

    Args:
        input_alphabet (Alphabet): Moore Machine input alphabet.
        output_alphabet (Alphabet): Moore Machine output alphabet.
        nominal_size (int): Target nominal size of the generated DFA.
        seed (int, optional): Random seed. Defaults to None.
        exporting_strategies (list, optional): List of exporting strategies. Defaults to [DotExportingStrategy()].

    Returns:
        MooreMachineAutomaton: Random Moore Machine with distribution of sizes centered near nominal_size and depth centered near 2*log(nominal_size,2)-2
    """
    k = len(input_alphabet)
    ro_k = k + lambertw(-k * exp(-k))
    ro_k = ro_k.real
    v_k = ro_k/k
    number_of_states = math.ceil(nominal_size / v_k)
    moore_machine = simple_moore_machine_generator.generate_moore_machine(
        input_alphabet, output_alphabet, number_of_states, seed=seed, exporting_strategies=exporting_strategies)
    return moore_machine
