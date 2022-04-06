from pythautomata.base_types.symbol import Symbol
from pythautomata.base_types.guard import Guard


class NegationGuard(Guard):
    def __init__(self, guard: Guard):
        self.guard = guard

    def matches(self, s: Symbol):
        return not self.guard.matches(s)

    def __str__(self):
        return repr(self)

    def __repr__(self):
        return (u"\u00AC(") + str(self.guard) + ")"
