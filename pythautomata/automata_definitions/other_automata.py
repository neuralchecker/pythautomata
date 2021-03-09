from base_types.state import State
from base_types.symbol import SymbolStr
from base_types.alphabet import Alphabet
from automata.deterministic_finite_automaton import DeterministicFiniteAutomaton as DFA
from automata.non_deterministic_finite_automaton import NondeterministicFiniteAutomaton as NFA
from model_comparators.nfa_hopcroft_karp_comparison_strategy import NFAHopcroftKarpComparisonStrategy as NFAComparator
from model_comparators.dfa_comparison_strategy import DFAComparisonStrategy as DFAComparator

binaryAlphabet = Alphabet(frozenset((SymbolStr('0'), SymbolStr('1'))))
zero = binaryAlphabet['0']
one = binaryAlphabet['1']

abAlphabet = Alphabet(frozenset((SymbolStr('a'), SymbolStr('b'))))
abcAlphabet = Alphabet(
    frozenset((SymbolStr('a'), SymbolStr('b'), SymbolStr('c'))))
a = abcAlphabet['a']
b = abcAlphabet['b']
c = abcAlphabet['c']

abcdAlphabet = Alphabet(frozenset((SymbolStr('a'), SymbolStr('b'),
                                   SymbolStr('c'), SymbolStr('d'))))

abcdeAlphabet = Alphabet(
    frozenset((a, b, c, SymbolStr('d'), SymbolStr('e'))))
d = abcdeAlphabet['d']
e = abcdeAlphabet['e']

