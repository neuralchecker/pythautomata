import numpy as np
from abc import ABC, abstractmethod


class ProbabilityPartitioner(ABC):

    def __init__(self):
        self._partitions_cache = dict()

    def get_partition(self, probability_vector):
        if tuple(probability_vector) in self._partitions_cache:
            return self._partitions_cache[tuple(probability_vector)]
        else:
            partition = self._get_partition(probability_vector)
            self._partitions_cache[tuple(probability_vector)] = partition
            return partition

    @abstractmethod
    def _get_partition(self, probability_vector):
        raise NotImplementedError

    def are_in_same_partition(self, probability_vector1, probability_vector2):
        assert (len(probability_vector1) == len(probability_vector2))
        partition1 = self.get_partition(probability_vector1)
        partition2 = self.get_partition(probability_vector2)
        return np.all(np.equal(partition1, partition2))


class QuantizationProbabilityPartitioner(ProbabilityPartitioner):

    def __init__(self, number_of_partitions) -> None:
        super().__init__()
        self._partitions = number_of_partitions

    def _get_interval(self, value):
        assert (value >= 0 and value <= 1)
        limits = np.linspace(0, 1, self._partitions+1)
        if value == 1:
            return self._partitions-1
        positions = list(range(len(limits)-1))
        mid_element = int(len(limits)/2)
        while len(positions) > 1:
            if value >= limits[mid_element]:
                positions = positions[int(len(positions)/2):]
            else:
                positions = positions[:int(len(positions)/2)]
            mid_element = positions[int(len(positions)/2)]
        assert (len(positions) == 1)
        return positions[0]

    def _get_partition(self, probability_vector):
        return np.fromiter((self._get_interval(xi) for xi in probability_vector), dtype=int)

class QuantizationProbabilityPartitionerPlus(ProbabilityPartitioner):
    """
    Class implementing a ProbabilityPartitioner.
    Identical to QuantizationProbabilityPartitioner but considers elements that are zero as a different interval. 
    This means that distributions should have the same support to be in the same partition.
    """
    def __init__(self, number_of_partitions) -> None:
        super().__init__()
        self._partitions = number_of_partitions

    def _get_interval(self, value):
        assert (value >= 0 and value <= 1)
        limits = np.linspace(0, 1, self._partitions+1)
        if value == 1:
            return self._partitions
        if value == 0:
            return 0
        positions = list(range(len(limits)-1))
        mid_element = int(len(limits)/2)
        while len(positions) > 1:
            if value >= limits[mid_element]:
                positions = positions[int(len(positions)/2):]
            else:
                positions = positions[:int(len(positions)/2)]
            mid_element = positions[int(len(positions)/2)]
        assert (len(positions) == 1)
        return positions[0]+1

    def _get_partition(self, probability_vector):
        return np.fromiter((self._get_interval(xi) for xi in probability_vector), dtype=int)

class TopKProbabilityPartitioner(ProbabilityPartitioner):

    def __init__(self, k) -> None:
        self.k = k
        super().__init__()

    def _get_partition(self, probability_vector):
        order = (np.array(probability_vector)*-1).argsort()
        ranks = order.argsort()
        ranks[ranks >= self.k] = -1
        ranks[ranks != -1] = 1
        return ranks


class RankingPartitioner(ProbabilityPartitioner):

    def __init__(self, k) -> None:
        self.k = k
        super().__init__()

    def _get_partition(self, probability_vector):
        order = (np.array(probability_vector)*-1).argsort()
        ranks = order.argsort()
        ranks[ranks >= self.k] = -1
        return ranks

class TopKProbabilityPartitionerPlus(ProbabilityPartitioner):
    def __init__(self, k) -> None:
        self.k = k
        super().__init__()

    def _get_partition(self, probability_vector):
        probability_vector = np.array(probability_vector)
        order = (-probability_vector).argsort()  # Sort descending
        support_mask = probability_vector > 0   # Identify the support
        top_k_mask = np.zeros_like(probability_vector, dtype=int)
        top_k_mask[order[:self.k]] = 1  # Mark the top-k elements
        
        # Combine top-k and support information
        partition = top_k_mask * support_mask.astype(int)
        return partition

class RankingPartitionerPlus(ProbabilityPartitioner):
    def __init__(self, k) -> None:
        self.k = k
        super().__init__()

    def _get_partition(self, probability_vector):
        probability_vector = np.array(probability_vector)
        order = (-probability_vector).argsort()  # Sort descending
        support_mask = probability_vector > 0   # Identify the support
        ranks = np.full_like(probability_vector, -1, dtype=int)  # Initialize as -1
        
        # Assign ranks only within the support
        for idx, value in enumerate(order):
            if idx < self.k:
                ranks[value] = idx + 1  # Rank within top-k
            elif support_mask[value]:
                ranks[value] = idx + 1  # Rank within full support
        
        return ranks