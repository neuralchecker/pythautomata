from pythautomata.abstract.model_exporting_strategy import ModelExportingStrategy
from pythautomata.automata.non_deterministic_finite_automaton import NondeterministicFiniteAutomaton
from pythautomata.base_types.symbolic_state import SymbolicState
from graphviz import Digraph


class DfaStandardDotExportingStrategy(ModelExportingStrategy):

    def export(self, model, path=None, encoding=None):
        graph = self.create_graph(model)
        path = self.get_path_for(path, model)
        path = str(path) + '.dot'

        dot_code = graph.source

        with open(path, "w+", encoding=encoding) as f:
            f.write(dot_code)

    def create_graph(self, model):
        if type(model) == NondeterministicFiniteAutomaton:
            raise NotImplemented

        graph = Digraph('finite_state_machine')

        graph.node('__start0', shape='none', label='')
        for state in model.states:
            if state.is_final:
                graph.node(state.name, label=state.name, shape='doublecircle')
            else:
                graph.node(state.name, label=state.name, shape='circle')

        initialState = model.initial_state
        graph.edge('__start0', initialState.name, label='')
        for state in model.states:
            for symbol, destinationStates in state.transitions.items():
                for destinationState in destinationStates:
                    graph.edge(state.name, destinationState.name, str(symbol))

        return graph