#TODO: DOCUMENT
class OtherAutomata:

    @staticmethod
    def get_all_automata():
        return [
            OtherAutomata.get_automaton_1(),
            OtherAutomata.get_automaton_1_minimized(),
            OtherAutomata.get_automaton_2(),
            OtherAutomata.get_automaton_2_minimized(),
            OtherAutomata.get_automaton_3(),
            OtherAutomata.get_automaton_3_minimized(),
            OtherAutomata.get_automaton_4(),
            OtherAutomata.get_automaton_4_minimized(),
            OtherAutomata.get_non_minimizable_automaton_1(),
            OtherAutomata.get_non_minimizable_automaton_2(),
            OtherAutomata.get_non_minimizable_automaton_3(),
            OtherAutomata.get_dfa_1(),
            OtherAutomata.get_nfa_1(),
            OtherAutomata.get_dfa_2(),
            OtherAutomata.get_nfa_2(),
            OtherAutomata.get_dfa_3(),
            OtherAutomata.get_nfa_3(),
            OtherAutomata.get_dfa_4(),
            OtherAutomata.get_nfa_4(),
            OtherAutomata.get_dfa_5(),
            OtherAutomata.get_nfa_5(),
            OtherAutomata.get_program_workflow_automaton(),
            OtherAutomata.get_ecommerce_automaton(),
            OtherAutomata.get_reduced_ecommerce_automaton(),
            OtherAutomata.get_dolzhenko_jonoska_automaton(),
            OtherAutomata.get_a_or_b_automaton(),
            OtherAutomata.get_ab_with_cs_automaton(),
            OtherAutomata.get_ab_automaton(),
            OtherAutomata.get_a_ending_automaton(),
            OtherAutomata.get_a_ending_with_cs_automaton(),
            OtherAutomata.get_zero_ending_automaton(),
            OtherAutomata.get_nonempty_zero_ending_automaton(),
            OtherAutomata.get_nonempty_one_ending_automaton(),
            OtherAutomata.get_simpler_ab_prefixed_automaton(),
            OtherAutomata.get_complex_ab_prefixed_automaton(),
            OtherAutomata.get_alternating_bit_protocol_automaton(),
            OtherAutomata.get_alternating_bit_protocol_z_automaton(),
            OtherAutomata.get_empty_automaton(),
            OtherAutomata.get_sigma_star_automaton(),
            OtherAutomata.get_uneven_number_of_as_automaton(),
            OtherAutomata.get_uneven_number_of_symbols_automaton(),
            OtherAutomata.get_uneven_number_of_as_and_symbols_automaton(),
            OtherAutomata.get_uneven_number_of_as_or_symbols_automaton()
        ]

    @staticmethod
    def get_automaton_1():
        state0 = State("State 0")
        state1 = State("State 1", True)
        state2 = State("State 2", True)
        state3 = State("State 3")
        state4 = State("State 4", True)
        state5 = State("State 5")

        state0.add_transition(zero, state3)
        state0.add_transition(one, state1)
        state1.add_transition(zero, state2)
        state1.add_transition(one, state5)
        state2.add_transition(zero, state2)
        state2.add_transition(one, state5)
        state3.add_transition(zero, state0)
        state3.add_transition(one, state4)
        state4.add_transition(zero, state2)
        state4.add_transition(one, state5)
        state5.add_transition(zero, state5)
        state5.add_transition(one, state5)
        comparator = DFAComparator()
        return DFA(binaryAlphabet, state0,
                               set([state0, state1, state2, state3,
                                    state4, state5]), comparator, "Automaton 1")

    @staticmethod
    def get_automaton_1_minimized():
        state0 = State("Part 0")
        state1 = State("Part 1", True)
        state2 = State("Part 2")
        state0.add_transition(zero, state0)
        state0.add_transition(one, state1)
        state1.add_transition(zero, state1)
        state1.add_transition(one, state2)
        state2.add_transition(zero, state2)
        state2.add_transition(one, state2)
        comparator = DFAComparator()
        return DFA(binaryAlphabet, state0,
                               set([state0, state1, state2]), comparator, "Automaton 1 minimized")

    @staticmethod
    def get_automaton_2():
        state0 = State("State 0")
        state1 = State("State 1")
        state2 = State("State 2", True)
        state3 = State("State 3")
        state0.add_transition(zero, state3)
        state0.add_transition(one, state1)
        state1.add_transition(zero, state2)
        state3.add_transition(zero, state2)
        comparator = DFAComparator()
        return DFA(binaryAlphabet, state0,
                               set([state0, state1, state2, state3]), comparator, "Automaton 2")

    @staticmethod
    def get_automaton_2_minimized():
        state0 = State("State 0")
        state1_and_state3 = State("State 1 and 3")
        state2 = State("State 2", True)
        state0.add_transition(zero, state1_and_state3)
        state0.add_transition(one, state1_and_state3)
        state1_and_state3.add_transition(zero, state2)
        comparator = DFAComparator()
        return DFA(binaryAlphabet, state0,
                               set([state0, state1_and_state3, state2]), comparator, "Automaton 2 minimized")

    @staticmethod
    def get_automaton_3():
        state1 = State("State 1", True)
        state2 = State("State 2", True)
        state3 = State("State 3", True)
        state4 = State("State 4")
        state5 = State("State 5")
        state6 = State("State 6")
        state7 = State("State 7")

        state1.add_transition(zero, state3)
        state1.add_transition(one, state2)
        state2.add_transition(zero, state3)
        state2.add_transition(one, state1)
        state3.add_transition(zero, state4)
        state3.add_transition(one, state2)
        state4.add_transition(one, state5)
        state5.add_transition(zero, state7)
        state5.add_transition(one, state6)
        state6.add_transition(one, state3)
        state7.add_transition(zero, state6)
        state7.add_transition(one, state6)
        comparator = DFAComparator()
        return DFA(binaryAlphabet, state1,
                               set([state1, state2, state3, state4, state5,
                                    state6, state7]), comparator, "Automaton 3")

    @staticmethod
    def get_automaton_3_minimized():
        state1_and_state2 = State("State 1 and State 2", True)
        state3 = State("State 3", True)
        state4 = State("State 4")
        state5 = State("State 5")
        state6 = State("State 6")
        state7 = State("State 7")

        state1_and_state2.add_transition(zero, state3)
        state1_and_state2.add_transition(one, state1_and_state2)
        state3.add_transition(zero, state4)
        state3.add_transition(one, state1_and_state2)
        state4.add_transition(one, state5)
        state5.add_transition(zero, state7)
        state5.add_transition(one, state6)
        state6.add_transition(one, state3)
        state7.add_transition(zero, state6)
        state7.add_transition(one, state6)
        comparator = DFAComparator()
        return DFA(binaryAlphabet, state1_and_state2,
                               set([state1_and_state2, state3, state4, state5,
                                    state6, state7]), comparator, "Automaton 3 minimized")

    @staticmethod
    def get_automaton_4():
        state_i = State("State i", True)
        state_d = State("State d")
        state_c = State("State c", True)
        state_a = State("State a")
        state_b = State("State b")
        state_g = State("State g")
        state_e = State("State e")
        state_h = State("State h")
        state_f = State("State f")

        state_i.add_transition(zero, state_i)
        state_i.add_transition(one, state_d)
        state_d.add_transition(zero, state_c)
        state_d.add_transition(one, state_e)
        state_c.add_transition(zero, state_a)
        state_c.add_transition(one, state_c)
        state_a.add_transition(zero, state_b)
        state_a.add_transition(one, state_f)
        state_b.add_transition(zero, state_g)
        state_b.add_transition(one, state_c)
        state_g.add_transition(zero, state_g)
        state_g.add_transition(one, state_e)
        state_e.add_transition(zero, state_h)
        state_e.add_transition(one, state_f)
        state_h.add_transition(zero, state_c)
        state_h.add_transition(one, state_g)
        state_f.add_transition(zero, state_c)
        state_f.add_transition(one, state_g)
        comparator = DFAComparator()
        return DFA(binaryAlphabet, state_i,
                               set([state_i, state_d, state_c, state_a, state_b,
                                    state_g, state_e, state_h, state_f]), comparator, 
                                    "Automaton 4")

    @staticmethod
    def get_automaton_4_minimized():
        state_i = State("State i", True)
        state_d = State("State d")
        state_c = State("State c", True)
        state_a = State("State a")
        state_b = State("State b")
        state_g = State("State g")
        state_e = State("State e")
        state_h_and_f = State("State h and f")

        state_i.add_transition(zero, state_i)
        state_i.add_transition(one, state_d)
        state_d.add_transition(zero, state_c)
        state_d.add_transition(one, state_e)
        state_c.add_transition(zero, state_a)
        state_c.add_transition(one, state_c)
        state_a.add_transition(zero, state_b)
        state_a.add_transition(one, state_h_and_f)
        state_b.add_transition(zero, state_g)
        state_b.add_transition(one, state_c)
        state_g.add_transition(zero, state_g)
        state_g.add_transition(one, state_e)
        state_e.add_transition(zero, state_h_and_f)
        state_e.add_transition(one, state_h_and_f)
        state_h_and_f.add_transition(zero, state_c)
        state_h_and_f.add_transition(one, state_g)
        comparator = DFAComparator()
        return DFA(binaryAlphabet, state_i,
                               set([state_i, state_d, state_c, state_a, state_b, state_g,
                                    state_e, state_h_and_f]), comparator, "Automaton 4 minimized")

    @staticmethod
    def get_non_minimizable_automaton_1():
        state0 = State("State 0", True)
        state1 = State("State 1")
        state2 = State("State 2")
        state3 = State("State 3")

        state0.add_transition(zero, state1)
        state0.add_transition(one, state1)
        state1.add_transition(zero, state2)
        state1.add_transition(one, state0)
        state2.add_transition(zero, state1)
        state2.add_transition(one, state3)
        state3.add_transition(zero, state0)
        state3.add_transition(one, state1)
        comparator = DFAComparator()
        return DFA(binaryAlphabet, state0,
                               set([state0, state1, state2, state3]), comparator, "Non-minimizable automaton 1")

    @staticmethod
    def get_non_minimizable_automaton_2():
        state0 = State("State 0")
        state1 = State("State 1", True)
        state0.add_transition(zero, state1)
        state0.add_transition(one, state1)
        state1.add_transition(zero, state0)
        state1.add_transition(one, state0)
        comparator = DFAComparator()
        return DFA(binaryAlphabet, state0,
                               set([state0, state1]), comparator, "Non-minimizable automaton 2")

    @staticmethod
    def get_non_minimizable_automaton_3():
        state0 = State("State 0")
        state1 = State("State 1", True)
        state2 = State("State 2")
        state0.add_transition(zero, state1)
        state0.add_transition(one, state2)
        state1.add_transition(zero, state1)
        state1.add_transition(one, state1)
        state2.add_transition(one, state0)
        comparator = DFAComparator()
        return DFA(binaryAlphabet, state0,
                               set([state0, state1, state2]), comparator, "Non-minimizable automaton 3")

    @staticmethod
    def get_nfa_1():
        state0 = State("State 0")
        state1 = State("State 1")
        state2 = State("State 2", True)
        state0.add_transition(zero, state0)
        state0.add_transition(zero, state1)
        state0.add_transition(one, state0)
        state1.add_transition(one, state2)
        comparator = NFAComparator()
        return NFA(binaryAlphabet, frozenset({state0}),
                               set([state0, state1, state2]), comparator, "NFA 1")

    @staticmethod
    def get_dfa_1():
        state0 = State("State 0")
        state0_1 = State("State 0, 1")
        state0_2 = State("State 0, 2", True)
        state0.add_transition(zero, state0_1)
        state0.add_transition(one, state0)
        state0_1.add_transition(zero, state0_1)
        state0_1.add_transition(one, state0_2)
        state0_2.add_transition(zero, state0_1)
        state0_2.add_transition(one, state0)
        comparator = DFAComparator()
        return DFA(binaryAlphabet, state0,
                               set([state0, state0_1, state0_2]), comparator, "DFA 1")

    @staticmethod
    def get_nfa_2():
        state0 = State("State 0")
        state1 = State("State 1")
        state2 = State("State 2", True)
        state0.add_transition(zero, state0)
        state0.add_transition(one, state1)
        state1.add_transition(zero, state1)
        state1.add_transition(zero, state2)
        state1.add_transition(one, state1)
        state2.add_transition(zero, state2)
        state2.add_transition(zero, state1)
        state2.add_transition(one, state2)
        comparator = NFAComparator()
        return NFA(binaryAlphabet, frozenset({state0}),
                               set([state0, state1, state2]), comparator, "NFA 2")

    @staticmethod
    def get_dfa_2():
        state0 = State("State 0")
        state1 = State("State 1")
        state1_2 = State("State 1, 2", True)
        state0.add_transition(zero, state0)
        state0.add_transition(one, state1)
        state1.add_transition(zero, state1_2)
        state1.add_transition(one, state1)
        state1_2.add_transition(zero, state1_2)
        state1_2.add_transition(one, state1_2)
        comparator = DFAComparator()
        return DFA(binaryAlphabet, state0,
                               set([state0, state1, state1_2]), comparator, "DFA 2")

    @staticmethod
    def get_nfa_3():
        state0 = State("State 0")
        state1 = State("State 1", True)
        state0.add_transition(zero, state0)
        state0.add_transition(zero, state1)
        state0.add_transition(one, state1)
        state1.add_transition(one, state0)
        state1.add_transition(one, state1)
        comparator = NFAComparator()
        return NFA(binaryAlphabet, frozenset({state0}),
                               set([state0, state1]), comparator, "NFA 3")

    @staticmethod
    def get_dfa_3():
        state0 = State("State 0")
        state1 = State("State 1", True,)
        state0_1 = State("State 0, 1", True)
        state0.add_transition(zero, state0_1)
        state0.add_transition(one, state1)
        state1.add_transition(one, state0_1)
        state0_1.add_transition(zero, state0_1)
        state0_1.add_transition(one, state0_1)
        comparator = DFAComparator()
        return DFA(binaryAlphabet, state0,
                               set([state0, state1, state0_1]), comparator, "DFA 3")

    @staticmethod
    def get_nfa_4():
        state0 = State("State 0")
        state1 = State("State 1")
        state2 = State("State 2")
        state3 = State("State 3")
        state4 = State("State 4", True)
        state5 = State("State 5")
        state6 = State("State 6", True)

        state0.add_transition(a, state0)
        state0.add_transition(a, state1)
        state0.add_transition(b, state2)
        state0.add_transition(c, state4)
        state1.add_transition(a, state4)
        state1.add_transition(a, state3)
        state1.add_transition(b, state1)
        state1.add_transition(c, state2)
        state3.add_transition(a, state3)
        state3.add_transition(a, state5)
        state5.add_transition(b, state6)
        state5.add_transition(b, state4)

        comparator = NFAComparator()
        return NFA(abcAlphabet, frozenset({state0}),
                               set([state0, state1, state2, state3,
                                    state4, state5, state6]), comparator, "NFA 4")

    @staticmethod
    def get_dfa_4():
        state1 = State("State 1")
        state4 = State("State 4", True)
        state2 = State("State 2")
        state4_3 = State("State 4, 3", True)
        state0 = State("State 0")
        state4_6 = State("State 4, 6", True)
        state3_5 = State("State 3, 5")
        state2_1 = State("State 2, 1")
        state2_4_6_1 = State("State 2, 4, 6, 1", True)
        state1_0 = State("State 1, 0")
        state4_3_1_0 = State("State 4, 3, 1, 0", True)
        state5_3_4_1_0 = State("State 5, 3, 4, 1, 0", True)
        state2_4 = State("State 2, 4", True)

        state1.add_transition(a, state4_3)
        state1.add_transition(b, state1)
        state1.add_transition(c, state2)

        state4_3.add_transition(a, state3_5)

        state0.add_transition(a, state1_0)
        state0.add_transition(b, state2)
        state0.add_transition(c, state4)

        state3_5.add_transition(a, state3_5)
        state3_5.add_transition(b, state4_6)

        state2_1.add_transition(a, state4_3)
        state2_1.add_transition(b, state1)
        state2_1.add_transition(c, state2)

        state2_4_6_1.add_transition(a, state4_3)
        state2_4_6_1.add_transition(b, state1)
        state2_4_6_1.add_transition(c, state2)

        state1_0.add_transition(a, state4_3_1_0)
        state1_0.add_transition(b, state2_1)
        state1_0.add_transition(c, state2_4)

        state4_3_1_0.add_transition(a, state5_3_4_1_0)
        state4_3_1_0.add_transition(b, state2_1)
        state4_3_1_0.add_transition(c, state2_4)

        state5_3_4_1_0.add_transition(a, state5_3_4_1_0)
        state5_3_4_1_0.add_transition(b, state2_4_6_1)
        state5_3_4_1_0.add_transition(c, state2_4)

        comparator = DFAComparator()
        return DFA(abcAlphabet, state0,
                               set([state1, state4, state2, state4_3,
                                    state0, state4_6, state3_5, state2_1,
                                    state2_4_6_1, state1_0, state4_3_1_0,
                                    state5_3_4_1_0, state2_4]), comparator, "DFA 4")

    @staticmethod
    def get_nfa_5():
        state0 = State("State 0")
        state1 = State("State 1")
        state2 = State("State 2", True)
        state0.add_transition(a, state1)
        state0.add_transition(a, state2)
        state0.add_transition(b, state0)
        state0.add_transition(d, state0)
        state1.add_transition(a, state0)
        state1.add_transition(c, state2)
        state1.add_transition(d, state2)
        state1.add_transition(e, state1)
        state2.add_transition(d, state2)
        comparator = NFAComparator()
        return NFA(abcdeAlphabet, frozenset({state0}),
                               set([state0, state1, state2]), comparator, "NFA 5")

    @staticmethod
    def get_dfa_5():
        state0 = State("State 0")
        state1 = State("State 1")
        state2 = State("State 2", True)
        state1_2 = State("State 1, 2", True)
        state0.add_transition(a, state1_2)
        state0.add_transition(b, state0)
        state0.add_transition(d, state0)
        state1.add_transition(a, state0)
        state1.add_transition(c, state2)
        state1.add_transition(d, state2)
        state1.add_transition(e, state1)
        state2.add_transition(d, state2)
        state1_2.add_transition(a, state0)
        state1_2.add_transition(c, state2)
        state1_2.add_transition(d, state2)
        state1_2.add_transition(e, state1)
        comparator = DFAComparator()
        return DFA(abcdeAlphabet, state0,
                               set([state0, state1, state2, state1_2]), comparator, "DFA 5")

    # Definition: Recognizes a program workflow.
    @staticmethod
    def get_program_workflow_automaton():
        stateA = State("State A")
        stateB = State("State B", True)
        stateA.add_transition(zero, stateA)
        stateA.add_transition(one, stateB)
        stateB.add_transition(zero, stateA)
        stateB.add_transition(one, stateB)
        comparator = DFAComparator()
        return DFA(binaryAlphabet, stateA,
                               set([stateA, stateB]), comparator, "Program workflow automaton")

    # Definition: Recognizes e-commerce(taken from:
    # https://pdfs.semanticscholar.org/9cb9/74b6ece3e3fc2eab4f9cf0843bfc570df4a9.pdf).
    @staticmethod
    def get_ecommerce_automaton():
        alphabet = Alphabet(frozenset((SymbolStr('a'), SymbolStr('b'), SymbolStr(
            'c'), SymbolStr('d'), SymbolStr('e'), SymbolStr('f'), SymbolStr('g'), SymbolStr('h'))))
        a = alphabet['a']
        b = alphabet['b']
        c = alphabet['c']
        d = alphabet['d']
        e = alphabet['e']
        f = alphabet['f']
        g = alphabet['g']
        h = alphabet['h']
        state0 = State("State 0", True)
        state1 = State("State 1", True)
        state2 = State("State 2", True)
        state3 = State("State 3", True)
        state4 = State("State 4", True)
        state5 = State("State 5", True)
        state6 = State("State 6", True)
        state7 = State("State 7", True)
        state0.add_transition(a, state2)
        state0.add_transition(c, state1)
        state1.add_transition(a, state3)
        state1.add_transition(c, state1)
        state2.add_transition(c, state3)
        state2.add_transition(b, state0)
        state2.add_transition(a, state2)
        state2.add_transition(d, state2)
        state2.add_transition(e, state2)
        state3.add_transition(a, state3)
        state3.add_transition(c, state3)
        state3.add_transition(d, state3)
        state3.add_transition(e, state3)
        state3.add_transition(b, state1)
        state3.add_transition(f, state4)
        state4.add_transition(b, state1)
        state4.add_transition(h, state3)
        state4.add_transition(d, state3)
        state4.add_transition(a, state3)
        state4.add_transition(f, state4)
        state4.add_transition(c, state4)
        state4.add_transition(e, state5)
        state5.add_transition(a, state6)
        state5.add_transition(d, state6)
        state5.add_transition(h, state6)
        state5.add_transition(b, state7)
        state5.add_transition(c, state5)
        state5.add_transition(e, state5)
        state5.add_transition(f, state5)
        state5.add_transition(g, state5)
        state6.add_transition(a, state6)
        state6.add_transition(c, state6)
        state6.add_transition(d, state6)
        state6.add_transition(b, state7)
        state6.add_transition(f, state5)
        state6.add_transition(g, state5)
        state7.add_transition(c, state7)
        state7.add_transition(a, state6)
        comparator = DFAComparator()
        return DFA(alphabet, state0,
                               set([state0, state1, state2, state3, state4, state5,
                                    state6, state7]), comparator, "E-commerce automaton")

    # Definition: Recognizes e-commerce(taken from:
    # https://pdfs.semanticscholar.org/9cb9/74b6ece3e3fc2eab4f9cf0843bfc570df4a9.pdf).
    @staticmethod
    def get_different_ecommerce_automaton_NFA():
        alphabet = Alphabet(frozenset((SymbolStr('a'), SymbolStr('b'), SymbolStr(
            'c'), SymbolStr('d'), SymbolStr('e'), SymbolStr('f'), SymbolStr('g'), SymbolStr('h'))))
        a = alphabet['a']
        b = alphabet['b']
        c = alphabet['c']
        d = alphabet['d']
        e = alphabet['e']
        f = alphabet['f']
        g = alphabet['g']
        h = alphabet['h']
        state0 = State("State 0", True)
        state1 = State("State 1", True)
        state2 = State("State 2", True)
        state3 = State("State 3", True)
        state4 = State("State 4", True)
        state5 = State("State 5", True)
        state6 = State("State 6", True)
        state7 = State("State 7", True)
        state0.add_transition(a, state2)
        state0.add_transition(c, state1)
        state1.add_transition(a, state3)
        state1.add_transition(c, state1)
        state2.add_transition(c, state3)
        state2.add_transition(b, state0)
        state2.add_transition(a, state2)
        state2.add_transition(d, state2)
        state2.add_transition(e, state2)
        state3.add_transition(a, state3)
        state3.add_transition(c, state3)
        state3.add_transition(d, state3)
        state3.add_transition(e, state3)
        state3.add_transition(c, state1)
        state3.add_transition(f, state4)
        state4.add_transition(b, state1)
        state4.add_transition(h, state3)
        state4.add_transition(d, state3)
        state4.add_transition(a, state3)
        state4.add_transition(f, state4)
        state4.add_transition(c, state4)
        state4.add_transition(e, state5)
        state5.add_transition(d, state6)
        state5.add_transition(h, state6)
        state5.add_transition(b, state7)
        state5.add_transition(c, state5)
        state5.add_transition(e, state5)
        state5.add_transition(f, state5)
        state5.add_transition(g, state5)
        state6.add_transition(b, state6)
        state6.add_transition(c, state6)
        state6.add_transition(b, state7)
        state6.add_transition(f, state5)
        state6.add_transition(h, state5)
        state7.add_transition(c, state7)
        state7.add_transition(a, state6)
        comparator = NFAComparator()
        return NFA(alphabet, frozenset({state0}),
                               set([state0, state1, state2, state3, state4, state5,
                                    state6, state7]), comparator, "Modified E-commerce automaton")

    # Definition: Recognizes e-commerce, reduced version (taken from:
    # https://pdfs.semanticscholar.org/9cb9/74b6ece3e3fc2eab4f9cf0843bfc570df4a9.pdf).
    @staticmethod
    def get_reduced_ecommerce_automaton():
        alphabet = Alphabet(frozenset((SymbolStr('a'), SymbolStr('b'), SymbolStr(
            'c'), SymbolStr('d'), SymbolStr('e'), SymbolStr('f'), SymbolStr('h'))))
        a = alphabet['a']
        b = alphabet['b']
        c = alphabet['c']
        d = alphabet['d']
        e = alphabet['e']
        f = alphabet['f']
        h = alphabet['h']
        state0 = State("State 0", True)
        state1 = State("State 1", True)
        state2 = State("State 2", True)
        state3 = State("State 3", True)
        state4 = State("State 4", True)
        state0.add_transition(a, state2)
        state0.add_transition(c, state1)
        state1.add_transition(a, state3)
        state1.add_transition(c, state1)
        state2.add_transition(c, state3)
        state2.add_transition(b, state0)
        state2.add_transition(a, state2)
        state2.add_transition(d, state2)
        state2.add_transition(e, state2)
        state3.add_transition(a, state3)
        state3.add_transition(c, state3)
        state3.add_transition(d, state3)
        state3.add_transition(e, state3)
        state3.add_transition(b, state1)
        state3.add_transition(f, state4)
        state4.add_transition(b, state1)
        state4.add_transition(h, state3)
        state4.add_transition(d, state3)
        state4.add_transition(a, state3)
        state4.add_transition(f, state4)
        state4.add_transition(c, state4)
        state4.add_transition(e, state4)
        comparator = DFAComparator()
        return DFA(alphabet, state0,
                               set([state0, state1, state2, state3, state4]),
                               comparator,
                               "Reduced E-commerce automaton")

    # Definition: Recognizes strings not containing 'bbb' (not minimized).
    @staticmethod
    def get_dolzhenko_jonoska_automaton():
        a = abAlphabet['a']
        b = abAlphabet['b']
        state0 = State("State 0", True)
        state1 = State("State 1", True)
        state2 = State("State 2", True)
        state3 = State("State 3", True)
        state4 = State("State 4", True)
        state5 = State("State 5", True)
        state6 = State("State 6", True)
        state7 = State("State 7", True)
        state0.add_transition(a, state1)
        state0.add_transition(b, state4)
        state1.add_transition(a, state1)
        state1.add_transition(b, state2)
        state2.add_transition(a, state1)
        state2.add_transition(b, state3)
        state3.add_transition(a, state1)
        state4.add_transition(a, state6)
        state4.add_transition(b, state5)
        state5.add_transition(a, state6)
        state6.add_transition(a, state6)
        state6.add_transition(b, state7)
        state7.add_transition(a, state6)
        state7.add_transition(b, state5)
        comparator = DFAComparator()
        return DFA(abAlphabet, state0,
                               set([state0, state1, state2, state3, state4, state5,
                                    state6, state7]), comparator,
                                    "Dolzhenko-Jonoska automaton")

    # Definition: (a|b)*
    @staticmethod
    def get_a_or_b_automaton():
        a = abAlphabet['a']
        b = abAlphabet['b']
        stateA = State("State A", True)
        stateA.add_transition(a, stateA)
        stateA.add_transition(b, stateA)
        comparator = DFAComparator()
        return DFA(abAlphabet, stateA, set([stateA]), comparator, "a or b Automaton")

    # Definition: (c*ac*bc*)*
    @staticmethod
    def get_ab_with_cs_automaton():
        a = abcAlphabet['a']
        b = abcAlphabet['b']
        c = abcAlphabet['c']
        state0 = State("State 0", True)
        state1 = State("State 1")
        state0.add_transition(a, state1)
        state0.add_transition(c, state0)
        state1.add_transition(b, state0)
        state1.add_transition(c, state1)
        comparator = DFAComparator()
        return DFA(abcAlphabet, state0,
                               set([state0, state1]), comparator, "ab with cs automaton")

    # Definition: (ab)*
    @staticmethod
    def get_ab_automaton():
        a = abAlphabet['a']
        b = abAlphabet['b']
        state0 = State("State 0", True)
        state1 = State("State 1")
        state0.add_transition(a, state1)
        state1.add_transition(b, state0)
        comparator = DFAComparator()
        return DFA(abAlphabet, state0,
                               set([state0, state1]), comparator, "ab automaton")

    # Definition: (.*0)
    @staticmethod
    def get_zero_ending_automaton():
        stateA = State("State A", True)
        stateB = State("State B", True)
        stateC = State("State C")
        stateA.add_transition(zero, stateA)
        stateA.add_transition(one, stateC)
        stateB.add_transition(zero, stateA)
        stateB.add_transition(one, stateC)
        stateC.add_transition(zero, stateA)
        stateC.add_transition(one, stateC)
        comparator = DFAComparator()
        return DFA(binaryAlphabet, stateA,
                               set([stateA, stateB, stateC]), comparator, "Zero ending automaton")

    # Definition: (.*a), with {a, b, c} alphabet.
    @staticmethod
    def get_a_ending_with_cs_automaton():
        a = abcAlphabet['a']
        b = abcAlphabet['b']
        c = abcAlphabet['c']
        state0 = State("State 0", True)
        state1 = State("State 1")
        state0.add_transition(a, state0)
        state0.add_transition(b, state1)
        state0.add_transition(c, state0)
        state1.add_transition(a, state0)
        state1.add_transition(b, state1)
        state1.add_transition(c, state1)
        comparator = DFAComparator()
        return DFA(abcAlphabet, state0,
                               set([state0, state1]), comparator, "a ending with cs automaton")

    # Definition: (.*a), with {a, b} alphabet.
    @staticmethod
    def get_a_ending_automaton():
        a = abAlphabet['a']
        b = abAlphabet['b']
        state0 = State("State 0", True)
        state1 = State("State 1")
        state0.add_transition(a, state0)
        state0.add_transition(b, state1)
        state1.add_transition(a, state0)
        state1.add_transition(b, state1)
        comparator = DFAComparator()
        return DFA(abAlphabet, state0,
                               set([state0, state1]), comparator, "a ending automaton")

    # Definition: (..*0)
    @staticmethod
    def get_nonempty_zero_ending_automaton():
        stateA = State("State A")
        stateB = State("State B", True)
        stateA.add_transition(zero, stateB)
        stateA.add_transition(one, stateA)
        stateB.add_transition(zero, stateB)
        stateB.add_transition(one, stateA)
        comparator = DFAComparator()
        return DFA(binaryAlphabet, stateA,
                               set([stateA, stateB]), comparator, "Non-empty zero ending automaton")

    # Definition: (..*1)
    @staticmethod
    def get_nonempty_one_ending_automaton():
        stateA = State("State A")
        stateB = State("State B", True)
        stateA.add_transition(zero, stateA)
        stateA.add_transition(one, stateB)
        stateB.add_transition(zero, stateA)
        stateB.add_transition(one, stateB)
        comparator = DFAComparator()
        return DFA(binaryAlphabet, stateA,
                               set([stateA, stateB]), comparator, "Non-empty one ending automaton")

    # Definition: (ab)*a
    @staticmethod
    def get_complex_ab_prefixed_automaton():
        a = abAlphabet['a']
        b = abAlphabet['b']
        state0 = State("State 0")
        state1 = State("State 1")
        state2 = State("State 2", True)
        state3 = State("State 3")
        state4 = State("State 4")
        state5 = State("State 5")
        state6 = State("State 6")
        state7 = State("State 7")
        state0.add_transition(a, state1)
        state0.add_transition(b, state5)
        state1.add_transition(a, state6)
        state1.add_transition(b, state2)
        state2.add_transition(a, state0)
        state2.add_transition(b, state2)
        state3.add_transition(a, state2)
        state3.add_transition(b, state6)
        state4.add_transition(a, state7)
        state4.add_transition(b, state5)
        state5.add_transition(a, state2)
        state5.add_transition(b, state6)
        state6.add_transition(a, state6)
        state6.add_transition(b, state4)
        state7.add_transition(a, state6)
        state7.add_transition(b, state2)
        comparator = DFAComparator()
        return DFA(abAlphabet, state0,
                               set([state0, state1, state2, state3, state4, state5,
                                    state6, state7]), comparator, "Complex ab prefixed automaton")

    # Definition: (ab)*a
    @staticmethod
    def get_simpler_ab_prefixed_automaton():
        a = abAlphabet['a']
        b = abAlphabet['b']
        state0 = State("State 0")
        state1 = State("State 1", True)
        state0.add_transition(a, state1)
        state1.add_transition(b, state0)
        comparator = DFAComparator()
        return DFA(abAlphabet, state0,
                               set([state0, state1]), comparator, "Simpler ab prefixed automaton")

    @staticmethod
    def get_alternating_bit_protocol_automaton():
        a = abcdAlphabet['a']
        b = abcdAlphabet['b']
        c = abcdAlphabet['c']
        d = abcdAlphabet['d']
        state0 = State("State 0", True)
        state1 = State("State 1")
        state2 = State("State 2")
        state3 = State("State 3")
        state0.add_transition(a, state0)
        state0.add_transition(d, state1)
        state1.add_transition(d, state1)
        state1.add_transition(b, state2)
        state2.add_transition(b, state2)
        state2.add_transition(c, state3)
        state3.add_transition(c, state3)
        state3.add_transition(a, state0)
        comparator = DFAComparator()
        return DFA(abcdAlphabet, state0,
                               set([state0, state1, state2, state3]),
                               comparator,
                               "Alternating bit protocol automaton")

    @staticmethod
    def get_alternating_bit_protocol_z_automaton():
        alphabet = Alphabet(frozenset((SymbolStr('a'), SymbolStr('b'),
                                       SymbolStr('c'), SymbolStr('d'), SymbolStr('e'))))
        a = alphabet['a']
        b = alphabet['b']
        c = alphabet['c']
        d = alphabet['d']
        e = alphabet['e']
        state0 = State("State 0", True)
        state1 = State("State 1")
        state2 = State("State 2")
        state3 = State("State 3")
        state0.add_transition(a, state0)
        state0.add_transition(d, state1)
        state0.add_transition(e, state0)
        state1.add_transition(d, state1)
        state1.add_transition(b, state2)
        state1.add_transition(e, state1)
        state2.add_transition(b, state2)
        state2.add_transition(c, state3)
        state2.add_transition(e, state2)
        state3.add_transition(c, state3)
        state3.add_transition(a, state0)
        state3.add_transition(e, state3)
        comparator = DFAComparator()
        return DFA(alphabet, state0,
                               set([state0, state1, state2, state3]),
                               comparator,
                               "Alternating bit protocol z automaton")

    # Definition: {}
    @staticmethod
    def get_empty_automaton():
        a = abAlphabet['a']
        b = abAlphabet['b']
        stateA = State("State A", False)
        stateA.add_transition(a, stateA)
        stateA.add_transition(b, stateA)
        comparator = DFAComparator()
        return DFA(abAlphabet, stateA,
                               set([stateA]), comparator, "Empty automaton")

    # Definition: Σ*
    @staticmethod
    def get_sigma_star_automaton():
        a = abAlphabet['a']
        b = abAlphabet['b']
        stateA = State("State A", True)
        stateA.add_transition(a, stateA)
        stateA.add_transition(b, stateA)
        comparator = DFAComparator()
        return DFA(abAlphabet, stateA,
                               set([stateA]), comparator, "Sigma-star automaton")

    # Definition: uneven number of as
    @staticmethod
    def get_uneven_number_of_as_automaton():
        a = abAlphabet['a']
        b = abAlphabet['b']
        stateA = State("State A", False)
        stateB = State("State B", True)
        stateA.add_transition(a, stateB)
        stateA.add_transition(b, stateA)
        stateB.add_transition(a, stateA)
        stateB.add_transition(b, stateB)
        comparator = DFAComparator()
        return DFA(abAlphabet, stateA,
                               set([stateA, stateB]), comparator, "Uneven number of as")

    # Definition: uneven number of symbols
    @staticmethod
    def get_uneven_number_of_symbols_automaton():
        a = abAlphabet['a']
        b = abAlphabet['b']
        stateC = State("State C", False)
        stateD = State("State D", True)
        stateC.add_transition(a, stateD)
        stateC.add_transition(b, stateD)
        stateD.add_transition(a, stateC)
        stateD.add_transition(b, stateC)
        comparator = DFAComparator()
        return DFA(abAlphabet, stateC,
                               set([stateC, stateD]), comparator, "Uneven number of symbols")

    # Definition: uneven number of as and symbols
    @staticmethod
    def get_uneven_number_of_as_and_symbols_automaton():
        a = abAlphabet['a']
        b = abAlphabet['b']
        stateAC = State("State AC", False)
        stateAD = State("State AD", False)
        stateBC = State("State BC", False)
        stateBD = State("State BD", True)

        stateAC.add_transition(a, stateBD)
        stateAC.add_transition(b, stateAD)
        stateAD.add_transition(a, stateBC)
        stateAD.add_transition(b, stateAC)
        stateBC.add_transition(a, stateAD)
        stateBC.add_transition(b, stateBD)
        stateBD.add_transition(a, stateAC)
        stateBD.add_transition(b, stateBC)
        comparator = DFAComparator()
        return DFA(abAlphabet, stateAC,
                               set([stateAC, stateAD, stateBC, stateBD]),
                               comparator,
                               "Uneven number of as and symbols")

    # Definition: uneven number of as or symbols
    @staticmethod
    def get_uneven_number_of_as_or_symbols_automaton():
        a = abAlphabet['a']
        b = abAlphabet['b']
        stateAC = State("State AC", False)
        stateAD = State("State AD", True)
        stateBC = State("State BC", True)
        stateBD = State("State BD", True)

        stateAC.add_transition(a, stateBD)
        stateAC.add_transition(b, stateAD)
        stateAD.add_transition(a, stateBC)
        stateAD.add_transition(b, stateAC)
        stateBC.add_transition(a, stateAD)
        stateBC.add_transition(b, stateBD)
        stateBD.add_transition(a, stateAC)
        stateBD.add_transition(b, stateBC)
        comparator = DFAComparator()
        return DFA(abAlphabet, stateAC,
                               set([stateAC, stateAD, stateBC, stateBD]),
                               comparator,
                               "Uneven number of as or symbols")
