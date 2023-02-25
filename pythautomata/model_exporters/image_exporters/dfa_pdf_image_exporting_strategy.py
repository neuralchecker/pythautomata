from graphviz import Digraph
from pythautomata.abstract.model_exporting_strategy import ModelExportingStrategy
from pythautomata.model_exporters.dot_exporters.dfa_dot_exporting_strategy import DfaDotExportingStrategy


class DfaPdfExportingStrategy(ModelExportingStrategy):
    def export(self, model, path=None):
        graph = DfaDotExportingStrategy().create_graph(model)
        path = self.get_path_for(path, model)
        graph.render(path, cleanup=True, format='pdf')
