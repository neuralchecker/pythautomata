from abc import ABC, abstractmethod
from collections import OrderedDict
from pythautomata.base_types.symbol import Symbol
import numpy as np


class PartitionMapper(ABC):
    @abstractmethod
    def get_str_for_partition(self, symbols_and_probabilities: OrderedDict, partition):
        raise NotImplementedError

    @abstractmethod
    def get_str_for_transition(self, symbols_and_probabilities: OrderedDict, symbol: Symbol, partition):
        raise NotImplementedError


class TopKPartitionMapper(PartitionMapper):
    def get_str_for_partition(self, symbols_and_probabilities: OrderedDict, partition):
        symbols = list(symbols_and_probabilities.keys())
        top_k_symbols = np.array(symbols)[partition == 1]
        return str(top_k_symbols)

    def get_str_for_transition(self, symbols_and_probabilities: OrderedDict, symbol: Symbol, partition):
        symbols = list(symbols_and_probabilities.keys())
        top_k_symbols = np.array(symbols)[partition == 1]
        return str(symbol in top_k_symbols)
