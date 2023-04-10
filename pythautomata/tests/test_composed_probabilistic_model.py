from unittest import TestCase

from pythautomata.automata_definitions.weighted_tomitas_grammars import WeightedTomitasGrammars
from pythautomata.other_models.composed_probabilistic_model import ComposedProbabilisticModel
from pythautomata.base_types.sequence import Sequence
from pythautomata.base_types.symbol import SymbolStr


class TestComposedProbabilisticModel(TestCase):

    def test_instantiate_composed_probabilistic_model_1(self):
        automata1 = WeightedTomitasGrammars.get_automaton_1()
        automata2 = WeightedTomitasGrammars.get_automaton_2()
        model = ComposedProbabilisticModel(
            [automata1, automata2], automata1.alphabet, lambda x, y: (x + y)/2)
        a = model.sequence_probability(
            Sequence([SymbolStr('0'), SymbolStr('1')]))
        b = model.last_token_probability(
            Sequence([SymbolStr('0'), SymbolStr('1')]))
        self.assertTrue(True)

    def test_instantiate_composed_probabilistic_model_exception(self):
        automata1 = WeightedTomitasGrammars.get_automaton_1()
        automata2 = WeightedTomitasGrammars.get_automaton_2()
        with self.assertRaises(TypeError):
            ComposedProbabilisticModel(
                [automata1, automata2], automata1.alphabet, lambda x, y, z: (x and not y or z))
