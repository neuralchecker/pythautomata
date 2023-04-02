from typing import Any
from pythautomata.base_types.sequence import Sequence
from pythautomata.base_types.alphabet import Alphabet
from pythautomata.abstract.boolean_model import BooleanModel


class ComposedBooleanModel(BooleanModel):
    def __init__(self, models: list, alphabet: Alphabet, reduction_function=lambda *args: all(args), verbose: bool = False):
        """
        Boolean model consisting of composing a series of different boolean models

        Args:
            models (list): A list of models to process
            alphabet (Alphabet): The alphabet of the models
            reduction_function (_type_, optional): A function for reducing the output of the models. Defaults to lambda*args:all(args).            
        """
        self._verify_reduction_function(reduction_function, models)
        self._verify_models(models)

        # init object
        self._models = models
        self._alphabet = alphabet
        self._reduction_function = reduction_function

    @property
    def alphabet(self) -> Alphabet:
        return self._alphabet

    @property
    def name(self) -> str:
        name = "Composed_model:"
        for model in self._models:
            name = name + " - " + model.name
        return name

    def accepts(self, sequence: Sequence) -> bool:
        accepts = list(map(lambda x: x.accepts(sequence), self._models))
        result = self._reduction_function(*accepts)
        return result

    def accepts_batch(self, sequences) -> list[bool]:
        for model in self._models:
            assert (hasattr(model, 'accepts_batch'))
        results = list(map(lambda x: x.accepts_batch(sequences), self._models))
        intermediate_results = zip(*results)
        return list(map(lambda x: self._reduction_function(*x), intermediate_results))

    def _verify_reduction_function(self, fun, models: list):
        try:
            args = map(lambda x: True, models)
            fun(*args)
        except TypeError:
            print("Reduction function should accept as many parameters as len(models)")
            raise

    def _verify_models(self, models: Any):
        all_verify = all(map(lambda x: hasattr(x, "accepts"), models))
        if not all_verify:
            print("Make sure all the models are of the class BooleanModel")
        assert all_verify
