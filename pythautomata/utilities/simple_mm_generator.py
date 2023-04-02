import random
from pythautomata.automata.moore_machine_automaton import MooreMachineAutomaton
from pythautomata.base_types.alphabet import Alphabet
from pythautomata.base_types.moore_state import MooreState
from pythautomata.model_comparators.moore_machine_comparison_strategy import MooreMachineComparisonStrategy
from pythautomata.model_exporters.image_exporters.image_exporting_strategy import ImageExportingStrategy
from pythautomata.model_exporters.dot_exporters.moore_dot_exporting_strategy import MooreDotExportingStrategy


def generate_moore_machine(input_alphabet: Alphabet, output_alphabet: Alphabet, number_of_states: int = 200, seed: int = None, exporting_strategies: list = [ImageExportingStrategy(MooreDotExportingStrategy(), "pdf")]) -> MooreMachineAutomaton:
    """
    Function returning a randomly generated Moore Machine.

    Args:
        input_alphabet (Alphabet): Moore Machine input alphabet.
        output_alphabet (Alphabet): Moore Machine output alphabet.
        number_of_states (int): Number of states of the generated Moore Machine. Defaults to 200.
        seed (int): Seed for the random number generator. Defaults to None.
        exporting_strategies (list, optional): List of strategies to export the generated Moore Machine. Defaults to [ImageExportingMMStrategy()].

    Returns:
        MooreMachineAutomaton: Random Moore Machine.
    """
    if seed is not None:
        random.seed(seed)
    states = _generate_states(number_of_states, output_alphabet)
    _add_moore_machine_transitions_to_states(states, input_alphabet.symbols)
    initial_state = next(iter(states))
    states = _remove_unreachable_states(initial_state, input_alphabet.symbols)
    comparator = MooreMachineComparisonStrategy()
    return MooreMachineAutomaton(input_alphabet, output_alphabet, initial_state, states, comparator=comparator, exportingStrategies=exporting_strategies)


def _generate_states(number_of_states, output_alphabet):
    states = []
    for index in range(number_of_states):
        generated_state = MooreState(
            # do a sample of size 1 and get the first element
            str(index), random.sample(output_alphabet.symbols, 1).pop())
        states.append(generated_state)
    return states


def _add_moore_machine_transitions_to_states(states, symbols):
    for state in states:
        for symbol in symbols:
            random_state = random.choice(states)
            state.add_transition(symbol, random_state)


def _remove_unreachable_states(initial_state, symbols):
    reachable_states = _get_reachable_states_from(initial_state, symbols)
    return reachable_states


def _get_reachable_states_from(initial_state, symbols):
    states_to_visit = [initial_state]
    visited_states = []
    while len(states_to_visit) > 0:
        state = states_to_visit.pop()
        visited_states.append(state)
        for symbol in symbols:
            next_states = state.next_states_for(symbol)
            for next_state in next_states:
                if next_state not in visited_states and next_state not in states_to_visit:
                    states_to_visit.append(next_state)
    return set(visited_states)
