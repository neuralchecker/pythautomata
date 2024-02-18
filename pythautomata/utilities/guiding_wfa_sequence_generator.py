from pythautomata.base_types.alphabet import Alphabet
from pythautomata.base_types.sequence import Sequence
from pythautomata.utilities.sequence_generator import SequenceGenerator
from pythautomata.automata.wheighted_automaton_definition.weighted_automaton import WeightedAutomaton as WFA
import random

class GuidingWDFASequenceGenerator(SequenceGenerator):    
    def __init__(self, wfa: WFA, max_seq_length: int, random_seed: int = 21, random_stop_proba = 0.2):
        self.wfa = wfa
        self._random_stop_proba = random_stop_proba
        super().__init__(wfa.alphabet, max_seq_length, random_seed)
    
    def generate_words(self, number_of_words: int):
        result = list()
        for _ in range(number_of_words):
            word = self.generate_single_word(None)
            result.append(word)
        return result

    def _sort_valid_symbol(self, symbols, weights):
        if random.random() < self._random_stop_proba:
            return self.wfa.terminal_symbol
        selected_symbols = []
        for i,w in enumerate(weights):
            if w>0:
                selected_symbols.append(symbols[i])
        next_symbol = random.choice(selected_symbols)
        return next_symbol
    
    def generate_single_word(self, length):
        assert length is None
        word = Sequence()
        first_state = list(filter(lambda x: x.initial_weight ==
                        1, self.wfa.weighted_states))[0]
        symbols, weights, next_states = first_state.get_all_symbol_weights()
        next_symbol = self._sort_valid_symbol(symbols, weights)
        while next_symbol != self.wfa.terminal_symbol:
            word += next_symbol
            i = symbols.index(next_symbol)
            next_state = next_states[i]
            symbols, weights, next_states = next_state.get_all_symbol_weights()
            next_symbol = self._sort_valid_symbol(symbols, weights)
        return word