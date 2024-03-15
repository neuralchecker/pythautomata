from pythautomata.base_types.moore_state import MooreState
from pythautomata.automata.moore_machine_automaton import MooreMachineAutomaton


class MooreMachineMinimizer():

    def __init__(self, moore_machine: MooreMachineAutomaton):
        self.moore_machine = moore_machine

    def minimize(self) -> MooreMachineAutomaton:
        """
        Minimizes Moore Machine.

        Returns
        -------
        MooreMachineAutomaton
            A minimized Moore Machine
        """
        final_eq_class, equivalence_class_0 = self._get_final_eq_class()

        if self._is_minimizable(final_eq_class):
            minimalDfa = self._convert_to_moore_machine(
                final_eq_class, equivalence_class_0)
            minimalDfa._exporting_strategies = self.moore_machine._exporting_strategies
            return minimalDfa
        else:
            return self.moore_machine

    def _get_final_eq_class(self):
        equivalence_class_0 = []
        for output_symbol in self.moore_machine.output_alphabet.symbols:
            output_symbol_states = self._get_output_symbol_states(output_symbol)
            equivalence_class_0.append(output_symbol_states)

        equivalence_classes = [equivalence_class_0]
        current_iteration = 0
        finished = False

        while not finished:
            new_eq_class = self._next_eq_class_from(
                equivalence_classes[current_iteration])
            current_iteration += 1
            equivalence_classes.append(new_eq_class)
            finished = self._eq_class_iterations_finished(
                equivalence_classes, current_iteration)
        final_eq_class = equivalence_classes[current_iteration]
        return final_eq_class, equivalence_class_0

    def _is_minimizable(self, final_eq_class) -> bool:
        minimizable = not len(final_eq_class) == len(
            [state for state in self.moore_machine.states if not state == self.moore_machine.hole])
        return minimizable

    def _convert_to_moore_machine(self, eq_class, eq_class_0):
        self._remove_hole_from_eq_class(eq_class)
        new_states = []

        # Load states
        for index, partition in enumerate(eq_class):
            partition_state = MooreState(str(index), partition[0].value)
            new_states.append(partition_state)

        # Add transitions
        for index, partition in enumerate(eq_class):
            state_of_partition = new_states[index]
            for symbol in self.moore_machine.alphabet.symbols:
                next_state = self._get_next_state(symbol, partition)
                if not next_state == self.moore_machine.hole:
                    # If its a hole, nothing needs to be done; hole transitions
                    # are added automatically on DFA construction.
                    number_of_part = self._get_num_of_partition_of_state(
                        next_state, eq_class)
                    actual_next_state = new_states[number_of_part]
                    state_of_partition.add_transition(
                        symbol, actual_next_state)

        number_of_part_of_init_state = self._get_num_of_partition_of_state(
            self.moore_machine.initial_state, eq_class)
        actual_initial_state = new_states[number_of_part_of_init_state]

        return MooreMachineAutomaton(self.moore_machine.alphabet, self.moore_machine.output_alphabet, actual_initial_state, set(new_states), comparator=self.moore_machine.comparator, hole = self.moore_machine.hole)

    def _remove_hole_from_eq_class(self, eq_class):
        for partition in eq_class:
            for state in partition:
                if state == self.moore_machine.hole:
                    if len(partition) == 1:
                        eq_class.remove(partition)
                    else:
                        partition.remove(state)

    def _get_num_of_partition_of_state(self, state, eq_class):
        for index, partition in enumerate(eq_class):
            if state in partition:
                return index

    def _get_next_state(self, symbol, partition):
        for state in partition:
            next_state = next(iter(state.next_states_for(symbol)))
            if not next_state == next_state.hole:
                return next_state
        return next_state

    def _next_eq_class_from(self, equivalence_class):
        new_eq_class = []
        for partition in equivalence_class:
            if len(partition) == 1:
                # Non partitionable
                new_eq_class.append(partition)
            else:
                number_of_states = len(partition)

                not_distinguishable_table = self._create_false_filled_square_table(
                    number_of_states)
                states = [state for state in partition]

                # Skip first element
                for i in range(1, number_of_states):
                    # Only below diagonal
                    for j in range(0, i):
                        not_distinguishable_table[i][j] = not self._are_distinguishable(
                            states[i], states[j], equivalence_class)

                self._fill_diag_and_make_symetric(not_distinguishable_table)
                eq_class_from_table = self._create_eq_class_from_table(
                    not_distinguishable_table, states)
                new_eq_class.extend(eq_class_from_table)
        return new_eq_class

    def _create_eq_class_from_table(self, non_distinguishable_table, states):
        moved_state_lst = [False for row in non_distinguishable_table]
        eq_class = []
        for i, row in enumerate(non_distinguishable_table):
            if not moved_state_lst[i]:
                partition = []
                for j, non_distinguishable in enumerate(row):
                    if non_distinguishable:
                        partition.append(states[j])
                        moved_state_lst[j] = True
                if len(partition) > 0:
                    eq_class.append(partition)
        return eq_class

    def _fill_diag_and_make_symetric(self, table):
        for i in range(0, len(table)):
            for j in range(0, len(table[0])):
                if i == j:
                    table[i][j] = True
                else:
                    table[i][j] = table[j][i]

    def _are_distinguishable(self, state1, state2, equivalence_class):
        distinguishable = False
        for symbol in self.moore_machine.alphabet.symbols:

            next_state_1 = next(iter(state1.next_states_for(symbol)))
            next_state_2 = next(iter(state2.next_states_for(symbol)))

            partition_where_1_belongs = self._get_partition_where_it_belongs(
                next_state_1, equivalence_class)
            partition_where_2_belongs = self._get_partition_where_it_belongs(
                next_state_2, equivalence_class)

            if not partition_where_1_belongs == partition_where_2_belongs:
                distinguishable = True
                break
        return distinguishable

    def _get_partition_where_it_belongs(self, state, partitions):
        if state == self.moore_machine.hole:
            return None
        for partition in partitions:
            if state in partition:
                return partition

    def _create_false_filled_square_table(self, dimension: int) -> list[list[bool]]:
        return [[False for x in range(dimension)]
                for x in range(dimension)]

    def _eq_class_iterations_finished(self, equivalence_classes: list, current_iteration: int) -> bool:
        are_same_equivalence_class = len(equivalence_classes[current_iteration]) == len(
            equivalence_classes[current_iteration - 1])
        return are_same_equivalence_class

    def _get_output_symbol_states(self, output_symbol) -> list[MooreState]:
        return [x for x in self.moore_machine.states if x.value == output_symbol]

