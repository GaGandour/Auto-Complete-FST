import time
from AutoComplete.autocomplete import first_n_correspondent_words
from HashTable.hash_table import dict_constains_word


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



def calculate_hash_table_(dict, list, word):
    start_time = time.time()
    dict_constains_word(dict, list, word)
    return time.time() - start_time