from unittest import TestLoader, TestSuite, TextTestRunner

from pythautomata.tests.test_minimizer import TestMinimizer
from pythautomata.tests.test_automata_convertor import TestAutomataConvertor
from pythautomata.tests.test_pdfa_generator import TestPDFAGenerator
from pythautomata.tests.test_pdfa_serialization import TestPDFASerialization
from pythautomata.tests.test_DFA_generators import TestDFAGenerators
from pythautomata.tests.test_automata_comparison import TestAutomataComparison
from pythautomata.tests.test_sequence import TestSequence
from pythautomata.tests.test_dfa_operations import TestDFAOperations
from pythautomata.tests.test_automata_definitions import TestAutomataDefinitions
from pythautomata.tests.test_regex_generator import TestRegexGenerator
from pythautomata.tests.test_pdfa_metrics import TestPDFAMetrics
from pythautomata.tests.test_simple_DFA_generator import TestSimpleDFAGenerator
from pythautomata.tests.test_pdfa_operations import TestPDFAOperations


def get_all_tests():
    return [TestSimpleDFAGenerator, TestPDFAGenerator, TestMinimizer, TestAutomataConvertor,
            TestDFAGenerators, TestAutomataComparison, TestSequence,
            TestDFAOperations, TestAutomataDefinitions, TestPDFAGenerator,
            TestRegexGenerator, TestPDFASerialization, TestPDFAMetrics, TestPDFAOperations]


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
