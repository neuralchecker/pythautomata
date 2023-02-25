from random import randint, seed
import random

from pythautomata.automata.mealy_machine import MealyMachine
from pythautomata.base_types.sequence import Sequence


class RandomWalkMealyMachineComparisonStrategy:

    def __init__(self, number_steps: int, reset_probability: float, random_seed: int = 21, ) -> None:
        self._number_steps = number_steps
        self._reset_probability = reset_probability
        self._seed = random_seed
        seed(self._seed)

    def are_equivalent(self, machine1: MealyMachine, machine2: MealyMachine) -> bool:
        return self.get_counterexample_between(machine1, machine2) is None

    def get_counterexample_between(self, machine1: MealyMachine, machine2: MealyMachine):
        if machine1._alphabet != machine2._alphabet:
            raise ValueError("Input alphabets are not equivalent.")
        if machine1._output_alphabet != machine2._output_alphabet:
            raise ValueError("Output alphabets are not equivalent.")

        steps = 0
        counter_example = Sequence()
        machine1.reset()
        machine2.reset()
        if not self.equivalent_output(
            machine1.last_symbol(
                counter_example), machine2.last_symbol(counter_example)):
            return counter_example

        symbols = list(machine1._alphabet.symbols)
        symbols.sort()

        while steps < self._number_steps:
            if random.random() <= self._reset_probability:
                counter_example = Sequence()
                machine1.reset()
                machine2.reset()
            pos = randint(0, len(symbols) - 1)
            counter_example = counter_example.append(symbols[pos])
            steps += 1
            if not self.equivalent_output(machine1.step(symbols[pos]), machine2.step(symbols[pos])):
                return counter_example

        return None

    def equivalent_output(self, observation1, observation2) -> bool:
        return observation1 == observation2
