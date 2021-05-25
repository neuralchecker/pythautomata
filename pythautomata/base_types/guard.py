from abc import ABC, abstractmethod
from pythautomata.base_types.symbol import Symbol

class Guard(ABC):

    
    @abstractmethod
    def matches(self, s:Symbol) -> bool: 
        """checks if the symbol s matches the guard

        Args:
            s (Symbol): symbol to check

        Returns:
            bool: True if the symbol matches the guard, False otherwise
        """        
        pass
