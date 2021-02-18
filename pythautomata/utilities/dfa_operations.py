from automata.deterministic_finite_automaton import DeterministicFiniteAutomaton as DFA
from model_comparators.dfa_comparison_strategy import DFAComparisonStrategy as AutomataComparator
from base_types.state import State

#TODO: ADD DOCSTRINGS

def join_DFAs(dfa1: DFA, dfa2: DFA) -> DFA:
    """
    Function implementing DFA join. 
    The join between two DFAs is a new DFA that recognizes only words belonging to languages of both DFAs at the same time.

    Args:
        dfa1 (DFA): A DFA.
        dfa2 (DFA): Another DFA.

    Returns:
        DFA: A DFA containing words that are accepted by dfa1 and dfa2 at the same time.
    """
    _check_alphabets(dfa1, dfa2)  

    initial_pair = _get_initial_pair(dfa1, dfa2)
    join_DFA_initial_state =  _pair_to_state_join(initial_pair)    
    join_DFA_alphabet = dfa1.alphabet

    pairs_to_visit = [initial_pair]
    visited_pairs = set()
    result_states = dict()
    result_states[join_DFA_initial_state.name]= join_DFA_initial_state
    while len(pairs_to_visit) > 0:
        pair = pairs_to_visit[0]
        new_state = _pair_to_state_join(pair)
        
        if(new_state.name not in result_states.keys()):
            result_states[new_state.name]= new_state
        else:
            new_state = result_states[new_state.name]

        for symbol in join_DFA_alphabet.symbols:
            next_pair = (pair[0].next_state_for(
                symbol), pair[1].next_state_for(symbol))

            next_state = _pair_to_state_join(next_pair)

            if next_pair not in pairs_to_visit and next_pair not in visited_pairs:                    
                pairs_to_visit.append(next_pair)
                result_states[next_state.name] = next_state
            else:
                next_state = result_states[next_state.name]  

            new_state.add_transition(symbol,next_state)
        
        pairs_to_visit.remove(pair)
        visited_pairs.add(pair)

    #Update the initial state, so it has the transitions
    join_DFA_initial_state = result_states[join_DFA_initial_state.name]
    join_DFA_states = set(result_states.values())
    comparator = AutomataComparator()
    resulting_DFA = DFA(join_DFA_alphabet,join_DFA_initial_state,join_DFA_states, comparator = comparator)
    return resulting_DFA

def union_DFAs(dfa1: DFA, dfa2: DFA) -> DFA:
    """
    Function implementing DFA union. 
    The union between two DFAs is a new DFA that recognizes words belonging to languages of any of the DFAs.

    Args:
        dfa1 (DFA): A DFA.
        dfa2 (DFA): Another DFA.

    Returns:
        DFA: A DFA containing words that are accepted by dfa1 or dfa2.
    """
    _check_alphabets(dfa1, dfa2)    

    initial_pair = _get_initial_pair(dfa1, dfa2)
    union_DFA_initial_state =  _pair_to_state_union(initial_pair)    
    union_DFA_alphabet = dfa1.alphabet

    pairs_to_visit = [initial_pair]
    visited_pairs = set()
    result_states = dict()
    result_states[union_DFA_initial_state.name]= union_DFA_initial_state
    while len(pairs_to_visit) > 0:
        pair = pairs_to_visit[0]
        new_state = _pair_to_state_union(pair)
        
        if(new_state.name not in result_states.keys()):
            result_states[new_state.name]= new_state
        else:
            new_state = result_states[new_state.name]

        for symbol in union_DFA_alphabet.symbols:
            next_pair = (pair[0].next_state_for(
                symbol), pair[1].next_state_for(symbol))

            next_state = _pair_to_state_union(next_pair)

            if next_pair not in pairs_to_visit and next_pair not in visited_pairs:                    
                pairs_to_visit.append(next_pair)
                result_states[next_state.name] = next_state
            else:
                next_state = result_states[next_state.name]  

            new_state.add_transition(symbol,next_state)
        
        pairs_to_visit.remove(pair)
        visited_pairs.add(pair)

    #Update the initial state, so it has the transitions
    union_DFA_initial_states = result_states[union_DFA_initial_state.name]
    union_DFA_states = set(result_states.values())
    comparator = AutomataComparator()
    resulting_DFA = DFA(union_DFA_alphabet,union_DFA_initial_states,union_DFA_states, comparator = comparator)
    return resulting_DFA

def join_DFA_set(dfaSet: set[DFA]) -> DFA:
    """
    Function implementing DFA join of a whole set of DFAs. 
    The join between DFAs is a new DFA that recognizes words belonging to languages of all of the DFAs at the same time.

    Args:
        dfaSet (set[DFA]): A set of DFAs.

    Returns:
        DFA: A DFA containing words that are accepted by all of the DFAs in the set.
    """
    listDFAs = list(dfaSet)
    result = listDFAs[0]
    for dfa in listDFAs:
        result = join_DFAs(result, dfa)
    return result    

def union_DFA_set(dfaSet: set[DFA]) -> DFA:
    """
    Function implementing DFA union of a whole set of DFAs. 
    The union between DFAs is a new DFA that recognizes words belonging to languages of any of the DFAs.

    Args:
        dfaSet (set[DFA]): A set of DFAs.

    Returns:
        DFA: A DFA containing words that are accepted by any of the DFAs in the set.
    """

    listDFAs = list(dfaSet)
    result = listDFAs[0]
    for dfa in listDFAs:
        result = union_DFAs(result, dfa)
    return result   

def _get_initial_pair(dfa1: DFA, dfa2:DFA) -> tuple[State, State]:
    initial_state1 = dfa1.initial_state
    initial_state2 = dfa2.initial_state
    return (initial_state1, initial_state2)    

def _check_alphabets(dfa1: DFA, dfa2:DFA) -> None:
    if dfa1.alphabet != dfa2.alphabet:
            raise ValueError("Alphabets are not equivalent.")   

def _pair_to_state_join(pair: tuple[State, State]) -> State:
    state0 = pair[0]    
    state1 = pair[1]
    new_state_is_final = state0.is_final and state1.is_final
    new_state_name = state0.name+state1.name
    new_state = State(new_state_name,new_state_is_final)
    return new_state
   
def _pair_to_state_union(pair: tuple[State, State]) -> State:
    state0 = pair[0]    
    state1 = pair[1]
    new_state_is_final = state0.is_final or state1.is_final
    new_state_name = state0.name+state1.name
    new_state = State(new_state_name,new_state_is_final)
    return new_state    

