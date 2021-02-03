from abstract.model_exporting_strategy import ModelExportingStrategy


class EncodedFileExportingStrategy(ModelExportingStrategy):

    def export(self, model, path=None):
        path = self.get_path_for(path, model)
        path = str(path)
        fileObject = open(path + ".ef", "w+", encoding="utf-8")

        fileObject.write("Alphabet: [")
        fileObject.write(
            ", ".join(map(lambda symbol: f"'{str(symbol)}'", sorted(model.alphabet.symbols))))

        fileObject.write("]\n\nStates:")
        sortedStates = sorted(model.states, key=lambda state: state.name)
        for state in sortedStates:
            fileObject.write(f"\n\t\"{state.name}\"")
            if state in model.initial_states:
                fileObject.write(" (Initial)")
            if state.is_final:
                fileObject.write(" (Final)")

        fileObject.write("\n\nTransitions:\n\n")
        fileObject.write("\n".join(map(self._get_all_transitions_lines_for,
                                       sortedStates)))
        fileObject.close()

    def _get_all_transitions_lines_for(self, state):
        if not state.transitions:
            return ""
        sortedTransitions = sorted(state.transitions.items())
        transitionsLines = "\n\t".join(
            map(self._get_one_symbol_transitions_lines_for,
                sortedTransitions))
        return f"\"{state.name}\":\n\t{transitionsLines}"

    def _get_one_symbol_transitions_lines_for(self, item):
        substring = ", ".join(
            map(lambda next_state: f"\"{next_state.name}\"", item[1]))
        return f"'{str(item[0])}' -> [{substring}]"
