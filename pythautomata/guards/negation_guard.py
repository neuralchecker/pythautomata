from pythautomata.base_types.symbol import Symbol
from  pythautomata.base_types.guard import Guard

class NegationGuard(Guard):
    def __init__(self, guard:Guard):
        self.guard = guard

    def matches(self, s:Symbol):
        return any(map(lambda g: g.matches(s), self.guards))

    def __str__(self):
        return repr(self)

    def __repr__(self):
        return print(u"\u00AC(" + str(self.guard) + ")")