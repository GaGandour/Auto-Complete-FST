import time
from AutoComplete.autocomplete import first_n_correspondent_words
from FSTInterpreter.fst import FST
from HashTable.hash_table import dict_constains_word
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
        "Uri",
        "stra",
        "mik"
    ]


def sum_times(times):
    t = 0
    for time in times:
        t += time
    return t

def compare_time():
    fst = FST("fst.json")
    words = generate_test_words()
    fst_times = [calculate_fst_search_time(fst, word) for word in words]
    # hash_times = [calculate_fst_search_time(fst, word) for word in words]
    # levensh_times = [calculate_fst_search_time(fst, word) for word in words]

    fst_time = sum_times(fst_times)
    
    print("FST complete:\t" + "{:.3f}".format(fst_time))


def calculate_hash_table_(dict, list, word):
    start_time = time.time()
    dict_constains_word(dict, list, word)
    return time.time() - start_time



def calculate_levenshtein_time(fst, word):

    start_time = time.time()
    search1DistanceWord(word,fst)
    return time.time() - start_time     
    