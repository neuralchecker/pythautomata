from os import makedirs
from os.path import isdir
from abc import ABC, abstractmethod
from pathlib import Path
from abstract.finite_automaton import FiniteAutomaton


class ModelExportingStrategy(ABC):

    @abstractmethod
    def export(self, model: FiniteAutomaton, path: str):
        # Exports a model to a human understandable format.
        raise NotImplementedError

    def get_path_for(self, path: str, model: FiniteAutomaton):
        if path is None:
            name = model.name
            path = "output_models/" + \
                ("" if name is None else f"{name}")
        if not isdir(path):
            makedirs(path)
        return Path(path, model.name)
