from unittest import TestCase

from pythautomata.automata_definitions.tomitas_grammars import TomitasGrammars
from pythautomata.other_models.composed_boolean_model import ComposedBooleanModel


class TestComposedBooleanModel(TestCase):

    def test_instantiate_composed_boolean_model_1(self):
        automata1 = TomitasGrammars.get_automaton_1()
        automata2 = TomitasGrammars.get_automaton_2()
        ComposedBooleanModel(
            [automata1, automata2], automata1.alphabet, lambda x, y: (x and not y))
        self.assertTrue(True)

    def test_instantiate_composed_boolean_model_exception(self):
        automata1 = TomitasGrammars.get_automaton_1()
        automata2 = TomitasGrammars.get_automaton_2()
        with self.assertRaises(TypeError):
            ComposedBooleanModel(
                [automata1, automata2], automata1.alphabet, lambda x, y, z: (x and not y or z))
