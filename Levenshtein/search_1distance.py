#from Levenshtein.levenshtein import LevenshteinAutomaton
from FSTInterpreter.fst import FST
from Levenshtein.levenshtein import LevenshteinAutomaton

# FSTInterpreter\fst.py

def first_n_1distance_words(fst: FST, levenshtein: LevenshteinAutomaton, string: str, initial_state: int = 0, n: int = 10):
    id = initial_state
    zero_state = levenshtein.start()

    return dfs_first_n(fst, string, 0, id,levenshtein,zero_state, '', [], n)

def dfs_first_n(fst: FST, input: str, i: int, fst_state_id: int,levenshtein: LevenshteinAutomaton ,levenshtein_state, current_output: str, outputs, n: int):
    if (len(outputs) >= n):
        return outputs
    if fst.fst_states[fst_state_id].is_final and levenshtein.is_match(levenshtein_state):
        outputs.append(current_output)
    
    for key in fst.fst_states[fst_state_id].transitions:
        value = fst.fst_states[fst_state_id].transitions[key]
        next_state = levenshtein.step(levenshtein_state,key)
        if levenshtein.can_match(next_state):
            dfs_first_n(fst, input, i + 1, value,levenshtein,next_state, current_output+key, outputs, n)
    
    return outputs



def search1DistanceWord(word,fst,N):
    search1Automata = LevenshteinAutomaton(word,1,fst)
    return first_n_1distance_words(fst,search1Automata,word,n=N)

 
 

# respostas = search1DistanceWord('aug',"fst.json",10)
# print(respostas)
