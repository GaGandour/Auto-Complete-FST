import os
import psutil

from FSTInterpreter.fst import FST
from AutoComplete.autocomplete import first_n_correspondent_words
from Levenshtein.search_1distance import first_n_1distance_words
from Levenshtein.levenshtein import LevenshteinAutomaton

def process_memory():
    process = psutil.Process(os.getpid())
    mem_info = process.memory_info()
    return mem_info.rss

def profile(func):
    def wrapper(*args, **kwargs):
        mem_before = process_memory()
        result = func(*args, **kwargs)
        mem_after = process_memory()
        print("{}: Memória consumida: {:,} bytes".format(
        func.__name__,
        mem_before, mem_after, mem_after - mem_before))
        return result
    return wrapper

@profile
def get_FST_memory():
    fst = FST("fst.json")
    first_n_correspondent_words(fst, "word")

@profile
def get_levenshtein_memory():
    fst = FST("fst.json")
    levenshtein = LevenshteinAutomaton("")
    first_n_correspondent_words(fst, "word")
    first_n_1distance_words(fst, )

    