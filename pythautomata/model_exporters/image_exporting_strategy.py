from graphviz import Digraph
from abstract.model_exporting_strategy import ModelExportingStrategy


class ImageExportingStrategy(ModelExportingStrategy):
    
    def export(self, model, path=None):
        graph = self.create_graph(model)
        path = self.get_path_for(path, model)
        graph.render(path, cleanup=True)

    def create_graph(self, model):
        graph = Digraph('finite_state_machine')
        graph.attr(rankdir='LR', size='8,5')

        finalStates = filter(lambda state: state.is_final, model.states)
        graph.attr('node', shape='doublecircle')
        for state in finalStates:
            graph.node(state.name)

        graph.attr('node', shape='circle')
        for state in model.states:
            transitions = dict()
            for symbol, destinationStates in state.transitions.items():
                for destinationState in destinationStates:
                    transitions.setdefault((state.name, destinationState.name), set())
                    transitions[(state.name, destinationState.name)].add(str(symbol))
            for key, symbols in transitions.items():
                state_from, state_to = key
                label = self.get_label_for(symbols, model.alphabet)
                graph.edge(state_from, state_to, label)

        graph.attr('node', shape='point')
        for index, initialState in enumerate(model.initial_states):
            nodeName = 'start' + str(index)
            graph.node(nodeName)
            graph.edge(nodeName, initialState.name)
        
        return graph    

    def get_label_for(self, symbols: list, alphabet):
        if len(symbols) == len(alphabet):
            return "Σ"
        elif len(symbols) <= len(alphabet) / 2:
            return ", ".join(sorted(symbols))
        else:
            complement = set(map(str, alphabet.symbols)) - set(symbols)
            label = ", ".join(sorted(complement))
            return f"Σ - {{{label}}}"
