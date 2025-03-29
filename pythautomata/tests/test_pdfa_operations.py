from unittest import TestCase

from pythautomata.automata_definitions.weighted_tomitas_grammars import WeightedTomitasGrammars
from pythautomata.utilities.pdfa_operations import get_representative_sample, check_is_minimal, make_absorbent
from pythautomata.base_types.symbol import SymbolStr
from pythautomata.base_types.alphabet import Alphabet
from pythautomata.automata.wheighted_automaton_definition.probabilistic_deterministic_finite_automaton import \
    ProbabilisticDeterministicFiniteAutomaton as PDFA
from pythautomata.automata.wheighted_automaton_definition.weighted_state import WeightedState
from pythautomata.model_comparators.wfa_tolerance_comparison_strategy import WFAToleranceComparator
from pythautomata.utilities import nicaud_dfa_generator
from pythautomata.utilities.pdfa_generator import pdfa_from_dfa
binaryAlphabet = Alphabet(frozenset((SymbolStr('0'), SymbolStr('1'))))
zero = binaryAlphabet['0']
one = binaryAlphabet['1']

class TestPDFAOperations(TestCase):

    def test_1(self):
        pdfa = WeightedTomitasGrammars.get_automaton_1()
        sample = get_representative_sample(pdfa, 10)
        self.assertTrue(True)

    def test_2(self):
        pdfa = WeightedTomitasGrammars.get_automaton_2()
        sample = get_representative_sample(pdfa, 20)
        self.assertTrue(True)

    def test_3(self):
        pdfa = WeightedTomitasGrammars.get_automaton_3()
        sample = get_representative_sample(pdfa, 30)
        self.assertTrue(True)

    def test_4(self):
        pdfa = WeightedTomitasGrammars.get_automaton_4()
        sample = get_representative_sample(pdfa, 400)
        self.assertTrue(True)

    def test_5(self):
        pdfa = WeightedTomitasGrammars.get_automaton_5()
        sample = get_representative_sample(pdfa, 0)
        self.assertTrue(True)

    def test_6(self):
        pdfa = WeightedTomitasGrammars.get_automaton_6()
        sample = get_representative_sample(pdfa, 1)
        self.assertTrue(True)

    def test_7(self):
        pdfa = WeightedTomitasGrammars.get_automaton_7()
        self.assertRaises(AssertionError, get_representative_sample, pdfa, -1)
    
    def test_8(self):
        pdfa = WeightedTomitasGrammars.get_automaton_6()
        sample = get_representative_sample(pdfa, 100, 5)
        self.assertTrue(max([len(x) for x in sample])==5)
        self.assertTrue(True)

    def test_pdfa_is_minimal(self):
        for pdfa in WeightedTomitasGrammars.get_all_automata():            
            assert check_is_minimal(pdfa)

    def get_not_minimal_pdfa(self):
        """
        method with a non minimal specification of automaton 1 from the Tomita's Grammars      

        Returns
        -------
        ProbabilisticDeterministicFiniteAutomaton
            non minimal weighted tomita grammar 1
        """
        q0 = WeightedState("q0", 1, 0.05)
        q1 = WeightedState("q1", 0, 0.05)
        q2 = WeightedState("q2", 0, 0.05)
        q3 = WeightedState("q3", 0, 0.05)
        q4 = WeightedState("q4", 0, 0.05)
        q5 = WeightedState("q5", 0, 0.05)
        q6 = WeightedState("q6", 0, 0.05)

        q0.add_transition(zero, q1, 0.665)
        q0.add_transition(one, q0, 0.285)
        q1.add_transition(zero, q2, 0.285)
        q1.add_transition(one, q2, 0.665)
        q2.add_transition(zero, q3, 0.285)
        q2.add_transition(one, q3, 0.665)
        q3.add_transition(zero, q4, 0.285)
        q3.add_transition(one, q4, 0.665)
        q4.add_transition(zero, q5, 0.285)
        q4.add_transition(one, q5, 0.665)
        q5.add_transition(zero, q6, 0.285)
        q5.add_transition(one, q6, 0.665)
        q6.add_transition(zero, q1, 0.285)
        q6.add_transition(one, q1, 0.665)
        

        states = {q0, q1, q2, q3, q4, q5, q6}
        comparator = WFAToleranceComparator()
        return PDFA(binaryAlphabet, states, SymbolStr("$"), comparator, "WeightedTomitas1")

    def test_pdfa_is_not_minimal(self):
        assert not check_is_minimal(self.get_not_minimal_pdfa())

    def test_make_absorbent(self):
        symbols = []
        for i in range(5):
            symbols.append(SymbolStr(str(i)))
        mediumAlphabet = Alphabet(frozenset(symbols))
        generated_automata = nicaud_dfa_generator.generate_dfa(
            mediumAlphabet, 1000)
        dfa = generated_automata
        pdfa = pdfa_from_dfa(
            dfa, distributions=1000, max_shift=0.3, zero_probability=0.99)        
        pdfa2 = make_absorbent(pdfa)
        assert len(pdfa2.weighted_states) <= len(pdfa.weighted_states)+1