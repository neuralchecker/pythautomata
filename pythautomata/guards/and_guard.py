from pythautomata.base_types.symbol import Symbol
from  pythautomata.base_types.guard import Guard

class AndGuard(Guard):
    def __init__(self, guard1:Guard, guard2:Guard):
        self.guard1 = guard1
        self.guard2 = guard2

    def matches(self, s:Symbol):
        return self.guard1.matches(s) and self.guard2.matches(s)

    def __str__(self):
        return repr(self)

    def __repr__(self):
        return "(" + str(self.guard1) + u") \u2227 (" + str(self.guard2) + ")"