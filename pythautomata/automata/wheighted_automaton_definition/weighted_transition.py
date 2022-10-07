class WeightedTransition:

    def __init__(self, next_state, weight: float):
        self.next_state = next_state
        self.weight = weight

    def __eq__(self, other):
        return isinstance(other, WeightedTransition) and self.next_state == other.next_state \
               and self.weight == other.weight

    def __hash__(self):
        return hash(self.next_state)
