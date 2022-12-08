import time
import random
from AutoComplete.autocomplete import first_n_correspondent_words
from Levenshtein.search_1distance import search1DistanceWord


def calculate_fst_search_time(fst, word):
    start_time = time.time()
    first_n_correspondent_words(fst, word)
    return time.time() - start_time







def generate_test_words(fst_file, number_of_words):
    file = open(fst_file, encoding='latin-1')
    lines_indexes = []
    
    for i in range(number_of_words):
        lines_indexes.append(random.randomint(0,100000))
    
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
    
def calculate_levenshtein_time(fst, word):

    start_time = time.time()
    search1DistanceWord(word,fst)
    return time.time() - start_time     
