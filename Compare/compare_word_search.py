import time
from AutoComplete.autocomplete import first_n_correspondent_words
from FSTInterpreter.fst import FST


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








def calculate_levenshtein_time():
    pass


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