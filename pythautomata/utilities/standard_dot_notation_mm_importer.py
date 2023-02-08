from pythautomata.base_types.alphabet import Alphabet
from pythautomata.base_types.moore_state import MooreState
from pythautomata.base_types.symbol import SymbolStr
from pythautomata.exceptions.model_importing_error import ModelImportingError
from pythautomata.automata.moore_machine_automaton import MooreMachineAutomaton
from pythautomata.model_comparators.moore_machine_comparison_strategy import \
    MooreMachineComparisonStrategy as MMComparator

import pydot


class StandardDotMMNotationImporter:

    @staticmethod
    def import_automata(path):
        graph = pydot.graph_from_dot_file(path)[0]
        name = graph.obj_dict['name']
        nodes = {}
        symbols = set()
        output_symbols = set()
        initial_state = None
        for node in graph.get_node_list():
            if node.get_name() not in ['__start0', '', '"\\n"']:
                value = SymbolStr(node.get_attributes()['label'].split("| ")[1][:-3])
                if value not in output_symbols:
                    output_symbols.add(value)
                nodes[node.get_name()] = MooreState(node.get_name(), value)

        for edge in graph.get_edge_list():
            if edge.get_source() == '__start0':
                initial_state = nodes[edge.get_destination()]
            else:
                edge_label = edge.get_attributes()['label']
                if edge_label[0] == "\"" and edge_label[0] == edge_label[-1]:
                    edge_label = edge_label[1:-1]
                symbol = SymbolStr(edge_label)
                symbols.add(symbol)
                nodes[edge.get_source()].add_transition(
                    symbol, nodes[edge.get_destination()])

        states = nodes.values()
        alphabet = Alphabet(frozenset(symbols))
        output_alphabet = Alphabet(frozenset(output_symbols))
        if initial_state is None:
            raise ModelImportingError

        return MooreMachineAutomaton(alphabet, output_alphabet, initial_state, states, MMComparator(), name)
