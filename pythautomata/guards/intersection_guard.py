from pythautomata.base_types.symbol import Symbol
from  pythautomata.base_types.guard import Guard

class IntersectionGuard(Guard):
    def __init__(self, *guards:Guard):
        self.guards = list(guards)

    def matches(self, s:Symbol):
        #TODO add concurrency
        return all(map(lambda g: g.matches(s), self.guards))

    def __str__(self):
        return repr(self)

    def __repr__(self):
        return (u" \u2229 ").join(map(str,self.guards))