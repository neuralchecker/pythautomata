from typing import Optional
import random

from pythautomata.automata.moore_machine_automaton import MooreMachineAutomaton as MooreMachine
from pythautomata.base_types.sequence import Sequence
from random import seed
from random import randint

class RandomWalkMMComparisonStrategy:
    def __init__(self, number_steps: int, reset_probability: float, random_seed: int = 21) -> None:
        super().__init__()
        self._number_steps = number_steps
        self._reset_probability = reset_probability
        self._seed = random_seed
        seed(self._seed)

    def are_equivalent(self, mm1: MooreMachine, mm2: MooreMachine) -> bool:
        return self.get_counterexample_between(mm1, mm2) is None

    def get_counterexample_between(self, mm1, mm2) -> Optional[Sequence]:
        if mm1._alphabet != mm2._alphabet:
            raise ValueError("Alphabets are not equivalent.")

        steps = 0
        counter_example = Sequence()
        mm1.reset()
        mm2.reset()
        equivalent_output = self.equivalent_output(
            mm1.last_symbol(counter_example), mm2.last_symbol(counter_example))

        symbols = list(mm1._alphabet.symbols)
        symbols.sort()

        while equivalent_output and steps < self._number_steps:
            if random.random() <= self._reset_probability:
                counter_example = Sequence()
                mm1.reset()
                mm2.reset()
            pos = randint(0, len(symbols) - 1)
            random_symbol = symbols[pos]
            counter_example = counter_example.append(random_symbol)
            steps += 1
            equivalent_output = self.equivalent_output(
                mm1.step(random_symbol), mm2.step(random_symbol))
            if not equivalent_output:
                return counter_example
        return None

    def equivalent_output(self, observation1, observation2) -> bool:
        return observation1 == observation2
