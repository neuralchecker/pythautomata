from typing import Any
from pythautomata.base_types.sequence import Sequence
from pythautomata.base_types.alphabet import Alphabet
from pythautomata.base_types.symbol import Symbol
from pythautomata.abstract.probabilistic_model import ProbabilisticModel
import numpy as np


class ComposedProbabilisticModel(ProbabilisticModel):
    def __init__(self, models: list, alphabet: Alphabet, reduction_function=lambda *args: np.mean(args), verbose: bool = False):
        """
        Probabilistic model consisting of composing a series of probabilistic models

        Args:
            models (list): A list of models to process
            alphabet (Alphabet): The alphabet of the models
            reduction_function (_type_, optional): A function for reducing the output of the models. Defaults to lambda*args:np.mean(args).            
        """
        # init object
        self._models = models
        self._alphabet = alphabet
        self._reduction_function = reduction_function
        self._terminal_symbol = models[0].terminal_symbol

        self._verify_reduction_function(reduction_function, models)
        self._verify_models(models)

    @property
    def terminal_symbol(self) -> Symbol:
        return self._terminal_symbol

    @property
    def alphabet(self) -> Alphabet:
        return self._alphabet

    @property
    def name(self) -> str:
        name = "Composed_model:"
        for model in self._models:
            name = name + " - " + model.name
        return name

    def _verify_reduction_function(self, fun, models: list):
        try:
            args = map(lambda x: True, models)
            fun(*args)
        except TypeError:
            print("Reduction function should accept as many parameters as len(models)")
            raise

    def _verify_models(self, models: Any):
        all_verify = all(map(lambda x: hasattr(
            x, "last_token_probability"), models))
        assert all_verify, "Make sure all the models are of the class ProbabilisticModel"
        for model in models:
            assert model.terminal_symbol == self.terminal_symbol, "All models should share the terminal symbol"

    def sequence_probability(self, sequence: Sequence) -> float:
        return self._reduction_function(*map(lambda x: x.sequence_probability(sequence), self._models))

    def log_sequence_probability(self, sequence: Sequence) -> float:
        raise NotImplementedError

    def last_token_probability(self, sequence: Sequence) -> float:
        return self._reduction_function(*map(lambda x: x.last_token_probability(sequence), self._models))
