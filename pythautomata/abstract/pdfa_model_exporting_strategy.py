from abc import ABC, abstractmethod
from os import makedirs
from os.path import isdir
from pathlib import Path


class PDFAModelExportingStrategy(ABC):

    @abstractmethod
    def export(self, model, path: str):
        raise NotImplementedError

    def get_path_for(self, path: str, model):
        if path is None:
            name = model.name
            path = "output_models/" + \
                ("" if name is None else f"{name}")
        if not isdir(path):
            makedirs(path)
        return Path(path, model.name)