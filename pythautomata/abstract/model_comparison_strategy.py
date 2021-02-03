from abc import ABC, abstractmethod
from base_types.sequence import Sequence
from abstract.finite_automaton import FiniteAutomaton

class ModelComparisonStrategy(ABC):

    @abstractmethod
    def are_equivalent(self, model1: FiniteAutomaton, model2: FiniteAutomaton) -> bool:
        # Returns true if both models are equivalent (i.e. they recongize the same
        # set of symbol sequences).
        raise NotImplementedError

    @abstractmethod
    def get_counterexample_between(self, model1: FiniteAutomaton, model2: FiniteAutomaton) -> Sequence:
        # Should return a counterexample sequence (one that is recognized by one and only
        # one of both models) if parameters are not equivalent, or None if they are
        raise NotImplementedError
