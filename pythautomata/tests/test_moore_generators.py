from unittest import TestCase
from pythautomata.utilities import nicaud_mm_generator
from pythautomata.utilities import simple_mm_generator
from pythautomata.base_types.alphabet import Alphabet
from pythautomata.base_types.symbol import SymbolStr

binaryAlphabet = Alphabet(
    frozenset([SymbolStr('0'), SymbolStr('1')]))

tripleAlphabet = Alphabet(
    frozenset([SymbolStr('a'), SymbolStr('b'), SymbolStr('c')]))


class TestMooreGenerators(TestCase):

    def test_simple_moore_generator_1(self):
        generated_moore = simple_mm_generator.generate_moore_machine(
            binaryAlphabet, tripleAlphabet, 80)
        self._assert_correctness(generated_moore)

    def test_simple_dfa_generator_1(self):
        generated_moore = simple_mm_generator.generate_moore_machine(
            binaryAlphabet, tripleAlphabet, 80)
        self._assert_correctness(generated_moore)

    def test_simple_dfa_generator_2(self):
        generated_moore = simple_mm_generator.generate_moore_machine(
            binaryAlphabet, tripleAlphabet, 49)
        self._assert_correctness(generated_moore)

    def test_simple_dfa_generator_3(self):
        generated_moore = simple_mm_generator.generate_moore_machine(
            binaryAlphabet, tripleAlphabet, 49)
        self._assert_correctness(generated_moore)

    def test_simple_dfa_generator_4(self):
        generated_moore = simple_mm_generator.generate_moore_machine(
            binaryAlphabet, tripleAlphabet, 1)
        self._assert_correctness(generated_moore)

    def test_nicaud_1(self):
        symbols = []
        for i in range(10):
            symbols.append(SymbolStr(str(i)))
        mediumAlphabet = Alphabet(frozenset(symbols))
        generated_moore = nicaud_mm_generator.generate_moore_machine(
            mediumAlphabet, tripleAlphabet, 1000)
        self._assert_correctness(generated_moore)

    def _assert_correctness(self, automaton):
        self.assertTrue(self._all_states_are_rechable(automaton))

    def _all_states_are_rechable(self, automaton):
        unrechable = automaton.states.copy()
        for state in unrechable.copy():
            for destinations in state.transitions.values():
                unrechable = unrechable - destinations
        return len(unrechable) <= 1  # Hole
