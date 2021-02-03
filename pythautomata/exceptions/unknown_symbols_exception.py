from exceptions.python_automata_exception import PythonAutomataException

class UnknownSymbolsException(PythonAutomataException):
    def __init__(self):
        self.message = "Some symbols do not belong to the given alphabet"