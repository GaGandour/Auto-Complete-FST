import time
from AutoComplete.autocomplete import first_n_correspondent_words


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




def calculate_levenshtein_time():
    pass
