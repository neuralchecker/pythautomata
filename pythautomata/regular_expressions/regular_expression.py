from re import match, compile
from typing import Pattern
import uuid
from pythautomata.base_types.alphabet import Alphabet
from pythautomata.base_types.sequence import Sequence
from pythautomata.abstract.boolean_model import BooleanModel

class RegularExpression(BooleanModel):

    def __init__(self, alphabet: Alphabet, pattern: Pattern, name:str = None):        
        self._alphabet = alphabet
        self._pattern = pattern
        self._name = 'REGEX - ' + str(uuid.uuid4().hex) if name is None else name
    
    @property
    def alphabet(self) -> Alphabet:
        return self._alphabet
    
    @property
    def name(self):
        return self._name
    
    def accepts(self, sequence: Sequence) -> bool:
        return bool(self._pattern.match( "".join(map(str, sequence.value))))
    


