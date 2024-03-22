from unittest import TestCase
from pythautomata.base_types.symbol import SymbolStr
from pythautomata.base_types.alphabet import Alphabet
from pythautomata.base_types.sequence import Sequence
from pythautomata.utilities.uniform_length_sequence_generator import UniformLengthSequenceGenerator
from pythautomata.utilities.uniform_word_sequence_generator import UniformWordSequenceGenerator
from pythautomata.utilities.guiding_wfa_sequence_generator import GuidingWDFASequenceGenerator
from pythautomata.utilities.guiding_pdfa_sequence_generator import GuidingPDFASequenceGenerator
from pythautomata.automata_definitions.weighted_tomitas_grammars import WeightedTomitasGrammars
abcAlphabet = Alphabet(frozenset(
    [SymbolStr('a'), SymbolStr('b'), SymbolStr('c')]))


class TestSequenceGenerator(TestCase):

    def test_sequence_generator(self):
        guide = WeightedTomitasGrammars().get_automaton_1()
        uniformLengthGenerator = UniformLengthSequenceGenerator(abcAlphabet, 10, 30, 0)
        uniformWordGenerator = UniformWordSequenceGenerator(abcAlphabet, 10, 30, 0)
        gudingWDFAGenerator = GuidingWDFASequenceGenerator(guide, 10, 30, 0.3)
        gudingPDFAGenerator = GuidingPDFASequenceGenerator(guide, 10, 30, 0.3)
        generators = [uniformLengthGenerator, uniformWordGenerator, gudingWDFAGenerator, gudingPDFAGenerator] 
        for generator in generators:
            generator.generate_words(100)