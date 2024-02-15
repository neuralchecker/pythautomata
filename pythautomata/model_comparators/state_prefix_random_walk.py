import random
from random import randint

from pythautomata.abstract.finite_automaton import FiniteAutomaton
from pythautomata.base_types.sequence import Sequence

class StatePrefixRandomWalkComparisonStrategy:

    def  __init__(self, number_of_steps, reset_probability):
        self.steps = number_of_steps
        self.reset_prob = reset_probability

    def are_equivalent(self, model1, model2):
        return self.get_counterexample(model1, model2) is None

    def get_counterexample(self, hypothesis: FiniteAutomaton, oracle):
        symbols = list(hypothesis.alphabet.symbols)
        symbols.sort()
        
        for state in hypothesis.states:
            prefix = state.access_string
            if prefix is None:
                prefix = hypothesis.get_access_string(state)

            suffix = Sequence()
            for _ in range(self.steps):
                pos = randint(0, len(symbols) - 1)
                suffix = suffix.append(symbols[pos])

                if hypothesis.process_query(prefix+suffix) != oracle.process_query(prefix+suffix):
                    return prefix+suffix

                if random.choices([True, False], [self.reset_prob, 1-self.reset_prob]):
                    suffix = Sequence()
                
        return None
