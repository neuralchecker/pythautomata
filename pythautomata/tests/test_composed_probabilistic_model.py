from unittest import TestCase

from pythautomata.automata_definitions.weighted_tomitas_grammars import WeightedTomitasGrammars
from pythautomata.other_models.composed_probabilistic_model import ComposedProbabilisticModel


class TestComposedProbabilisticModel(TestCase):

    def test_instantiate_composed_probabilistic_model_1(self):
        automata1 = WeightedTomitasGrammars.get_automaton_1()
        automata2 = WeightedTomitasGrammars.get_automaton_2()
        ComposedProbabilisticModel(
            [automata1, automata2], automata1.alphabet, lambda x, y: (x + y)/2)
        self.assertTrue(True)

    def test_instantiate_composed_probabilistic_model_exception(self):
        automata1 = WeightedTomitasGrammars.get_automaton_1()
        automata2 = WeightedTomitasGrammars.get_automaton_2()
        with self.assertRaises(TypeError):
            ComposedProbabilisticModel(
                [automata1, automata2], automata1.alphabet, lambda x, y, z: (x and not y or z))
