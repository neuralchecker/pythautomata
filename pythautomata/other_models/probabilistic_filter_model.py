from pythautomata.abstract.probabilistic_model import ProbabilisticModel
from pythautomata.base_types.alphabet import Alphabet
from pythautomata.base_types.symbol import SymbolStr
from pythautomata.base_types.sequence import Sequence


class ProbabilisticFilterModel(ProbabilisticModel):

    def __init__(self, model: ProbabilisticModel, max_length: int):
        self._model = model        
        alphabet_symbols = set(self._model.alphabet.symbols)
        #filter_symbol = SymbolStr('#')
        #assert(filter_symbol not in alphabet_symbols)
        #alphabet_symbols.add(filter_symbol)
        self._alphabet = Alphabet(alphabet_symbols)
        self._max_length = max_length
        #self._filter_symbol = filter_symbol
    
    @property
    def name(self) -> str:
        return self._model.name+"_filtered"

    @property
    def terminal_symbol(self) -> SymbolStr:
        return self._model.terminal_symbol
        
    @property
    def alphabet(self) -> Alphabet:
        return self._alphabet

    def sequence_probability(self, sequence: Sequence) -> float:
        raise NotImplementedError

    def log_sequence_probability(self, sequence: Sequence) -> float:
        raise NotImplementedError

    def last_token_probability(self, sequence: Sequence) -> float:
        if len(sequence) > self._max_length:
            if sequence[-1] == self._model.terminal_symbol:
                return 1.0
            else:
                return 0.0
        else:
            return self._model.last_token_probability(sequence)


   
