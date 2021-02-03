from exceptions.python_automata_exception import PythonAutomataException

class UnexpectedTypeException(PythonAutomataException):
    def __init__(self):
        self.message = "Unexpected type"