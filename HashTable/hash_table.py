

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

def dict_constains_word(dictionary, dictio2list, word):
        if word in  dictionary:
            index = dictionary.get(word)
            answer = []
            
            answer.append(word)
            
        # tenho que cortar as proximas palavras da lista e comparar com a palavra dada, se bater, printa a próxima em questão.
            iterator = index + 1
            if iterator <= len(dictio2list)-1:
                answer.append( dictio2list[index+1])
            return answer
        else:
            return []

(dictionary,list) = txt2hashtable('dictionary.txt')

word = 'jan'
print(dict_constains_word(dictionary,list,word))