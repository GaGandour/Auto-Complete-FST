import time
from AutoComplete.autocomplete import first_n_correspondent_words
from Levenshtein.search_1distance import search1DistanceWord


def calculate_fst_search_time(fst, word):
    start_time = time.time()
    first_n_correspondent_words(fst, word)
    return time.time() - start_time







def generate_test_words():
    return [
        "Monday",
        "Ariel",
        "Emanuel",
        
    ]




def calculate_levenshtein_time(fst, word):

    start_time = time.time()
    search1DistanceWord(word,fst)
    return time.time() - start_time     
