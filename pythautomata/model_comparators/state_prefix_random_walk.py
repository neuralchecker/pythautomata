import random
from pythautomata.abstract.finite_automaton import FiniteAutomaton

class StatePrefixRandomWalkComparisonStrategy:

    def init(self, number_of_steps, reset_probability):
        self.steps = number_of_steps
        self.reset_prob = reset_probability

    def are_equivalent(self, model1, model2):
        return self.get_counterexample(model1, model2) is None

    def get_counterexample(self, hypothesis: FiniteAutomaton, oracle):
        access_strings = []
        for state in hypothesis.states:
            access_strings.append(hypothesis.get_access_string(state))

        for prefix in access_strings:
            suffix = ""
            for _ in range(self.steps):
                suffix += random.choice(hypothesis.alphabet)

                if hypothesis.process_query(prefix+suffix) != oracle.process_query(prefix+suffix):
                    return prefix+suffix

                if random.choices([True, False], [self.reset_prob, 1-self.reset_prob]):
                    suffix = ""
                
        return None
