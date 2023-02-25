from pythautomata.automata.mealy_machine import MealyMachine
from pythautomata.base_types.sequence import Sequence


class MealyMachineComparisonStrategy:
    def are_equivalent(self, machine1: MealyMachine, machine2: MealyMachine):
        return self.get_counterexample_between(machine1, machine2) is None

    def get_counterexample_between(self, machine1: MealyMachine, machine2: MealyMachine):
        if machine1._alphabet != machine2._alphabet:
            raise ValueError("Input alphabets are not equivalent.")
        if machine1.output_alphabet != machine2.output_alphabet:
            raise ValueError("Output alphabets are not equivalent.")

        initial_pair = (machine1.initial_state, machine2.initial_state)
        pairs_to_visit = [initial_pair]
        sequence_for_pairs = {initial_pair: Sequence()}
        visited_pairs = set()

        pair = pairs_to_visit[0]
        for symbol in machine1._alphabet.symbols:
            if pair[0].outputs[symbol] != pair[1].outputs[symbol]:
                return sequence_for_pairs[pair]
            self_next_state = min(pair[0].next_states_for(symbol))
            other_next_state = min(pair[1].next_states_for(symbol))
            next_pair = (self_next_state, other_next_state)
            if next_pair not in pairs_to_visit and next_pair not in visited_pairs:
                sequence_for_pairs[next_pair] = sequence_for_pairs[pair] + symbol
                pairs_to_visit.append(next_pair)
        return None
