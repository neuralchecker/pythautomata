from exceptions.python_automata_exception import PythonAutomataException

class ModelImportingError(PythonAutomataException):
    def __init__(self):
        self.message = "There was an error when importing model"
