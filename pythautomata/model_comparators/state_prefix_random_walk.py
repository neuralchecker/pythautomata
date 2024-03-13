import random
from random import randint

from pythautomata.abstract.finite_automaton import FiniteAutomaton
from pythautomata.base_types.sequence import Sequence

class StatePrefixRandomWalkComparisonStrategy:

    def  __init__(self, number_steps):
        self.steps = number_steps

    def are_equivalent(self, model1, model2):
        return self.get_counterexample_between(model1, model2) is None

    def get_counterexample_between(self, hypothesis: FiniteAutomaton, oracle):
        symbols = list(hypothesis.alphabet.symbols)
        symbols.sort()
        
        for state in hypothesis.states:
            prefix = state.access_string
            if prefix is None:
                prefix = hypothesis.get_access_string(state)

            hypothesis.reset()
            oracle.reset()
            for p in prefix:
                hypothesis.step(p)
                oracle.step(p)

            suffix = Sequence()
            for _ in range(self.steps):
                pos = randint(0, len(symbols) - 1)
                suffix = suffix.append(symbols[pos])

                if hypothesis.step(symbols[pos]) != oracle.step(symbols[pos]):
                    return prefix+suffix
                
        return None
