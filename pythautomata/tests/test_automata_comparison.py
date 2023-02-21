from itertools import chain
from unittest import TestCase

from pythautomata.automata.deterministic_finite_automaton import \
    DeterministicFiniteAutomaton as DFA
from pythautomata.automata.symbolic_finite_automaton import SymbolicFiniteAutomaton
from pythautomata.automata.wheighted_automaton_definition.probabilistic_deterministic_finite_automaton import \
    ProbabilisticDeterministicFiniteAutomaton
from pythautomata.automata.wheighted_automaton_definition.weighted_state import WeightedState
from pythautomata.automata_definitions.bollig_habermehl_kern_leucker_automata import \
    BolligHabermehlKernLeuckerAutomata
from pythautomata.automata_definitions.omlin_giles_automata import \
    OmlinGilesAutomata
from pythautomata.automata_definitions.other_automata import OtherAutomata
from pythautomata.automata_definitions.sample_mealy_machines import SampleMealyMachines
from pythautomata.automata_definitions.tomitas_grammars import TomitasGrammars
from pythautomata.automata_definitions.weighted_tomitas_grammars import WeightedTomitasGrammars
from pythautomata.base_types.alphabet import Alphabet
from pythautomata.base_types.symbol import SymbolStr
from pythautomata.base_types.symbolic_state import SymbolicState
from pythautomata.model_comparators.dfa_comparison_strategy import \
    DFAComparisonStrategy as DFAComparator
from pythautomata.model_comparators.random_walk_comparison_strategy import \
    RandomWalkComparisonStrategy
from pythautomata.model_comparators.hopcroft_karp_comparison_strategy import \
    HopcroftKarpComparisonStrategy as HopcroftKarpComparison
from pythautomata.model_comparators.random_walk_mm_comparison_strategy import RandomWalkMMComparisonStrategy
from pythautomata.utilities.automata_converter import AutomataConverter
from pythautomata.model_comparators.wfa_tolerance_comparison_strategy import WFAToleranceComparator
from pythautomata.model_comparators.wfa_quantization_comparison_strategy import WFAQuantizationComparator
from pythautomata.automata_definitions.sample_moore_machines import SampleMooreMachines


