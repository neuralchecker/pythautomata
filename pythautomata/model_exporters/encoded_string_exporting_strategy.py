from pythautomata.abstract.model_exporting_strategy import ModelExportingStrategy


class EncodedStringExportingStrategy(ModelExportingStrategy):

    def export(self, model):
        my_string = ""
        my_string += model.name+"\n"
        my_string += "Alphabet: ["
        my_string += ", ".join(
            map(lambda symbol: f"'{str(symbol)}'", sorted(model.alphabet.symbols)))

        my_string += "]\n\nStates:"
        sortedStates = sorted(model.states, key=lambda state: state.name)
        for state in sortedStates:
            my_string += f"\n\t\"{state.name}\""
            if state in model.initial_states:
                my_string += " (Initial)"
            if state.is_final:
                my_string += " (Final)"

        my_string += "\n\nTransitions:\n\n"
        my_string += "\n".join(map(self._get_all_transitions_lines_for,
                                   sortedStates))
        return my_string

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
