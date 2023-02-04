
from pythautomata.abstract.model_exporting_strategy import ModelExportingStrategy
from pythautomata.model_exporters.dot_exporting_strategy import DotExportingStrategy


class ImageExportingStrategy(ModelExportingStrategy):

    def export(self, model, path=None):
        graph = DotExportingStrategy().create_graph(model)
        path = self.get_path_for(path, model)
        graph.render(path, cleanup=True)
