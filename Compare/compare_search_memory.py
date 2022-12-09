import os
import psutil

from FSTInterpreter.fst import FST
from AutoComplete.autocomplete import first_n_correspondent_words
from Levenshtein.search_1distance import search1DistanceWord
from HashTable.hash_table import txt2hashtable, dict_constains_word

def process_memory():
    process = psutil.Process(os.getpid())
    mem_info = process.memory_info()
    return mem_info.rss

def profile(func):
    def wrapper(*args, **kwargs):
        mem_before = process_memory()
        result = func(*args, **kwargs)
        mem_after = process_memory()
        memory_usage = mem_after-mem_before
        memory_usage_mega = memory_usage/(2**20)

        print("{}: Memória consumida: {:,} bytes = {:.2f} megabytes".format(
        func.__name__,
        memory_usage,
        memory_usage_mega
        )
        )
        return result
    return wrapper

@profile
def get_FST_memory():
    fst = FST("fst.json")
    first_n_correspondent_words(fst, "word")


@profile
def get_levenshtein_memory():
    fst = FST("fst.json")
    search1DistanceWord("word", fst)


@profile
def get_hash_table_memory():
    dict, list = txt2hashtable("dictionary.txt")
    dict_constains_word(dict, list, "word")