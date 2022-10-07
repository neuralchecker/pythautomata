from pythautomata.abstract.probabilistic_model import ProbabilisticModel
from pythautomata.base_types.sequence import Sequence
from pythautomata.utilities import pdfa_utils
import math
from sklearn.metrics import ndcg_score
import numpy as np
epsilon = Sequence()


def ndcg_score_avg(target_model: ProbabilisticModel, learned_model: ProbabilisticModel, test_sequences: list[Sequence]):
    suffixes = list()
    suffixes.append(Sequence() + learned_model.terminal_symbol)
    ndcg = list()
    k = math.ceil(len(learned_model.alphabet) / 2)

    for symbol in learned_model.alphabet.symbols:
        suffixes.append(Sequence(symbol))

    all_obs1 = target_model.last_token_probabilities_batch(
        test_sequences, suffixes)
    all_obs2 = learned_model.last_token_probabilities_batch(
        test_sequences, suffixes)

    for i in range(len(all_obs1)):
        obs1 = np.asarray([all_obs1[i]])
        obs2 = np.asarray([all_obs2[i]])
        ndcg_word_score = ndcg_score(obs1, obs2, k=k)
        ndcg.append(ndcg_word_score)

    return np.mean(np.array(ndcg))


def wer_avg(target_model: ProbabilisticModel, learned_model: ProbabilisticModel, test_sequences: list[Sequence]):
    suffixes = list()
    suffixes.append(Sequence() + learned_model.terminal_symbol)
    wer = 0

    for symbol in learned_model.alphabet.symbols:
        suffixes.append(Sequence(symbol))

    all_obs1 = target_model.last_token_probabilities_batch(
        test_sequences, suffixes)
    all_obs2 = learned_model.last_token_probabilities_batch(
        test_sequences, suffixes)

    for i in range(len(all_obs1)):
        obs1 = np.asarray(all_obs1[i])
        obs2 = np.asarray(all_obs2[i])
        max1 = np.argmax(obs1)
        max2 = np.argmax(obs2)
        if max1 != max2:
            wer += 1

    return wer / len(test_sequences)


def log_probability_error(target_model: ProbabilisticModel, learned_model: ProbabilisticModel, test_sequences: list[Sequence]):
    errors = list()
    for seq in test_sequences:
        errors.append(abs(target_model.log_sequence_weight(seq) -
                      learned_model.log_sequence_weight(seq)))
    return np.mean(np.array(errors))


def out_of_tolerance_elements(target_model: ProbabilisticModel, learned_model: ProbabilisticModel, test_sequences: list[Sequence], tolerance):
    suffixes = list()
    errorCount = 0
    suffixes.append(Sequence() + learned_model.terminal_symbol)
    for symbol in learned_model.alphabet.symbols:
        suffixes.append(Sequence(symbol))

    all_obs1 = target_model.last_token_probabilities_batch(
        test_sequences, suffixes)
    all_obs2 = learned_model.last_token_probabilities_batch(
        test_sequences, suffixes)

    for i in range(len(all_obs1)):
        obs1 = np.asarray(all_obs1[i])
        obs2 = np.asarray(all_obs2[i])
        if not pdfa_utils.are_within_tolerance_limit(obs1, obs2, tolerance):
            errorCount += 1

    return errorCount


def out_of_partition_elements(target_model: ProbabilisticModel, learned_model: ProbabilisticModel, test_sequences: list[Sequence], partitions: int):
    suffixes = list()
    errorCount = 0
    suffixes.append(Sequence() + learned_model.terminal_symbol)
    for symbol in learned_model.alphabet.symbols:
        suffixes.append(Sequence(symbol))

    all_obs1 = target_model.last_token_probabilities_batch(
        test_sequences, suffixes)
    all_obs2 = learned_model.last_token_probabilities_batch(
        test_sequences, suffixes)

    for i in range(len(all_obs1)):
        obs1 = np.asarray(all_obs1[i])
        obs2 = np.asarray(all_obs2[i])
        result = pdfa_utils.are_in_same_partition(obs1, obs2, partitions)
        if not result:
            errorCount += 1

    return errorCount


def absolute_error_avg(target_model: ProbabilisticModel, learned_model: ProbabilisticModel, test_sequences: list[Sequence]):
    suffixes = list()
    suffixes.append(Sequence() + learned_model.terminal_symbol)

    for symbol in learned_model.alphabet.symbols:
        suffixes.append(Sequence(symbol))

    all_obs1 = target_model.last_token_probabilities_batch(
        test_sequences, suffixes)
    all_obs2 = learned_model.last_token_probabilities_batch(
        test_sequences, suffixes)

    absolute_error_sum = 0
    for i in range(len(all_obs1)):
        obs1 = np.asarray(all_obs1[i])
        obs2 = np.asarray(all_obs2[i])
        absolute_error_sum += np.sum(np.abs(obs1-obs2))

    return absolute_error_sum / len(test_sequences)
