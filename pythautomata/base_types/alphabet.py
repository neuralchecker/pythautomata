from base_types.symbol import Symbol
from typing import FrozenSet

class Alphabet:
    """Set of Symbols.
    """

    def __init__(self, symbols: frozenset[Symbol], name: str = None):
        """Constructor

        Parameters
        ----------
        symbols : frozenset[Symbol]
            Symbols belonging to alphabet
        name : str, optional
            An optional name, by default None
        """
        self.symbols = symbols
        self.name = name

    def __getitem__(self, key: str):
        return next(symbol for symbol in self.symbols if str(symbol) == key)

    def __contains__(self, symbol: Symbol):
        return symbol in self.symbols

    def __len__(self):
        return len(self.symbols)

    def __eq__(self, other):
        return isinstance(other, Alphabet) and self.symbols == other.symbols

    def __hash__(self):
        return hash(self.symbols)

    def __str__(self):
        return repr(self)

    def __repr__(self):
        return str(self.symbols)
