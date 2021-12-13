from pythautomata.base_types.symbol import Symbol
from pythautomata.base_types.guard import Guard

class EqualityGuard(Guard):
    def __init__(self, s:Symbol):
        self._s = s

    def matches(self, s: Symbol) -> bool:
        return self._s == s

    def __str__(self):
        return repr(self)

    def __repr__(self):
        return str(self._s)