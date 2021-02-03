from exceptions.python_automata_exception import PythonAutomataException

class NoneStateException(PythonAutomataException):
    def __init__(self):
        self.message = "State can not be None"