class TestAutomataComparison(TestCase):

    def test_equivalence_reflexiveness(self):
        mergedAutomata = list(chain(TomitasGrammars.get_all_automata(),
                                    OmlinGilesAutomata.get_all_automata(),
                                    OtherAutomata.get_all_automata()))
        for automaton in mergedAutomata:
            self.assertAreEquivalentFAs(automaton, automaton)

    def test_equivalence_minimized_automaton_1(self):
        automaton = OtherAutomata.get_automaton_1()
        minimized_automaton = OtherAutomata.get_automaton_1_minimized()
        self.assertAreEquivalentFAs(automaton, minimized_automaton)

    def test_equivalence_minimized_automaton_2(self):
        automaton = OtherAutomata.get_automaton_2()
        minimized_automaton = OtherAutomata.get_automaton_2_minimized()
        self.assertAreEquivalentFAs(automaton, minimized_automaton)

    def test_equivalence_minimized_automaton_3(self):
        automaton = OtherAutomata.get_automaton_3()
        minimized_automaton = OtherAutomata.get_automaton_3_minimized()
        self.assertAreEquivalentFAs(automaton, minimized_automaton)

    def test_equivalence_minimized_automaton_4(self):
        automaton = OtherAutomata.get_automaton_4()
        minimized_automaton = OtherAutomata.get_automaton_4_minimized()
        self.assertAreEquivalentFAs(automaton, minimized_automaton)

    def test_dfa_ndfa_equivalence_1(self):
        dfa = OtherAutomata.get_nfa_1()
        ndfa = OtherAutomata.get_dfa_1()
        self.assertAreEquivalentFAs(dfa, ndfa)

    def test_dfa_ndfa_equivalence_2(self):
        dfa = OtherAutomata.get_nfa_2()
        ndfa = OtherAutomata.get_dfa_2()
        self.assertAreEquivalentFAs(dfa, ndfa)

    def test_dfa_ndfa_equivalence_3(self):
        dfa = OtherAutomata.get_nfa_3()
        ndfa = OtherAutomata.get_dfa_3()
        self.assertAreEquivalentFAs(dfa, ndfa)

    def test_dfa_ndfa_equivalence_4(self):
        dfa = OtherAutomata.get_nfa_4()
        ndfa = OtherAutomata.get_dfa_4()
        self.assertAreEquivalentFAs(dfa, ndfa)

    def test_dfa_ndfa_equivalence_5(self):
        dfa = OtherAutomata.get_nfa_5()
        ndfa = OtherAutomata.get_dfa_5()
        self.assertAreEquivalentFAs(dfa, ndfa)

    def test_e_commerce_equivalent_to_itself(self):
        e_commerce_automata = OtherAutomata.get_reduced_ecommerce_automaton()
        self.assertAreEquivalentFAs(e_commerce_automata, e_commerce_automata)

    def test_e_commerce_equivalence_with_reduced_version(self):
        e_commerce_automata = OtherAutomata.get_reduced_ecommerce_automaton()
        reduced_e_commerce_automata = OtherAutomata.get_reduced_ecommerce_automaton()
        self.assertAreEquivalentFAs(
            e_commerce_automata, reduced_e_commerce_automata)

    def test_comparator_equivalency_when_different_1(self):
        automaton = OtherAutomata.get_nfa_1()
        nonEquivalentDfa = OtherAutomata.get_dfa_2()
        self.assertAreNotEquivalentFAs(automaton, nonEquivalentDfa)

    def test_comparator_equivalency_when_different_2(self):
        automaton = OtherAutomata.get_nfa_2()
        nonEquivalentDfa = OtherAutomata.get_dfa_1()
        self.assertAreNotEquivalentFAs(automaton, nonEquivalentDfa)

    def test_comparator_equivalency_through_counterexample(self):
        automaton = OtherAutomata.get_nfa_1()
        equivalentDfa = OtherAutomata.get_dfa_1()
        comparator = DFAComparator()
        automaton = AutomataConverter.convert_nfa_to_dfa(automaton)
        counterexample = comparator.get_counterexample_between(
            automaton, equivalentDfa)
        self.assertIsNone(counterexample)

    def test_comparator_returns_valid_counterexample(self):
        nfa = OtherAutomata.get_nfa_1()
        nonEquivalentDfa = OtherAutomata.get_dfa_2()
        transformedNfa = AutomataConverter.convert_nfa_to_dfa(nfa)
        comparator = DFAComparator()
        counterexample = comparator.get_counterexample_between(
            transformedNfa, nonEquivalentDfa)
        self.assertIsNotNone(counterexample)
        self.assertTrue(transformedNfa.accepts(counterexample) !=
                        nonEquivalentDfa.accepts(counterexample))

    def test_comparator_returns_valid_counterexample_2(self):
        ecommerce_automaton = OtherAutomata.get_ecommerce_automaton()
        different_ecommerce_automaton = OtherAutomata.get_different_ecommerce_automaton_NFA()
        different_ecommerce_automaton = AutomataConverter.convert_nfa_to_dfa(
            different_ecommerce_automaton)
        comparator = DFAComparator()
        counterexample = comparator.get_counterexample_between(
            ecommerce_automaton, different_ecommerce_automaton)
        self.assertIsNotNone(counterexample)
        self.assertTrue(ecommerce_automaton.accepts(counterexample) !=
                        different_ecommerce_automaton.accepts(counterexample))

    def test_nfa_learning_FAs(self):
        dfa = BolligHabermehlKernLeuckerAutomata.get_first_example_DFA()
        nfa = BolligHabermehlKernLeuckerAutomata.get_first_example_NFA()
        self.assertAreEquivalentFAs(dfa, nfa)
        self.assertAreEquivalentFAs(nfa, dfa)

    def _areEquivalentFAs(self, automaton1, automaton2):
        if type(automaton1) == DFA and type(automaton2) == DFA:
            comparator = DFAComparator()
        else:
            comparator = HopcroftKarpComparison()
        areEquivalent = comparator.are_equivalent(automaton1, automaton2)
        return areEquivalent

    def assertAreEquivalentFAs(self, automaton1, automaton2):
        assert (self._areEquivalentFAs(automaton1, automaton2))

    def assertAreNotEquivalentFAs(self, automaton1, automaton2):
        self.assertFalse(self._areEquivalentFAs(automaton1, automaton2))

    def test_wfa_equivalence_reflexiveness(self):
        weightedTomitasAutomata = WeightedTomitasGrammars.get_all_automata()
        comparator = WFAToleranceComparator()
        for wfa in weightedTomitasAutomata:
            assert (comparator.are_equivalent(wfa, wfa))

    def test_wfa_equivalence_false_case(self):
        weightedTomitasAutomata = WeightedTomitasGrammars.get_all_automata()
        comparator = WFAToleranceComparator()
        for i in range(len(weightedTomitasAutomata)):
            for j in range(len(weightedTomitasAutomata)):
                if i != j:
                    wfa1 = weightedTomitasAutomata[i]
                    wfa2 = weightedTomitasAutomata[j]
                    assert (not comparator.are_equivalent(wfa1, wfa2))

    def test_tomita4_vs_single_state_pdfa(self):
        weightedTomita4 = WeightedTomitasGrammars.get_automaton_4()
        from pythautomata.base_types.symbol import SymbolStr
        from pythautomata.base_types.alphabet import Alphabet
        from pythautomata.automata.wheighted_automaton_definition.weighted_state import WeightedState
        from pythautomata.automata.wheighted_automaton_definition.probabilistic_deterministic_finite_automaton import \
            ProbabilisticDeterministicFiniteAutomaton
        q0 = WeightedState("q0", 1, 0.05)
        binaryAlphabet = Alphabet(frozenset((SymbolStr('0'), SymbolStr('1'))))
        zero = binaryAlphabet['0']
        one = binaryAlphabet['1']
        q0.add_transition(zero, q0, 0.665)
        q0.add_transition(one, q0, 0.285)

        states = {q0}
        comparator = WFAToleranceComparator()
        single_state_wfa = ProbabilisticDeterministicFiniteAutomaton(
            binaryAlphabet, states, SymbolStr("$"), comparator, "WeightedTomitas4")
        counterexample = comparator.get_counterexample_between(
            weightedTomita4, single_state_wfa)
        assert (counterexample is not None)

    def test_wfa_quantization_equivalence_reflexiveness(self):
        weightedTomitasAutomata = WeightedTomitasGrammars.get_all_automata()
        comparator = WFAQuantizationComparator(100)
        for wfa in weightedTomitasAutomata:
            assert (comparator.are_equivalent(wfa, wfa))

    def test_wfa_quantization_equivalence_false_case(self):
        weightedTomitasAutomata = WeightedTomitasGrammars.get_all_automata()
        comparator = WFAQuantizationComparator(100)
        for i in range(len(weightedTomitasAutomata)):
            for j in range(len(weightedTomitasAutomata)):
                if i != j:
                    wfa1 = weightedTomitasAutomata[i]
                    wfa2 = weightedTomitasAutomata[j]
                    assert (not comparator.are_equivalent(wfa1, wfa2))

    def test_quantization_equivalence_tomita4_vs_single_state_pdfa(self):
        weightedTomita4 = WeightedTomitasGrammars.get_automaton_4()
        q0 = WeightedState("q0", 1, 0.05)
        binaryAlphabet = Alphabet(frozenset((SymbolStr('0'), SymbolStr('1'))))
        zero = binaryAlphabet['0']
        one = binaryAlphabet['1']
        q0.add_transition(zero, q0, 0.665)
        q0.add_transition(one, q0, 0.285)

        states = {q0}
        comparator = WFAQuantizationComparator(100)
        single_state_wfa = ProbabilisticDeterministicFiniteAutomaton(
            binaryAlphabet, states, SymbolStr("$"), comparator, "Single State PDFA")
        counterexample = comparator.get_counterexample_between(
            weightedTomita4, single_state_wfa)
        assert (counterexample is not None)

    def test_tomita1_vs_empty_sfa(self):
        tomita1 = TomitasGrammars.get_automaton_1()
        comparator = HopcroftKarpComparison()
        init_state = SymbolicState('', is_final=True)
        sfa = SymbolicFiniteAutomaton(
            Alphabet(frozenset()), init_state, {init_state})
        assert (not comparator.are_equivalent(tomita1, sfa))

    def test_equivalence_reflexiveness_random_walk(self):
        mergedAutomata = list(chain(TomitasGrammars.get_all_automata()))
        comparison_strategy1 = RandomWalkComparisonStrategy(1000, 0.01)
        comparison_strategy2 = RandomWalkComparisonStrategy(1000, 0.01)
        for i in range(len(mergedAutomata)):
            for j in range(len(mergedAutomata)):
                if i == j:
                    self.assertTrue(comparison_strategy1.are_equivalent(
                        mergedAutomata[i], mergedAutomata[j].clone()))
                else:
                    self.assertFalse(
                        comparison_strategy2.are_equivalent(mergedAutomata[i], mergedAutomata[j]))

    def test_equivalence_random_walk_for_mm(self):
        mergedAutomata = list(chain(SampleMooreMachines.get_all_automata()))
        mergedAutomata2 = list(chain(SampleMooreMachines.get_all_automata()))
        comparison_strategy = RandomWalkMMComparisonStrategy(1000, 0.01)

        for i in range(len(mergedAutomata)):
            for j in range(len(mergedAutomata2)):
                if i == j:
                    self.assertTrue(comparison_strategy.are_equivalent(
                        mergedAutomata[i], mergedAutomata2[j]))
                else:
                    try:
                        self.assertFalse(
                            comparison_strategy.are_equivalent(mergedAutomata[i], mergedAutomata2[j]))
                    except:
                        pass

    def test_are_equivalent_mealy(self):
        machine1 = SampleMealyMachines.get_3_states_mealy_machine()
        machine2 = SampleMealyMachines.get_3_states_mealy_machine()
        self.assertEqual(machine1, machine2)
