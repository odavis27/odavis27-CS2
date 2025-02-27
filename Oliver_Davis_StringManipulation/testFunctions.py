from name_functions import *
# note: must be only english alphabet characters
def run_name_functions(name):
    print(f"First name:\n  {get_first_name(name)}\n---------------------------")
    print(f"Last name:\n  {get_last_name(name)}\n---------------------------")
    print(f"Middle names:\n  {get_middle_names(name)}\n---------------------------")
    print(f"Name Contains a title:\n  {contains_title(name)}\n---------------------------")
    print(f"Last Name Contains a hyphen:\n  {last_name_contains_hyphen(name)}\n---------------------------")
    print(f"Random Name:\n  {randomize_name(name)}\n---------------------------")
    print(f"First name is a palindrome:\n  {is_first_name_palindrome(name)}\n---------------------------")
    print(f"Initials:\n  {get_initials(name)}\n---------------------------")
    print(f"First name as sorted characters:\n  {get_sorted_first_name(name)}")

def run_word_functions(word):
    print(f"Word reversed:\n  {reverse(word)}\n---------------------------")
    print("Vowels:")
    vowels = get_vowels(word)
    for i in vowels.keys():
        print(f"  {i}: {vowels[i]}")
    print("---------------------------")
    print("Consonants:")
    consonants = get_consonants(word)
    for i in consonants.keys():
        print(f"  {i}: {consonants[i]}")
    print("---------------------------")
    print(f"Uppercase:\n  {uppercase(word)}\n---------------------------")
    print(f"Lowercase:\n  {lowercase(word)}\n---------------------------")


if __name__ == "__main__":
    inputting = True
    while inputting:
        input_type = lowercase(input("'Word' or 'name'?\n  ")) 
        input_type='name'
        if input_type == 'word':
            word = input("Please insert a word.\n  ")
            print("===============================")
            run_word_functions(word)
            inputting = False
        elif input_type == 'name':
            name = input("Please insert a name.\n  ")
            #name = "dr. racecar j. bartholomeu higgledy smith"
            #name = "freddrick figglebottom junior"
            print("===============================")
            run_name_functions(name)
            inputting = False
        else:
            print('''Please insert only "name" or "word"''')
# Shephard Nicholas OKeeffe III Esq.