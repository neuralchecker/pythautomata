from turtle import pos
import numpy as np
from pythautomata.base_types.alphabet import Alphabet
from pythautomata.base_types.sequence import Sequence


def are_within_tolerance_limit(obs1, obs2, tolerance):
    assert(len(obs1) == len(obs2))
    return np.all((abs(np.array(obs1) - np.array(obs2)) <= tolerance))


def get_partition(value, partitions):
    assert(value >= 0 and value <= 1)
    limits = np.linspace(0, 1, partitions+1)
    if value == 1:
        return partitions-1
    # for i in range(len(limits)-1):
    #    if limits[i] <= value and limits[i+1] > value:
    #        return i
    positions = list(range(len(limits)-1))
    mid_element = int(len(limits)/2)
    while len(positions) > 1:
        if value >= limits[mid_element]:
            positions = positions[int(len(positions)/2):]
        else:
            positions = positions[:int(len(positions)/2)]
        mid_element = positions[int(len(positions)/2)]
    assert(len(positions) == 1)
    return positions[0]


def get_partitions(observation, partitions):
    return np.fromiter((get_partition(xi, partitions) for xi in observation), dtype=int)


def are_in_same_partition(obs1, obs2, partitions):
    assert(len(obs1) == len(obs2))
    return are_same_partition(get_partitions(obs1, partitions),
                              get_partitions(obs2, partitions))


def are_same_partition(partition1, partition2):
    assert(len(partition1) == len(partition2))
    return np.all((abs(partition1 - partition2) == 0))
