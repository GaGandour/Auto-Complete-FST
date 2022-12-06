from FSTInterpreter.fst import FST

def first_n_correspondent_words(fst: FST, string: str, initial_state: int = 0, n: int = 10):
    id = initial_state
    state = fst.fst_states[id]
    valid_word = True
    i = -1
    while valid_word and i < len(string) - 1:
        i += 1
        if string[i] not in state.transitions:
            valid_word = False
            break
        id = state.transitions[string[i]]
        state = fst.fst_states[id]

    if not valid_word:
        return []

    return dfs_first_n(fst, string, i+1, id, string, [], n)

def dfs_first_n(fst: FST, input: str, i: int, state_id: int, current_output: str, outputs, n: int):
    if (len(outputs) >= n):
        return outputs
    if fst.fst_states[state_id].is_final:
        outputs.append(current_output)
    for key in fst.fst_states[state_id].transitions:
        value = fst.fst_states[state_id].transitions[key]
        dfs_first_n(fst, input, i + 1, value, current_output+key, outputs, n)
    
    return outputs

