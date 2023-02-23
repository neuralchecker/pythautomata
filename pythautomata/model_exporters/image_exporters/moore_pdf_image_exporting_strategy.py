from genericpath import isdir
from os import makedirs
from pathlib import Path
from graphviz import Digraph

from pythautomata.abstract.model_exporting_strategy import ModelExportingStrategy
from pythautomata.model_exporters.dot_exporters.moore_dot_exporting_strategy import MooreDotExportingStrategy


class MoorePdfExportingStrategy(ModelExportingStrategy):

    def export(self, model, path=None):
        graph = MooreDotExportingStrategy().create_graph(model)
        path = self.get_path_for(path, model)
        graph.render(path, cleanup=True, format='pdf')
