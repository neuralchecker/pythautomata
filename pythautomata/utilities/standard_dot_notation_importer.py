from re import findall, match
from typing import Any

from pythautomata.base_types.alphabet import Alphabet
from pythautomata.base_types.state import State
from pythautomata.base_types.symbol import SymbolStr
from pythautomata.exceptions.model_importing_error import ModelImportingError
from pythautomata.automata.deterministic_finite_automaton import DeterministicFiniteAutomaton
from pythautomata.model_comparators.dfa_comparison_strategy import \
    DFAComparisonStrategy as DFAComparator

import pydot


class StandardDotNotationImporter:

    @staticmethod
    def import_automata(path):
        graph = pydot.graph_from_dot_file(path)[0]
        name = graph.obj_dict['name']
        nodes = {}
        symbols = set()
        initial_state = None
        for node in graph.get_node_list():
            if node.get_name() not in ['__start0', '', '"\\n"']:
                is_final = 'shape' in node.get_attributes().keys(
                ) and 'doublecircle' in node.get_attributes()['shape']
                nodes[node.get_name()] = State(node.get_name(), is_final)

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
        comparator = DFAComparator()
        if initial_state is None:
            raise ModelImportingError

        return DeterministicFiniteAutomaton(alphabet, initial_state, states, comparator, name)
