import pickle
from unittest import TestCase

from pythautomata.automata_definitions.tomitas_grammars import TomitasGrammars
from pythautomata.automata_definitions.weighted_tomitas_grammars import WeightedTomitasGrammars
from pythautomata.model_exporters.dot_exporters.dfa_dot_exporting_strategy import DfaDotExportingStrategy
from pythautomata.model_exporters.standard_exporters.dfa_standard_dot_exporting_strategy import DfaStandardDotExportingStrategy
from pythautomata.model_exporters.image_exporters.image_exporting_strategy import ImageExportingStrategy
from pythautomata.model_exporters.dot_exporters.dfa_dot_exporting_strategy import DfaDotExportingStrategy
from pythautomata.model_exporters.image_exporters.dfa_pdf_image_exporting_strategy_without_hole_state import ImageExportingStrategyWithoutHoleState


class TestDFAExporting(TestCase):

    def test_1(self):
        dfa = TomitasGrammars.get_automaton_1()
        name = dfa.name
        DfaDotExportingStrategy().export(dfa, "./output_models/tests")
        ImageExportingStrategy(DfaDotExportingStrategy(), "pdf").export(
            dfa, "./output_models/tests")
        dfa.name = name + "_standard"
        DfaStandardDotExportingStrategy().export(dfa, "./output_models/tests")
        dfa.name = name + "_no_hole"
        ImageExportingStrategyWithoutHoleState().export(dfa, "./output_models/tests")

    def test_2(self):
        dfa = TomitasGrammars.get_automaton_2()
        name = dfa.name
        DfaDotExportingStrategy().export(dfa, "./output_models/tests")
        ImageExportingStrategy(DfaDotExportingStrategy(), "pdf").export(
            dfa, "./output_models/tests")
        dfa.name = name + "_standard"
        DfaStandardDotExportingStrategy().export(dfa, "./output_models/tests")
        dfa.name = name + "_no_hole"
        ImageExportingStrategyWithoutHoleState().export(dfa, "./output_models/tests")

    def test_3(self):
        dfa = TomitasGrammars.get_automaton_3()
        name = dfa.name
        DfaDotExportingStrategy().export(dfa, "./output_models/tests")
        ImageExportingStrategy(DfaDotExportingStrategy(), "pdf").export(
            dfa, "./output_models/tests")
        dfa.name = name + "_standard"
        DfaStandardDotExportingStrategy().export(dfa, "./output_models/tests")
        dfa.name = name + "_no_hole"
        ImageExportingStrategyWithoutHoleState().export(dfa, "./output_models/tests")

    def test_4(self):
        dfa = TomitasGrammars.get_automaton_4()
        name = dfa.name
        DfaDotExportingStrategy().export(dfa, "./output_models/tests")
        ImageExportingStrategy(DfaDotExportingStrategy(), "pdf").export(
            dfa, "./output_models/tests")
        dfa.name = name + "_standard"
        DfaStandardDotExportingStrategy().export(dfa, "./output_models/tests")
        dfa.name = name + "_no_hole"
        ImageExportingStrategyWithoutHoleState().export(dfa, "./output_models/tests")

    def test_5(self):
        dfa = TomitasGrammars.get_automaton_5()
        name = dfa.name
        DfaDotExportingStrategy().export(dfa, "./output_models/tests")
        ImageExportingStrategy(DfaDotExportingStrategy(), "pdf").export(
            dfa, "./output_models/tests")
        dfa.name = name + "_standard"
        DfaStandardDotExportingStrategy().export(dfa, "./output_models/tests")
        dfa.name = name + "_no_hole"
        ImageExportingStrategyWithoutHoleState().export(dfa, "./output_models/tests")

    def test_6(self):
        dfa = TomitasGrammars.get_automaton_6()
        name = dfa.name
        DfaDotExportingStrategy().export(dfa, "./output_models/tests")
        ImageExportingStrategy(DfaDotExportingStrategy(), "pdf").export(
            dfa, "./output_models/tests")
        dfa.name = name + "_standard"
        DfaStandardDotExportingStrategy().export(dfa, "./output_models/tests")
        dfa.name = name + "_no_hole"
        ImageExportingStrategyWithoutHoleState().export(dfa, "./output_models/tests")

    def test_7(self):
        dfa = TomitasGrammars.get_automaton_7()
        name = dfa.name
        DfaDotExportingStrategy().export(dfa, "./output_models/tests")
        ImageExportingStrategy(DfaDotExportingStrategy(), "pdf").export(
            dfa, "./output_models/tests")
        dfa.name = name + "_standard"
        DfaStandardDotExportingStrategy().export(dfa, "./output_models/tests")
        dfa.name = name + "_no_hole"
        ImageExportingStrategyWithoutHoleState().export(dfa, "./output_models/tests")
