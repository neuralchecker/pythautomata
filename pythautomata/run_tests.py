from unittest import TestLoader, TestSuite, TextTestRunner
import os
import sys

from pythautomata.tests.test_minimizer import TestMinimizer
from pythautomata.tests.test_automata_convertor import TestAutomataConvertor
from pythautomata.tests.test_moore_machines_last_symbol_queries import TestMooreMachinesLastSymbolQueries
from pythautomata.tests.test_pdfa_generator import TestPDFAGenerator
from pythautomata.tests.test_pdfa_serialization import TestPDFASerialization
from pythautomata.tests.test_dfa_serialization import TestDFASerialization
from pythautomata.tests.test_dfa_generators import TestDFAGenerators
from pythautomata.tests.test_automata_comparison import TestAutomataComparison
from pythautomata.tests.test_sequence import TestSequence
from pythautomata.tests.test_dfa_operations import TestDFAOperations
from pythautomata.tests.test_automata_definitions import TestAutomataDefinitions
from pythautomata.tests.test_regex_generator import TestRegexGenerator
from pythautomata.tests.test_pdfa_metrics import TestPDFAMetrics
from pythautomata.tests.test_simple_DFA_generator import TestSimpleDFAGenerator
from pythautomata.tests.test_pdfa_operations import TestPDFAOperations
from pythautomata.tests.test_pdfa_last_token_queries import TestPDFALastTokenQueries
from pythautomata.tests.test_dfa_to_moore_machine import TestDFAToMooreMachine
from pythautomata.tests.test_dfa_exporting import TestDFAExporting
from pythautomata.tests.test_dfa_loading import TestDFALoading
from pythautomata.tests.test_probabilistic_filter_model import TestProbabilisticFilterModel
from pythautomata.tests.test_mm_exporting import TestMMExporting
from pythautomata.tests.test_mm_loading import TestMMLoading
from pythautomata.tests.test_mealy_exporting import TestMealyExporting
from pythautomata.tests.test_wfa_exporting import TestWFAExporting
from pythautomata.tests.test_mealy_loading import TestMealyLoading
from pythautomata.tests.test_composed_boolean_model import TestComposedBooleanModel
from pythautomata.tests.test_moore_generators import TestMooreGenerators
from pythautomata.tests.test_fast_pdfa_converter import TestFastPDFAConverter


def get_all_tests():
    return [TestDFALoading, TestDFAExporting, TestSimpleDFAGenerator, TestMinimizer,
            TestAutomataConvertor, TestDFAGenerators, TestAutomataComparison, TestSequence,
            TestDFAOperations, TestAutomataDefinitions, TestPDFAGenerator, TestRegexGenerator,
            TestPDFASerialization, TestDFASerialization, TestPDFAMetrics, TestPDFAOperations,
            TestPDFALastTokenQueries, TestMooreMachinesLastSymbolQueries, TestDFAToMooreMachine,
            TestMMLoading, TestMMExporting, TestProbabilisticFilterModel, TestMealyExporting, TestWFAExporting,
            TestMealyLoading, TestComposedBooleanModel, TestMooreGenerators, TestFastPDFAConverter]


def run():
    test_classes_to_run = get_all_tests()
    loader = TestLoader()
    suites_list = []
    for test_class in test_classes_to_run:
        suite = loader.loadTestsFromTestCase(test_class)
        suites_list.append(suite)
    meta_suite = TestSuite(suites_list)
    TextTestRunner().run(meta_suite)


if __name__ == '__main__':
    run()
