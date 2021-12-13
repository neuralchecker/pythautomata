from re import match, compile
from enum import Enum
from collections import namedtuple
from pythautomata.base_types.alphabet import Alphabet
from random import randrange, random, choice, seed
from pythautomata.regular_expressions.regular_expression import RegularExpression

class ProductionRules(Enum):
    CONCATENATION = ""
    CHOICE = "|"
    KLEENE_STAR = "*"


RuleApplication = namedtuple(
    'RuleApplication', 'rule dependencies')


class RegularExpressionGenerator():

    __possible_applications = (RuleApplication(ProductionRules.CONCATENATION, (None, None)),
                               RuleApplication(ProductionRules.CHOICE, (None, None)),
                               RuleApplication(ProductionRules.KLEENE_STAR, (None,)))

    def __init__(self, alphabet: Alphabet):        
        self._alphabet = alphabet
        seed()
    
    
    @property
    def alphabet(self) -> Alphabet:
        return self._alphabet

    def generate_regular_expression_with(self,iterations: int, some_seed:int = 42):
        seed(some_seed)
        if self.alphabet is None or len(self.alphabet) < 2:
            raise ValueError("Alphabet must not be None, and have at least two symbols")

        expression = None
        for _ in range(iterations):
            expression = self.__add_production_rule_to(expression)
        result = self.__convert_to_string(expression, list(self.alphabet.symbols))
        pattern = None
        if iterations > 0 and expression.rule == ProductionRules.CHOICE:
             pattern = compile(f"^(?:{result[0]})$")
        pattern = compile(f"^{result[0]}$")
        return RegularExpression(alphabet = self.alphabet, pattern = pattern)

    def __add_production_rule_to(self, result, noKleeneStar=False):
        if result is None:
            ruleToAdd = self.__choose_random_rule_with(noKleeneStar)
            return RuleApplication(ruleToAdd.rule, list(ruleToAdd.dependencies))
        else:
            index = randrange(len(result.dependencies))
            selected = result.dependencies[index]
            noKleeneStar = result.rule == ProductionRules.KLEENE_STAR or \
                noKleeneStar and result.rule == ProductionRules.CHOICE
            result.dependencies[index] = self.__add_production_rule_to(selected, noKleeneStar)
            return result

    def __choose_random_rule_with(self, noKleeneStar):
        roll = random()
        if noKleeneStar:
            index = 0 if roll < 0.66666 else 1
        else:
            index = 0 if roll < 0.556 else 1 if roll < 0.834 else 2
        return self.__possible_applications[index]

    def __convert_to_string(self, result, symbols: list):
        if result is None:
            return str(choice(symbols)), None

        symbol = result.rule.value
        if result.rule == ProductionRules.KLEENE_STAR:
            child, childRule = self.__convert_to_string(result.dependencies[0], symbols)
            substring = self.__get_substring_for(child, result.rule, childRule)
            return f"{substring}{symbol}?", result.rule
        else:
            left, leftRule = self.__convert_to_string(result.dependencies[0], symbols)
            right, rightRule = self.__convert_to_string(result.dependencies[1], symbols)
            leftSubstring = self.__get_substring_for(left, result.rule, leftRule)
            rightSubstring = self.__get_substring_for(right, result.rule, rightRule)
            return f"{leftSubstring}{symbol}{rightSubstring}", result.rule

    def __get_substring_for(self, child: str, rule: ProductionRules, child_rule: ProductionRules):
        if rule == ProductionRules.CONCATENATION and child_rule == ProductionRules.CHOICE or \
                rule == ProductionRules.KLEENE_STAR and child_rule is not None:
            return f"(?:{child})"
        return child