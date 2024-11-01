useless_words = ['is','um','the','and','to','of','in','a','is','it','this','that','will','have','are','be','who','you','not','was']
remove_characters = ['.',',','!','?','-','\\','/','@','#','$','%','^','&','*','(',')','{','}','|','~',';']

def get_word_dict(file_name,words_to_graph):
    file = open(file_name+'.txt', "r")
    words_dict = {}
    for line in file:
        #line = line.replace('.','').replace(',','').replace('!','').replace('?','').replace('-','').lower()
        
        for char in remove_characters:
            line = line.replace(char,'')
        line = line.lower().split(' ')
        for word in line:
            if word in words_dict:
                words_dict[word] += 1
            else:
                words_dict[word] = 1
    words_dict.pop('\n', None)
    words_dict.pop('', None)
    
    # sort dictionary then convert sorted list back into a dictionary
    words_dict = dict(sorted(words_dict.items(), key=lambda item: item[1], reverse=True))

    # remove all words that do not carry much weight
    for word in useless_words: 
        # none input included so it doesnt die if the key doesnt exist
        words_dict.pop(word, None)
    print(words_dict)

    top_x_words = dict([(list(words_dict.keys())[i],list(words_dict.values())[i]) for i in range(0,words_to_graph)])
    return top_x_words