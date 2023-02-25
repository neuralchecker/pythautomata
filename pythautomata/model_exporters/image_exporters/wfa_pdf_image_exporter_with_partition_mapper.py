from graphviz import Digraph
from pythautomata.abstract.pdfa_model_exporting_strategy import PDFAModelExportingStrategy
from pythautomata.utilities.probability_partitioner import ProbabilityPartitioner
from pythautomata.model_exporters.partition_mapper import PartitionMapper
from collections import OrderedDict


class WFAImageExporterWithPartitionMapper(PDFAModelExportingStrategy):
    def __init__(self, partitioner: ProbabilityPartitioner, partition_mapper: PartitionMapper) -> None:
        super().__init__()
        self._partitioner = partitioner
        self._mapper = partition_mapper

    def export(self, model, path=None, file_name=None):
        graph = Digraph('weighted_automaton', format='png')
        graph.attr(rankdir='LR', margin='0', size='15')

        graph.attr('node', shape='circle')
        states = sorted(model.weighted_states, key=lambda x: str(x.name))
        for state in states:
            state_name = str(state.name)
            symbols_positions, weights, _ = state.get_all_symbol_weights()
            symb_weight = OrderedDict(zip(symbols_positions, weights))
            state_partition = self._partitioner.get_partition(weights)
            label_partition = self._mapper.get_str_for_partition(symb_weight,
                                                                 state_partition)
            label = state_name + "\n" + label_partition
            if state.initial_weight == 1:
                graph.node(state_name, label, shape='diamond')
            else:
                graph.node(state_name, label)
            transitions = dict()
            for symbol, weighted_transitions in state.transitions_list.items():
                for weighted_transition in weighted_transitions:
                    weighted_transition_name = str(weighted_transition[0].name)
                    transition_representation = self._mapper.get_str_for_transition(
                        symb_weight, symbol, state_partition)
                    if (state_name, weighted_transition_name) in transitions.keys():
                        new = transitions[(state_name, weighted_transition_name)] + "\n" + str(symbol) + "-" + \
                            transition_representation
                    else:
                        new = str(symbol) + "-" + transition_representation
                    transitions[(state_name, weighted_transition_name)] = new
            for key in transitions.keys():
                s_from, s_to = key
                graph.edge(s_from, s_to, str(transitions[key]))

        graph.render(self.get_path_for(path, model, file_name),
                     cleanup=True, format='pdf')
