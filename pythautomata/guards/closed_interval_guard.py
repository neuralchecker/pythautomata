from pythautomata.base_types.guard import Guard
from pythautomata.base_types.symbol import Symbol

class ClosedIntervalGuard(Guard):
    def __init__(self, left, right):
        self.left, self.right = left, right

    def matches(self, s: Symbol) -> bool:
        return s >= self.left and s <= self.right

    def __str__(self):
        return repr(self)

    def __repr__(self):
        return "[" + str(self.left) + " , " + str(self.right) +"]"