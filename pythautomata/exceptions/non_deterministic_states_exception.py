from exceptions.python_automata_exception import PythonAutomataException

class NonDeterministicStatesException(PythonAutomataException):
    def __init__(self):
        self.message = "All states must be deterministic in order to create a Deterministic Finite Automaton"