from unittest import TestCase
from pythautomata.utilities.regex_generator import RegularExpressionGenerator
from pythautomata.utilities.sequence_generator import SequenceGenerator
from pythautomata.base_types.alphabet import Alphabet
from pythautomata.base_types.symbol import SymbolStr

class TestRegexGenerator(TestCase):

    def test_generated_correctly_1(self):
        binaryAlphabet = Alphabet(
            frozenset([SymbolStr('0'), SymbolStr('1')]))            
        generator = RegularExpressionGenerator(alphabet=binaryAlphabet)

        generated_regex = generator.generate_regular_expression_with(iterations = 10)
        self._assert_correctness(generated_regex, binaryAlphabet)
    
    def test_generated_correctly_2(self):
        symbols = []
        for i in range(20):
            symbols.append(SymbolStr(str(i)))
        bigAlphabet = Alphabet(frozenset(symbols))            
        generator = RegularExpressionGenerator(alphabet=bigAlphabet)
        generated_regex = generator.generate_regular_expression_with(iterations = 100)
        self._assert_correctness(generated_regex, bigAlphabet)

    
    def _assert_correctness(self, regex, alphabet):       
        sequence_generator = SequenceGenerator(alphabet, 100)
        for i in range(1,100):
            seq = sequence_generator.generate_word(i)
            regex.accepts(seq) 
            self.assertTrue(True)

