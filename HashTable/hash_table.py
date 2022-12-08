

def txt2hashtable(path):
    dict_file = open(path, "r")
    dict_data = {}
    dict_list = []
    index = 0
    while(True):
        line = dict_file.readline()
        if not line:
            break
        dict_data.update({line.strip():index})
        dict_list.append(line.strip())
        index += 1
    dict_file.close()
    return dict_data,dict_list

def dict_constains_word(dictionary, dictio2list, word, n = 10):
    word_lower = word
    if  word_lower in  dictionary:
        index = dictionary.get( word_lower)
        answer = []
        length = len(word_lower)
        answer.append( word_lower)
        
    # comparing the suffixes of the next words in the file with the given word.
        for i in range(n-1): 
            index = index + 1  
            if  word_lower[:length] == dictio2list[index][:length] and index <= len(dictio2list)-1:
                answer.append( dictio2list[index])
            else:
                break
        return answer
    return []


## How to use the functions

##Constructing the HashTable and the List
#(dictionary,list) = txt2hashtable('dictionary.txt')

##Searched word
#word = 'jan'

## Getting the results
#print(dict_constains_word(dictionary,list,word,6))