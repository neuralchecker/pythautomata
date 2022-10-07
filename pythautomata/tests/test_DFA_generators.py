from unittest import TestCase
from pythautomata.utilities import simple_dfa_generator
from pythautomata.utilities import abbadingo_one_dfa_generator
from pythautomata.utilities import nicaud_dfa_generator
from pythautomata.base_types.alphabet import Alphabet
from pythautomata.base_types.symbol import SymbolStr


class TestDFAGenerators(TestCase):

    def test_simple_dfa_generator_1(self):
        binaryAlphabet = Alphabet(
            frozenset([SymbolStr('0'), SymbolStr('1')]))
        generated_automata = simple_dfa_generator.generate_dfa(
            binaryAlphabet, 80)
        self._assert_correctness(generated_automata)

    def test_simple_dfa_generator_2(self):
        binaryAlphabet = Alphabet(
            frozenset([SymbolStr('0'), SymbolStr('1')]))
        generated_automata = simple_dfa_generator.generate_dfa(
            binaryAlphabet, 49)
        self._assert_correctness(generated_automata)

    def test_simple_dfa_generator_3(self):
        abcdAlphabet = Alphabet(frozenset(
            [SymbolStr('a'), SymbolStr('b'), SymbolStr('c'), SymbolStr('d')]))
        generated_automata = simple_dfa_generator.generate_dfa(
            abcdAlphabet, 49)
        self._assert_correctness(generated_automata)

    def test_simple_dfa_generator_4(self):
        alphabet012 = Alphabet(
            frozenset([SymbolStr('0'), SymbolStr('1'), SymbolStr('2')]))
        generated_automata = simple_dfa_generator.generate_dfa(alphabet012, 1)
        self._assert_correctness(generated_automata)

    def test_abbadingo_one_1_excep(self):
        alphabet012 = Alphabet(
            frozenset([SymbolStr('0'), SymbolStr('1'), SymbolStr('2')]))
        exc = AssertionError
        self.assertRaises(
            exc, abbadingo_one_dfa_generator.generate_dfa, alphabet012, 10)

    def test_abbadingo_one_1_ok(self):
        alphabet12 = Alphabet(
            frozenset([SymbolStr('1'), SymbolStr('2')]))
        generated_automata = abbadingo_one_dfa_generator.generate_dfa(
            alphabet12, 10)
        self._assert_correctness(generated_automata)

    def test_nicaud_1_ok(self):
        symbols = []
        for i in range(10):
            symbols.append(SymbolStr(str(i)))
        mediumAlphabet = Alphabet(frozenset(symbols))
        generated_automata = nicaud_dfa_generator.generate_dfa(
            mediumAlphabet, 1000)
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
