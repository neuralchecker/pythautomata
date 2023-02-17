import pickle
from unittest import TestCase

from pythautomata.automata_definitions.tomitas_grammars import TomitasGrammars
from pythautomata.automata_definitions.weighted_tomitas_grammars import WeightedTomitasGrammars
from pythautomata.model_exporters.dot_exporting_strategy import DotExportingStrategy
from pythautomata.model_exporters.standard_dot_exporting_strategy import StandardDotExportingStrategy
from pythautomata.model_exporters.image_exporting_strategy import ImageExportingStrategy
from pythautomata.model_exporters.image_exporting_strategy_without_hole_state import ImageExportingStrategyWithoutHoleState
from pythautomata.model_exporters.wfa_image_exporter import WFAImageExporter
from pythautomata.base_types.sequence import Sequence


class TestDFAExporting(TestCase):

    def test_1(self):
        dfa = TomitasGrammars.get_automaton_1()
        name = dfa.name
        DotExportingStrategy().export(dfa, "./output_models/tests")
        ImageExportingStrategy().export(dfa, "./output_models/tests")
        dfa.name = name + "_standard"
        StandardDotExportingStrategy().export(dfa, "./output_models/tests")
        dfa.name = name + "_no_hole"
        ImageExportingStrategyWithoutHoleState().export(dfa, "./output_models/tests")

    def test_2(self):
        dfa = TomitasGrammars.get_automaton_2()
        name = dfa.name
        DotExportingStrategy().export(dfa, "./output_models/tests")
        ImageExportingStrategy().export(dfa, "./output_models/tests")
        dfa.name = name + "_standard"
        StandardDotExportingStrategy().export(dfa, "./output_models/tests")
        dfa.name = name + "_no_hole"
        ImageExportingStrategyWithoutHoleState().export(dfa, "./output_models/tests")

    def test_3(self):
        dfa = TomitasGrammars.get_automaton_3()
        name = dfa.name
        DotExportingStrategy().export(dfa, "./output_models/tests")
        ImageExportingStrategy().export(dfa, "./output_models/tests")
        dfa.name = name + "_standard"
        StandardDotExportingStrategy().export(dfa, "./output_models/tests")
        dfa.name = name + "_no_hole"
        ImageExportingStrategyWithoutHoleState().export(dfa, "./output_models/tests")

    def test_4(self):
        dfa = TomitasGrammars.get_automaton_4()
        name = dfa.name
        DotExportingStrategy().export(dfa, "./output_models/tests")
        ImageExportingStrategy().export(dfa, "./output_models/tests")
        dfa.name = name + "_standard"
        StandardDotExportingStrategy().export(dfa, "./output_models/tests")
        dfa.name = name + "_no_hole"
        ImageExportingStrategyWithoutHoleState().export(dfa, "./output_models/tests")

    def test_5(self):
        dfa = TomitasGrammars.get_automaton_5()
        name = dfa.name
        DotExportingStrategy().export(dfa, "./output_models/tests")
        ImageExportingStrategy().export(dfa, "./output_models/tests")
        dfa.name = name + "_standard"
        StandardDotExportingStrategy().export(dfa, "./output_models/tests")
        dfa.name = name + "_no_hole"
        ImageExportingStrategyWithoutHoleState().export(dfa, "./output_models/tests")

    def test_6(self):
        dfa = TomitasGrammars.get_automaton_6()
        name = dfa.name
        DotExportingStrategy().export(dfa, "./output_models/tests")
        ImageExportingStrategy().export(dfa, "./output_models/tests")
        dfa.name = name + "_standard"
        StandardDotExportingStrategy().export(dfa, "./output_models/tests")
        dfa.name = name + "_no_hole"
        ImageExportingStrategyWithoutHoleState().export(dfa, "./output_models/tests")

    def test_7(self):
        dfa = TomitasGrammars.get_automaton_7()
        name = dfa.name
        DotExportingStrategy().export(dfa, "./output_models/tests")
        ImageExportingStrategy().export(dfa, "./output_models/tests")
        dfa.name = name + "_standard"
        StandardDotExportingStrategy().export(dfa, "./output_models/tests")
        dfa.name = name + "_no_hole"
        ImageExportingStrategyWithoutHoleState().export(dfa, "./output_models/tests")

    def test_8(self):
        wfa = WeightedTomitasGrammars.get_automaton_7()
        WFAImageExporter().export(wfa, "./output_models/tests")
