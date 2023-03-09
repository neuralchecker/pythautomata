from graphviz import Digraph
from pythautomata.abstract.pdfa_model_exporting_strategy import PDFAModelExportingStrategy


class WFADotExportingStrategy(PDFAModelExportingStrategy):

    def export(self, model, path=None, file_name=None):
        graph = self.create_graph(model)
        path = self.get_path_for(path, model, file_name)
        path = str(path) + ".dot"

        dot_code = graph.source

        with open(path, "w+", encoding="utf-8") as f:
            f.write(dot_code)

    def create_graph(self, model):
        graph = Digraph('weighted_automaton', format='png')
        graph.attr(rankdir='LR', margin='0', size='15')

        graph.attr('node', shape='circle')
        states = sorted(model.weighted_states, key=lambda x: str(x.name))
        for state in states:
            state_name = str(state.name)
            label = state_name + "\n" + str(state.final_weight)
            if state.initial_weight == 1:
                graph.node(state_name, label, shape='diamond')
            else:
                graph.node(state_name, label)
            transitions = dict()
            for symbol, weighted_transitions in state.transitions_list.items():
                for weighted_transition in weighted_transitions:
                    weighted_transition_name = str(weighted_transition[0].name)
                    if (state_name, weighted_transition_name) in transitions.keys():
                        new = transitions[(state_name, weighted_transition_name)] + "\n" + str(symbol) + "-" + \
                            str(weighted_transition[1])
                    else:
                        new = str(symbol) + "-" + str(weighted_transition[1])
                    transitions[(state_name, weighted_transition_name)] = new
            for key in transitions.keys():
                s_from, s_to = key
                graph.edge(s_from, s_to, str(transitions[key]))

        return graph
