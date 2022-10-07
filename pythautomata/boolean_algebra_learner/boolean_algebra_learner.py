from abc import ABC, abstractmethod
from pythautomata.base_types.guard import Guard
from pythautomata.base_types.symbol import Symbol
from pythautomata.base_types.symbolic_state import SymbolicState

class BooleanAlgebraLearner(ABC):
    """Abstract class that boolean algebra learners should extend
    """
    @abstractmethod
    def learn(self, multidict:dict[SymbolicState, list[Symbol]]) -> list[tuple[Guard, SymbolicState]]:
        """[summary]

        Args:
            multidict (dict[SymbolicState, list[Symbol]]): a dictionary that maps a state to all the symbols with which the transition goes to said state

        Returns:
            list[tuple[Guard, SymbolicState]]: a list containing a guards and the state the guards transition to
        """
        pass