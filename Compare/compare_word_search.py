import time
import random
from AutoComplete.autocomplete import first_n_correspondent_words
from FSTInterpreter.fst import FST
from HashTable.hash_table import dict_constains_word, txt2hashtable
from Levenshtein.search_1distance import search1DistanceWord


def calculate_fst_search_time(fst, word):
    start_time = time.time()
    first_n_correspondent_words(fst, word)
    return time.time() - start_time


def calculate_hash_table_time(dict, list, word):
    start_time = time.time()
    dict_constains_word(dict, list, word)
    return time.time() - start_time


def calculate_levenshtein_time(fst, word):
    start_time = time.time()
    search1DistanceWord(word,fst)
    return time.time() - start_time


def generate_test_words(dictionary_path, number_of_words):
    file = open(dictionary_path, encoding='latin-1')
    lines_indexes = []
    
    for i in range(number_of_words):
        lines_indexes.append(random.randint(0,100000))
    
    lines_indexes.sort()
    lines_data = []
    
    for i, line in enumerate(file):
        if i in lines_indexes:
            lines_data.append(line.strip())
        elif i > lines_indexes[-1]:
            break
    
    return lines_data
    
    
def generate_test_words_splitted(test_words):
    splitted_words = []
    
    for word in test_words: 
        split_index = random.randint(1,len(word))
        splitted_words.append(word[:split_index])
        
    return splitted_words
    

def compare_time():
    random.seed(42) # 42 is the answer for life, the universe and everything
    fst = FST("fst.json")
    test_words = generate_test_words("dictionary.txt", 100)
    dict, list = txt2hashtable("dictionary.txt")
    splitted_test_words = generate_test_words_splitted(test_words)
    fst_time = sum([calculate_fst_search_time(fst, word) for word in test_words])
    hash_time = sum([calculate_hash_table_time(dict, list, word) for word in test_words])
    levenshtein_time = sum([calculate_levenshtein_time(fst, word) for word in test_words])

    fst_splitted_time = sum([calculate_fst_search_time(fst, word) for word in splitted_test_words])
    hash_splitted_time = sum([calculate_hash_table_time(dict, list, word) for word in splitted_test_words])
    levenshtein_splitted_time = sum([calculate_levenshtein_time(fst, word) for word in splitted_test_words])

    print("Buscas com palavras completas:")
    print("FST: \t\t", fst_time, " segundos")
    print("Hash table: \t", hash_time, " segundos")
    print("Levenshtein: \t", levenshtein_time, " segundos")


    print("\nBuscas com prefixos de palavras:")
    print("FST: \t\t", fst_splitted_time, " segundos")
    print("Hash table: \t", hash_splitted_time, " segundos")
    print("Levenshtein: \t", levenshtein_splitted_time, " segundos")
