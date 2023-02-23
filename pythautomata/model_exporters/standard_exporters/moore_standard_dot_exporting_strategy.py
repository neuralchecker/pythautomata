from graphviz import Digraph
from pythautomata.abstract.model_exporting_strategy import ModelExportingStrategy


class MooreStandardDotExportingStrategy(ModelExportingStrategy):

    def export(self, model, path=None, encoding=None):
        graph = self.create_graph(model)
        path = self.get_path_for(path, model)
        path = str(path) + '.dot'

        dot_code = graph.source

        with open(path, "w+", encoding=encoding) as f:
            f.write(dot_code)

    def create_graph(self, model):
        graph = Digraph('moore-machine-automata')

        graph.node('__start0', shape='none', label='')
        initialState = model.initial_state
        graph.edge('__start0', initialState.name)

        for state in model.states:
            label = "{ %s | %s }" % (state.name, state.value.value)
            graph.node(state.name, shape='record',
                       style='rounded', label=label)

        for state in model.states:
            for symbol, destinationStates in state.transitions.items():
                for destinationState in destinationStates:
                    graph.edge(state.name, destinationState.name, str(symbol))

        return graph
