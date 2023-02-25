from genericpath import isdir
from os import makedirs
from pathlib import Path
from graphviz import Digraph

from pythautomata.abstract.model_exporting_strategy import ModelExportingStrategy


class MealyStandardDotExportingStrategy(ModelExportingStrategy):
    def export(self, model, path=None, encoding=None):
        graph = self.create_graph(model)
        path = self.get_path_for(path, model)
        path = str(path) + '.dot'

        dot_code = graph.source

        with open(path, "w+", encoding=encoding) as f:
            f.write(dot_code)

    def create_graph(self, model):
        graph = Digraph('mealy-machine')

        graph.node('__start0', shape='none', label='')
        initialState = model.initial_state
        graph.edge('__start0', initialState.name)

        for state in model.states:
            graph.node(state.name, shape='circle', label=state.name)

        for state in model.states:
            for symbol, state_set in state.transitions.items():
                for destinationState in state_set:
                    label = "%s/%s" % (symbol, state.outputs[symbol])
                    graph.edge(state.name, destinationState.name, label)

        return graph
