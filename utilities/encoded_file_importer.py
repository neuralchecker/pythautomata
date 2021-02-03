from glob import iglob
from base_types.state import State
from re import findall, match, search
from base_types.symbol import SymbolStr
from base_types.alphabet import Alphabet
from abstract.finite_automaton import FiniteAutomaton
from exceptions.model_importing_error import ModelImportingError
from typing import Any


class EncodedFileImporter:

    @staticmethod
    def import_generated_automata(path:str=None):
        if path is None:
            path = "target_models"

        for fileName in iglob(path + "/**/*.ef", recursive=True):
            file = open(fileName)
            fileLines = file.readlines()
            file.close()

            alphabet = EncodedFileImporter._get_alphabet_from_data(fileLines)
            del fileLines[:3]
            statesByName, initialStates, currentIndex = EncodedFileImporter._get_states_from_data(
                fileLines)
            del fileLines[:currentIndex + 3]
            EncodedFileImporter._get_transitions_from_data(
                fileLines, alphabet, statesByName)

            modelNameResults = search(r"(?:\\.*\\([^\\]+) -)", fileName)
            modelName = modelNameResults.group(1) if modelNameResults is not None else fileName
            yield FiniteAutomaton(alphabet, initialStates,
                                  set(statesByName.values()), modelName)

    @staticmethod
    def _get_alphabet_from_data(fileLines: list) -> Alphabet:
        if not match(r"^(?:Alphabet: )\[(?:'([^']+)')(?:, (?:'([^']+)')+)*\]$", fileLines[0]):
            raise ModelImportingError()
        return Alphabet(frozenset(SymbolStr(symbol)
                            for symbol in findall(r"(?:'([^']+)')", fileLines[0])))

    @staticmethod
    def _get_states_from_data(fileLines: list) -> tuple[dict[Any, State], frozenset[State], int]:
        statesByName = {}
        initialStates = set()
        currentIndex = 0

        while not fileLines[currentIndex].isspace():
            currentLine = fileLines[currentIndex]
            stateData = match(
                r"^\t(?:\"([^\"]+)\")( \(Initial\))?( \(Final\))?\n$", currentLine)

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
    def _get_transitions_from_data(fileLines: list, alphabet: Alphabet, statesByName: dict):
        currentIndex = 0
        while True:
            originName = match(r"^(?:\"([^\"]+)\"):\n$", fileLines[currentIndex])
            #TODO custom exception, hablar con franz
            assert originName is not None
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
