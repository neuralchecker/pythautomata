from genericpath import isdir
from os import makedirs
from pathlib import Path
from pythautomata.automata.moore_machine_automaton import MooreMachineAutomaton
from pythautomata.model_exporters.image_exporting_mm_strategy import ImageExportingMMStrategy


class DotExportingMMStrategy():
    def export(self, model, path=None):
        graph = ImageExportingMMStrategy().create_graph(model)
        path = self.get_path_for(path, model)
        path = str(path) + '.dot'

        dot_code = graph.source

        with open(path, "w+", encoding="utf-8") as f:
            f.write(dot_code)

    def get_path_for(self, path: str, model: MooreMachineAutomaton):
        if path is None:
            name = model._name
            path = "output_models/" + \
                ("" if name is None else f"{name}")
        if not isdir(path):
            makedirs(path)
        return Path(path, model._name)
