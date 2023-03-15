from typing import Optional

from pythautomata.automata.moore_machine_automaton import MooreMachineAutomaton
from pythautomata.base_types.sequence import Sequence
from pythautomata.base_types.state import State


class MooreMachineComparisonStrategy():

    def are_equivalent(self, automaton1, automaton2) -> bool:
        return self.get_counterexample_between(automaton1, automaton2) is None

    def get_counterexample_between(self, mma1: MooreMachineAutomaton, mma2: MooreMachineAutomaton) -> Optional[Sequence]:
        if mma1._alphabet != mma2._alphabet:
            raise ValueError("Input alphabets are not equivalent.")
        if mma1.output_alphabet != mma2.output_alphabet:
            raise ValueError("Output alphabets are not equivalent.")

        # initialPairs is an arbitrary pair of states
        initialPair: tuple[State, State] = (
            mma1.initial_state, mma2.initial_state)
        pairsToVisit = [initialPair]
        sequenceForPairs = {initialPair: Sequence()}
        visitedPairs: set[tuple[State, State]] = set()

        while pairsToVisit:
            pair = pairsToVisit[0]
            if pair[0].value != pair[1].value:
                return sequenceForPairs[pair]
            for symbol in mma1._alphabet.symbols:
                self._process_equivalence_iteration_with(symbol, pairsToVisit,
                                                         visitedPairs, sequenceForPairs)
            pairsToVisit.remove(pair)
            visitedPairs.add(pair)
        return None

    def _process_equivalence_iteration_with(self, symbol, pairs_to_visit, visited_pairs, sequence_for_pairs):
        pair = pairs_to_visit[0]
        selfNextState = min(pair[0].next_states_for(symbol))
        otherNextState = min(pair[1].next_states_for(symbol))
        nextPair = (selfNextState, otherNextState)
        if nextPair not in pairs_to_visit and nextPair not in visited_pairs:
            sequence_for_pairs[nextPair] = sequence_for_pairs[pair] + symbol
            pairs_to_visit.append(nextPair)

    def equivalent_output(self, observation1, observation2) -> bool:
        return observation1 == observation2
