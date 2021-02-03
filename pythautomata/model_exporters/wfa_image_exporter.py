from graphviz import Digraph
from abstract.model_exporting_strategy import ModelExportingStrategy


class WFAImageExporter(ModelExportingStrategy):

    def export(self, model, path=None):
        graph = Digraph('weighted_automaton', format='png')
        graph.attr(rankdir='LR', margin='0', size='15')

        graph.attr('node', shape='circle')
        states = sorted(model.weighted_states, key=lambda x: x.name)
        for state in states:
            label = str(state.final_weight)
            if state.initial_weight == 1:
                graph.node(state.name, label, shape='diamond')
            else:
                graph.node(state.name, label)
            transitions = dict()
            for symbol, weighted_transitions in state.transitions_list.items():
                for weighted_transition in weighted_transitions:
                    if (state.name, weighted_transition[0].name) in transitions.keys():
                        new = transitions[(state.name, weighted_transition[0].name)] + "\n" + str(symbol) + "-" + \
                              str(weighted_transition[1])
                    else:
                        new = str(symbol) + "-" + str(weighted_transition[1])
                    transitions[(state.name, weighted_transition[0].name)] = new
            for key in transitions.keys():
                s_from, s_to = key
                graph.edge(s_from, s_to, str(transitions[key]))

        graph.render(self.get_path_for(path, model), cleanup=True)
