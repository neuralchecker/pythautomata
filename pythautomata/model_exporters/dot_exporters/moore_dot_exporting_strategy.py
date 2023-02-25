from symtable import Symbol
from graphviz import Digraph

from pythautomata.abstract.model_exporting_strategy import ModelExportingStrategy


class MooreDotExportingStrategy(ModelExportingStrategy):
    def export(self, model, path=None):
        graph = self.create_graph(model)
        path = self.get_path_for(path, model)
        path = str(path) + '.dot'

        dot_code = graph.source

        with open(path, "w+", encoding="utf-8") as f:
            f.write(dot_code)

    def create_graph(self, model):
        graph = Digraph('moore_machine')
        graph.attr(rankdir='LR', size='8,5')

        graph.attr('node', shape='circle')
        for state in model.states:
            label = state.name + '/' + str(state.value)
            graph.node(state.name, label=label)
            transitions = dict()
            for symbol, destinationStates in state.transitions.items():
                for destinationState in destinationStates:
                    transitions.setdefault(
                        (state.name, destinationState.name), set())
                    transitions[(state.name, destinationState.name)].add(
                        str(symbol))

            for (state_from, state_to), symbols in transitions.items():
                label = self._get_label_for(symbols, model._alphabet)
                graph.edge(state_from, state_to, label)

        graph.attr('node', shape='point')
        nodeName = 'start'
        graph.node(nodeName)
        graph.edge(nodeName, model.initial_state.name)

        return graph

    def _get_label_for(self, symbols: list, alphabet):
        if len(symbols) == len(alphabet):
            return "Σ"
        elif len(symbols) <= len(alphabet) / 2:
            return ", ".join(sorted(symbols))
        else:
            complement = set(map(str, alphabet.symbols)) - set(symbols)
            label = ", ".join(sorted(complement))
            return f"Σ - {{{label}}}"
