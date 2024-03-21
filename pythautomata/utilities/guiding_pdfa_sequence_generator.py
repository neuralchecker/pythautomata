from pythautomata.utilities.sequence_generator import SequenceGenerator
from pythautomata.automata.wheighted_automaton_definition.probabilistic_deterministic_finite_automaton import ProbabilisticDeterministicFiniteAutomaton as PDFA
from pythautomata.base_types.sequence import Sequence
import random

class GuidingPDFASequenceGenerator(SequenceGenerator):
    def __init__(self, pdfa: PDFA, max_seq_lenght: int, random_seed: int = 21, random_stop_proba = 0.2):
        self.pdfa = pdfa
        self._random_stop_proba = random_stop_proba
        self.max_seq_length = max_seq_lenght
        super().__init__(pdfa.alphabet, max_seq_lenght, random_seed)

    def generate_words(self, number_of_words: int):
        result = list()
        for _ in range(number_of_words):
            word = self.generate_single_word(self.max_seq_length)
            result.append(word)
        return result
    
    def _sort_valid_symbol(self, symbols, weights):
        if random.random() < self._random_stop_proba:
            return self.pdfa.terminal_symbol
        selected_symbols = []
        for i,w in enumerate(weights):
            if w>0:
                selected_symbols.append(symbols[i])
        next_symbol = random.choice(selected_symbols)
        return next_symbol
    
    def generate_single_word(self, length):
        word = Sequence()
        first_state = list(filter(lambda x: x.initial_weight == 1, self.pdfa.weighted_states))[0]
        symbols, weights, next_states = first_state.get_all_symbol_weights()
        next_symbol = self._sort_valid_symbol(symbols, weights)
        terminal_state = False
        while next_symbol != self.pdfa.terminal_symbol and (length is not None or len(word) <= length) and not terminal_state:
            word += next_symbol
            i = symbols.index(next_symbol)
            next_state = next_states[i]
            symbols, weights, next_states = next_state.get_all_symbol_weights()
            next_symbol = self._sort_valid_symbol(symbols, weights)
            if next_symbol == self.pdfa.terminal_symbol:
                word += next_symbol
                terminal_state = True
            else:
                length += 1
        print(len(word))
        return word