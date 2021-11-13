from unittest import TestCase

from pythautomata.abstract.finite_automaton import FiniteAutomaton
from pythautomata.automata_definitions.bollig_habermehl_kern_leucker_automata import BolligHabermehlKernLeuckerAutomata
from pythautomata.automata_definitions.omlin_giles_automata import OmlinGilesAutomata
from pythautomata.automata_definitions.other_automata import OtherAutomata
from pythautomata.automata_definitions.sample_nfas import SampleNFAs
from pythautomata.automata_definitions.tomitas_grammars_modifications import TomitasGrammarsMods
from pythautomata.automata_definitions.tomitas_grammars import TomitasGrammars
from pythautomata.automata_definitions.weighted_tomitas_grammars import WeightedTomitasGrammars

class TestAutomataDefinitions(TestCase):

    def test_instantiating_all_automata(self):
        automata1 =BolligHabermehlKernLeuckerAutomata.get_all_automata()
        automata2 =OmlinGilesAutomata.get_all_automata()
        automata3 =OtherAutomata.get_all_automata()
        automata4 =SampleNFAs.get_all_automata()
        automata5 =TomitasGrammarsMods.get_all_automata()
        automata6 =TomitasGrammars.get_all_automata()
        automata7 =WeightedTomitasGrammars.get_all_automata()

        self.assertTrue(True)