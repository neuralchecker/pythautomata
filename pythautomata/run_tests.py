from unittest import TestLoader, TestSuite, TextTestRunner


from tests.test_minimizer import TestMinimizer
from tests.test_automata_convertor import TestAutomataConvertor
from tests.test_simple_dfa_generator import TestSimpleDFAGenerator
from tests.test_automata_comparison import TestAutomataComparison
from tests.test_sequence import TestSequence
from tests.test_dfa_operations import TestDFAOperations

def run():
    test_classes_to_run = [TestMinimizer, TestAutomataConvertor, TestSimpleDFAGenerator, TestAutomataComparison, TestSequence, TestDFAOperations]
    loader = TestLoader()
    suites_list = []
    for test_class in test_classes_to_run:
        suite = loader.loadTestsFromTestCase(test_class)
        suites_list.append(suite)
    meta_suite = TestSuite(suites_list)
    TextTestRunner().run(meta_suite)


if __name__ == '__main__':
    run()
