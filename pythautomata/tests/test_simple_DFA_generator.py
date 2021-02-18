from unittest import TestCase
from utilities.simple_dfa_generator import generate_dfa
from base_types.alphabet import Alphabet
from base_types.symbol import SymbolStr

class TestSimpleDFAGenerator(TestCase):

    def test_generated_correctly_1(self):
        binaryAlphabet = Alphabet(
            frozenset([SymbolStr('0'), SymbolStr('1')]))
        generated_automata = generate_dfa(binaryAlphabet, 80)
        self._assert_correctness(generated_automata)

    def test_generated_correctly_2(self):
        binaryAlphabet = Alphabet(
            frozenset([SymbolStr('0'), SymbolStr('1')]))
        generated_automata = generate_dfa(binaryAlphabet, 49)
        self._assert_correctness(generated_automata)

    def test_generated_correctly_3(self):
        abcdAlphabet = Alphabet(frozenset(
            [SymbolStr('a'), SymbolStr('b'), SymbolStr('c'), SymbolStr('d')]))
        generated_automata = generate_dfa(abcdAlphabet, 49)
        self._assert_correctness(generated_automata)

    def test_generated_correctly_4(self):
        alphabet012 = Alphabet(
            frozenset([SymbolStr('0'), SymbolStr('1'), SymbolStr('2')]))
        generated_automata = generate_dfa(alphabet012, 1)
        self._assert_correctness(generated_automata)

    def _assert_correctness(self, automaton):        
        self.assertTrue(self._all_states_are_rechable(automaton))

    def _all_states_are_rechable(self, automaton):
        unrechable = automaton.states.copy()
        for state in unrechable.copy():
            for destinations in state.transitions.values():
                unrechable = unrechable - destinations
        return len(unrechable) <= 1  # Hole

    def _has_final_state(self, automaton):
        return any(state.is_final for state in automaton.states)
