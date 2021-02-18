from base_types.sequence import Sequence
from base_types.state import State
from abstract.finite_automata_comparator import FiniteAutomataComparator
from abstract.finite_automaton import FiniteAutomaton
from typing import Optional

class DFAComparisonStrategy(FiniteAutomataComparator):

    def are_equivalent(self, automaton1: FiniteAutomaton, automaton2: FiniteAutomaton) -> bool:
        return self.get_counterexample_between(automaton1, automaton2) is None

    #TODO: Change types to DeterministicFiniteAutomaton
    def get_counterexample_between(self, dfa1: FiniteAutomaton, dfa2: FiniteAutomaton) -> Optional[Sequence]:
        if dfa1.alphabet != dfa2.alphabet:
            raise ValueError("Alphabets are not equivalent.")
        
        
        #initialPairs is an arbitrary pair of states
        initialPair: tuple[State, State] = (dfa1.initial_state, dfa2.initial_state)
        pairsToVisit = [initialPair]
        sequenceForPairs = {initialPair: Sequence()}
        visitedPairs: set[tuple[State, State]] = set()

        while pairsToVisit:
            pair = pairsToVisit[0]
            if pair[0].is_final != pair[1].is_final:
                return sequenceForPairs[pair]
            for symbol in dfa1.alphabet.symbols:
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
