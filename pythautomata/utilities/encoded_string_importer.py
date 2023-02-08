from re import findall, match
from typing import Any

from pythautomata.base_types.alphabet import Alphabet
from pythautomata.base_types.state import State
from pythautomata.base_types.symbol import SymbolStr
from pythautomata.exceptions.model_importing_error import ModelImportingError


class EncodedStringImporter:

    @staticmethod
    def import_automata_attributes(code):
        fileLines = str.split(code, '\n')
        modelName = fileLines[0]
        alphabet = EncodedStringImporter.__get_alphabet_from_data(
            fileLines[1:4])
        del fileLines[:4]
        statesByName, initialStates, currentIndex = EncodedStringImporter.__get_states_from_data(
            fileLines)
        del fileLines[:currentIndex + 3]
        EncodedStringImporter.__get_transitions_from_data(
            fileLines, alphabet, statesByName)

        return alphabet, initialStates, set(statesByName.values()), modelName

    @staticmethod
    def __get_alphabet_from_data(fileLines: list) -> Alphabet:
        if not match(r"^(?:Alphabet: )\[(?:'([^']+)')(?:, (?:'([^']+)')+)*\]$", fileLines[0]):
            raise ModelImportingError()
        return Alphabet(set(SymbolStr(symbol)
                            for symbol in findall(r"(?:'([^']+)')", fileLines[0])))

    @staticmethod
    def __get_states_from_data(fileLines: list) -> tuple[dict[Any, State], frozenset[State], int]:
        statesByName = {}
        initialStates = set()
        currentIndex = 0

        while not fileLines[currentIndex].isspace() and not fileLines[currentIndex] == '':
            currentLine = fileLines[currentIndex]
            stateData = match(
                r"^\t(?:\"([^\"]+)\")( \(Initial\))?( \(Final\))?$", currentLine)

            if not stateData:
                raise ModelImportingError()

            name = stateData.group(1)
            isInitial = stateData.group(2) is not None
            isFinal = stateData.group(3) is not None

            state = State(name, isFinal)
            statesByName[name] = state
            if isInitial:
                initialStates.add(state)
            currentIndex += 1
        return statesByName, frozenset(initialStates), currentIndex

    @staticmethod
    def __get_transitions_from_data(fileLines: list, alphabet: Alphabet, statesByName: dict):
        currentIndex = 0
        while True:
            originName = match(
                r"^(?:\"([^\"]+)\"):$", fileLines[currentIndex])
            origin = statesByName[originName.group(1)]
            currentIndex += 1

            while True:
                if currentIndex >= len(fileLines):
                    return

                currentLine = fileLines[currentIndex]
                transitionData = match(
                    r"^\t(?:'([^']+)')(?: -> )\[(?:\"([^\"]+)\")(?:, (?:\"([^\"]+)\"))*\]$", currentLine)
                if not transitionData:
                    break
                symbol = alphabet[transitionData.group(1)]
                destinations = set(statesByName[name]
                                   for name in findall(r"(?:\"([^\"]+)\")", currentLine))
                origin.transitions[symbol] = destinations
                currentIndex += 1
