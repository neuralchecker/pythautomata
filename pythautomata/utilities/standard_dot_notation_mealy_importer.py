import pydot
from pythautomata.automata.mealy_machine import MealyMachine
from pythautomata.base_types.alphabet import Alphabet
from pythautomata.base_types.mealy_state import MealyState

from pythautomata.base_types.symbol import SymbolStr
from pythautomata.exceptions.model_importing_error import ModelImportingError
from pythautomata.model_comparators.mealy_machine_comparison_strategy import MealyMachineComparisonStrategy


class StandardDotNotationMealyImporter:

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
                nodes[node.get_name()] = MealyState(node.get_name())

        for edge in graph.get_edge_list():
            if edge.get_source() == '__start0':
                initial_state = nodes[edge.get_destination()]
            else:
                edge_label = edge.get_attributes()['label']
                if edge_label[0] == "\"" and edge_label[0] == edge_label[-1]:
                    edge_label = edge_label[1:-1]

                edge_label = edge_label.split("/")
                symbol = SymbolStr(edge_label[0])
                symbols.add(symbol)
                output_symbol = SymbolStr(edge_label[1])
                output_symbols.add(output_symbol)

                nodes[edge.get_source()].add_transition(
                    symbol, nodes[edge.get_destination()], output_symbol)

        states = nodes.values()
        alphabet = Alphabet(frozenset(symbols))
        output_alphabet = Alphabet(frozenset(output_symbols))
        if initial_state is None:
            raise ModelImportingError

        return MealyMachine(alphabet, output_alphabet, initial_state, states, MealyMachineComparisonStrategy(), name)
