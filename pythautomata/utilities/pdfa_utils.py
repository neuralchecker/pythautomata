import numpy as np


def are_within_tolerance_limit(obs1, obs2, tolerance):
    assert (len(obs1) == len(obs2))
    return np.all((abs(np.array(obs1) - np.array(obs2)) <= tolerance))


def get_quantized_interval_partition(value, partitions):
    assert (value >= 0 and value <= 1)
    limits = np.linspace(0, 1, partitions+1)
    if value == 1:
        return partitions-1
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


def get_quantized_interval_partitions(observation, partitions):
    return np.fromiter((get_quantized_interval_partition(xi, partitions) for xi in observation), dtype=int)


# def are_in_same_quantized_interval_partition(obs1, obs2, partitions):
#    assert (len(obs1) == len(obs2))
#    partition1 = get_quantized_interval_partitions(obs1, partitions)
#    partition2 = get_quantized_interval_partitions(obs2, partitions)
#    return compare_quantized_interval_partition(partition1, partition2)


def compare_quantized_interval_partition(partition1, partition2):
    assert (len(partition1) == len(partition2))
    return np.all((abs(partition1 - partition2) == 0))
