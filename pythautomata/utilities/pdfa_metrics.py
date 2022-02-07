from pythautomata.abstract.probabilistic_model import ProbabilisticModel
from pythautomata.base_types.alphabet import Alphabet
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

    for word in test_sequences:
        obs1 = np.asarray(
            [target_model.last_token_probabilities(word, suffixes)])
        obs2 = np.asarray(
            [learned_model.last_token_probabilities(word, suffixes)])
        ndcg_word_score = ndcg_score(obs1, obs2, k=k)
        ndcg.append(ndcg_word_score)

    return np.mean(np.array(ndcg))


def wer_avg(target_model: ProbabilisticModel, learned_model: ProbabilisticModel, test_sequences: list[Sequence]):
    suffixes = list()
    suffixes.append(Sequence() + learned_model.terminal_symbol)
    wer = 0

    for symbol in learned_model.alphabet.symbols:
        suffixes.append(Sequence(symbol))

    for word in test_sequences:
        obs1 = np.array(
            target_model.last_token_probabilities(word, suffixes))
        obs2 = np.array(
            learned_model.last_token_probabilities(word, suffixes))
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

    for word in test_sequences:
        obs1 = np.asarray(
            [target_model.last_token_probabilities(word, suffixes)])
        obs2 = np.asarray(
            [learned_model.last_token_probabilities(word, suffixes)])

        if not pdfa_utils.are_within_tolerance_limit(obs1, obs2, tolerance):
            errorCount += 1

    return errorCount


def out_of_partition_elements(target_model: ProbabilisticModel, learned_model: ProbabilisticModel, test_sequences: list[Sequence], partitions: int):
    suffixes = list()
    errorCount = 0
    suffixes.append(Sequence() + learned_model.terminal_symbol)
    for symbol in learned_model.alphabet.symbols:
        suffixes.append(Sequence(symbol))

    for word in test_sequences:
        obs1 = np.asarray(
            target_model.last_token_probabilities(word, suffixes))
        obs2 = np.asarray(
            learned_model.last_token_probabilities(word, suffixes))
        result = pdfa_utils.are_in_same_partition(obs1, obs2, partitions)
        if not pdfa_utils.are_in_same_partition(obs1, obs2, partitions):
            errorCount += 1

    return errorCount
