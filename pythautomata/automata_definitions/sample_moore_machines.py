from pythautomata.base_types.state import State
from pythautomata.base_types.symbol import SymbolStr
from pythautomata.base_types.alphabet import Alphabet

from pythautomata.automata.moore_machines.moore_machine_automaton import MooreMachineAutomaton
from pythautomata.automata.moore_machines.moore_state import MooreState

from pythautomata.model_comparators.dfa_comparison_strategy import DFAComparisonStrategy as DFAComparison

from pythautomata.utilities.automata_converter import AutomataConverter

abAlphabet = Alphabet(frozenset((SymbolStr('a'), SymbolStr('b'))))
abcAlphabet = Alphabet(frozenset((SymbolStr('a'), SymbolStr('b'), SymbolStr('c'))))

# TODO: DOCUMENT AND TEST


class SampleMooreMachines:
    """
    Class containing sample Moore Machines

    Methods
    -------

    """
    @staticmethod
    def get_all_automata():
        return [
            SampleMooreMachines.get_3_states_automaton(),
            #! Estos ejemplos fallan las pruebas
            # SampleMooreMachines.get_3_states_automaton_wrong_alphabet(),
            # SampleMooreMachines.get_3_states_automaton_non_deterministic()
        ]

    @staticmethod
    def get_3_states_automaton():
        a = abAlphabet['a']
        b = abAlphabet['b']

        state0 = MooreState("State 0", abcAlphabet["a"]);
        state1 = MooreState("State 1", abcAlphabet["b"]);
        state2 = MooreState("State 2", abcAlphabet["c"]);

        state0.add_transition(a, state1)
        state0.add_transition(b, state2)
        state1.add_transition(a, state2)
        state1.add_transition(b, state0)
        state2.add_transition(a, state0)
        state2.add_transition(b, state1)

        return MooreMachineAutomaton(abAlphabet, abcAlphabet, frozenset({state0}), 
                set([state0, state1, state2]), DFAComparison(), "3 States Moore Machine")

    @staticmethod
    def get_3_states_automaton_wrong_alphabet():
        a = abAlphabet['a']
        b = abAlphabet['b']

        state0 = MooreState("State 0", abcAlphabet["a"]);
        state1 = MooreState("State 1", abcAlphabet["b"]);
        state2 = MooreState("State 2", abcAlphabet["c"]);

        state0.add_transition(a, state1)
        state0.add_transition(b, state2)
        state1.add_transition(a, state2)
        state1.add_transition(b, state0)
        state2.add_transition(a, state0)
        state2.add_transition(b, state1)

        return MooreMachineAutomaton(abAlphabet, abAlphabet, frozenset({state0}), 
                set([state0, state1, state2]), DFAComparison(), "3 States Moore Machine")

    @staticmethod
    def get_3_states_automaton_non_deterministic():
        a = abAlphabet['a']
        b = abAlphabet['b']

        state0 = MooreState("State 0", abcAlphabet["a"]);
        state1 = MooreState("State 1", abcAlphabet["b"]);
        state2 = MooreState("State 2", abcAlphabet["c"]);

        state0.add_transition(a, state1)
        state0.add_transition(a, state2)
        state0.add_transition(b, state2)
        state1.add_transition(a, state2)
        state1.add_transition(b, state0)
        state2.add_transition(a, state0)
        state2.add_transition(b, state1)

        return MooreMachineAutomaton(abAlphabet, abAlphabet, frozenset({state0}), 
                set([state0, state1, state2]), DFAComparison(), "3 States Moore Machine")

    