from typing import Optional
import random

from pythautomata.abstract.finite_automaton import FiniteAutomataComparator
from pythautomata.base_types.sequence import Sequence
from random import seed
from random import randint


class RandomWalkComparisonStrategy(FiniteAutomataComparator):

    def __init__(self, number_steps: int, reset_probability: float, random_seed: int = 21, ) -> None:
        super().__init__()
        self._number_steps = number_steps
        self._reset_probability = reset_probability
        self._seed = random_seed
        seed(self._seed)

    def are_equivalent(self, automaton1, automaton2) -> bool:
        return self.get_counterexample_between(automaton1, automaton2) is None

    # TODO: Change types to DeterministicFiniteAutomaton
    def get_counterexample_between(self, dfa1, dfa2) -> Optional[Sequence]:
        if dfa1.alphabet != dfa2.alphabet:
            raise ValueError("Alphabets are not equivalent.")

        steps = 0
        counter_example = Sequence()
        dfa1.reset()
        dfa2.reset()
        if not self.equivalent_output(
                dfa1.accepts(counter_example), dfa2.accepts(counter_example)):
            return counter_example

        symbols = list(dfa1.alphabet.symbols)
        symbols.sort()

        while steps < self._number_steps:
            if random.random() <= self._reset_probability:
                counter_example = Sequence()
                dfa1.reset()
                dfa2.reset()
            pos = randint(0, len(symbols) - 1)
            counter_example = counter_example.append(symbols[pos])
            steps += 1
            if not self.equivalent_output(dfa1.step(symbols[pos]), dfa2.step(symbols[pos])):
                return counter_example
        return None

    def equivalent_output(self, observation1, observation2) -> bool:
        return observation1 == observation2
