import time
from AutoComplete.autocomplete import first_n_correspondent_words
<<<<<<< HEAD
from HashTable.hash_table import dict_constains_word
=======
from Levenshtein.search_1distance import search1DistanceWord
>>>>>>> e3381beb69e3dec9edf249968f55987671c84ce4


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


<<<<<<< HEAD
def calculate_levenshtein_time():
    pass



def calculate_hash_table_(dict, list, word):
    start_time = time.time()
    dict_constains_word(dict, list, word)
    return time.time() - start_time
=======


def calculate_levenshtein_time(fst, word):

    start_time = time.time()
    search1DistanceWord(word,fst)
    return time.time() - start_time     
>>>>>>> e3381beb69e3dec9edf249968f55987671c84ce4
