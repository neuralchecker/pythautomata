from abstract.model_exporting_strategy import ModelExportingStrategy
from model_exporters.image_exporting_strategy import ImageExportingStrategy

class DotExportingStrategy(ModelExportingStrategy):
    
    def export(self, model, path=None):
        graph = ImageExportingStrategy().create_graph(model)
        path = self.get_path_for(path, model)
        path = str(path)+'.dot'

        dot_code = graph.source
        
        with open(path, "w+", encoding="utf-8") as f:  
            f.write(dot_code)


