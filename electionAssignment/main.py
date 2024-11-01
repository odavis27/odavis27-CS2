''' 
Oliver Davis
10/31/2024
Description:
   Program opens chosen text file and creates a csv file with the top x words in the transcript rated by usage.
   if chosen, the program can also display a bar graph of the data
Bugs:
    If more than arround 13 words are chosen from the transcript and then graphed using the bar graph it gets
    very difficult to read as the words begin to overlap because the text size does not scale.
Constaints:
    - can only graph a bar chart
    - cannot properly graph more than arround 13 words
    - 
Instructions:
    There are three variables that are intended to be changed. Beggining on line 27, the way the variables are 
    changed affects how the file runs.
        - file_name: file_name is the name of the file being opened without any file extensions (so no .txt at the end)
        - show_graph: Show graph determines whether the dat should be graphed.
        - words_to_graph: determines how many words should be picked out from the sorted dictionary
Note:
    I gave up on putting it all in one file and even though it doesnt really matter for whatever reason it really annoys me so I split it up.
'''



from get_word_dict import get_word_dict
from graph import graph
#==================
#  Configuration Variables
#------------------
file_name = 'cleaned_trump_speech_transcript'
show_graph = True
words_to_graph = 13
#==================

words_dict = get_word_dict(file_name,words_to_graph)                # get sorted words said as a dictionary with times used as the value

# turn words_dict dictionary into a new csv
with open(f'{file_name}.csv', 'w') as new_csv:                      # open a new csv file as wrtie saving the file as the variable new_csv
    for word in words_dict:                                         
        new_csv.write(word+', '+str(words_dict[word])+'\n')         # write the dictionary line by line properly formated
    new_csv.close()

if show_graph:                                                      # determine whether a graph should be shown
    graph(file_name)                                         # graph the data
