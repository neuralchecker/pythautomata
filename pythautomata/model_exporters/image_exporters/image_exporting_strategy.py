from genericpath import isdir
from os import makedirs
from pathlib import Path
from pythautomata.abstract.model_exporting_strategy import ModelExportingStrategy


class UniversalImageExportingStrategy:
    def __init__(self, exporting_strategy: ModelExportingStrategy, format: str):
        self.image_exporter = exporting_strategy
        self.format = format

    def export(self, model, path):
        graph = self.image_exporter.create_graph(model)
        path = self.get_path_for(path, model)
        graph.render(path, cleanup=True, format=self.format)

    def get_path_for(self, path, model):
        if path is None:
            name = model.name
            path = "output_models/" + \
                ("" if name is None else f"{name}")
        if not isdir(path):
            makedirs(path)
        return Path(path, model.name)
