import random
def join_list(list_to_join,with_spaces=True):
    """
    joins a list of strings together into one string
    Args:
        string (str): a list of strings
    Returns:
        string: the list items joined in a string
    """
    if type(list_to_join) == type([]):
        new_string = ""
        for i in list_to_join:
            #new_string+=(i+' ')
            if with_spaces: new_string+=(i+' ')
            else: new_string+=(i)
        return new_string
    else: return list_to_join

def lowercase(string):
    """
    string which will be turned into all lowercase
    Args:
        string (str): the string to become lowercase
    Returns:
        string: the string as all lowercase characters
    Raises:
        TypeError: If the input is not a string
    """
    if type(string) != type('a'): raise TypeError(f'Input type must be a string, not {type(string).__name__}')    # raises error if wrong type is inputted
    upper_string = ""
    for char in string:
        if ord(char) >= 65 and ord(char) <= 90: 
            upper_string+=chr(ord(char)+32)
        else:upper_string+=char
    return upper_string

def uppercase(string):
    """
    string which will be turned into all uppercase
    Args:
        string (str): the string to become uppercase
    Returns:
        string: the string as all uppercase characters
    Raises:
        TypeError: If the input is not a string
    """
    if type(string) != type('a'): raise TypeError(f'Input type must be a string, not {type(string).__name__}')    # raises error if wrong type is inputted
    upper_string = ""
    for char in string:
        if ord(char) >= 97 and ord(char) <= 122: 
            upper_string+=chr(ord(char)-32)
        else:upper_string+=char
    return upper_string

def count_character(string,char):
    """
    counts the frequency of a specific character in a string.
    Args:
        string (str): string which will be counted for a specific character
        char (str): character which will be counted in the string
    Returns:
        int: frequency of that character in the string
    Raises:
        TypeError: If the input is not a string
    """
    if type(string) != type('a'): raise TypeError(f'Input type must be a string, not {type(string).__name__}')    # raises error if wrong type is inputted
    x=0
    for i in string:
        if i == char:
            x+=1
    return x

def get_vowels(word,full_dict=False):
    """
    takes a full name and returns the last name.
    Args:
        word (str): word which the vowels are counted
        full_dict (bool): determines if vowels with vlaue 0 should be returned too
    Returns:
        dict: a dictionary of all the vowels and their frequency in the str
            optional variable full_dict determines if it should include the vowels
            with value 0 in the returned dictionary
        string: returns the last name if the name contains one.
    Raises:
        TypeError: If the input is not a string
    """
    if type(word) != type('a'): raise TypeError(f'Input type must be a string, not {type(word).__name__}')    # raises error if wrong type is inputted
    vowels = {'a':0,'e':0,'i':0,'o':0,'u':0,'y':0}
    for i in lowercase(word):
        if i in vowels.keys(): vowels[i] +=1
    if full_dict: return vowels
    else: return {key: value for key, value in vowels.items() if value != 0}

def get_consonants(word,full_dict=False):
    """
    takes a full name and returns the last name.
    Args:
        word (str): word which the consonants are counted
        full_dict (bool): determines if consonants with vlaue 0 should be returned too
    Returns:
        dict: a dictionary of all the consonants and their frequency in the str
            optional variable full_dict determines if it should include the consonants
            with value 0 in the returned dictionary
        string: returns the last name if the name contains one.
    Raises:
        TypeError: If the input is not a string
    """
    if type(word) != type('a'): raise TypeError(f'Input type must be a string, not {type(word).__name__}')    # raises error if wrong type is inputted
    consonants = {'b':0,'c':0,'d':0,'f':0,'g':0,'h':0,'j':0,'k':0,'l':0,'m':0,'n':0,'p':0,'q':0,'r':0,'s':0,'t':0,'v':0,'w':0,'x':0,'z':0}
    for i in lowercase(word):
        if i in consonants.keys(): consonants[i] +=1
    if full_dict: return consonants
    else:
        return {key: value for key, value in consonants.items() if value != 0}

def reverse(word):
    """
    takes a string and reverses it.
    Args:
        word (str): the string that is being reversed
    Returns:
        string: returns the reversed word
    """
    return word[::-1]

def get_first_name(name):
    """
    takes a full name and returns the first name.
    Args:
        name (str): full name which may contain a first name to get
    Returns:
        none: returns none if name doesn't contain a first name.
        string: returns the first name if the name contains one.
    Raises:
        TypeError: If the input is not a string
    """
    if type(name) != type('a'): raise TypeError(f'Input type must be a string, not {type(name).__name__}')    # raises error if wrong type is inputted
    name = lowercase(name).split(' ')
    if contains_title(name):
        if len(name) == 2:
            return None
        else:
            return name[1]
    else:
        return name[0]

def get_last_name(name):
    """
    takes a full name and returns the last name.
    Args:
        name (str): full name which may contain a last name to get
    Returns:
        none: returns none if name doesn't contain a last name.
        string: returns the last name if the name contains one.
    Raises:
        TypeError: If the input is not a string
    """
    if type(name) == type(None):
        return None
    if type(name) != type('a'): raise TypeError(f'Input type must be a string, not {type(name).__name__}')    # raises error if wrong type is inputted
    name = lowercase(name).split(' ')
    if len(name) != 1:
        return name[-1]
    else: return None

def get_middle_names(name):
    """
    takes a name and returns a list of all the middle names in it
    Args:
        name (str): full name which will be checked for middle names
    Returns:
        list: list of strings as middle names (empty list if none)
    Raises:
        TypeError: If the input is not a string
    """
    if type(name) != type('a'): raise TypeError(f'Input type must be a string, not {type(name).__name__}')    # raises error if wrong type is inputted
    name = lowercase(name).split(' ')
    if len(name) < 3:
        return []
    else:
        if contains_title(name):
            if len(name) <4:
                return []
            else: return name[2:len(name)-1:]
        else: return name[1:len(name)-1:]

def contains_title(name):
    """
    takes a name and returns true if it contains a title
    Args:
        name (str): full name which will be checked for a title
    Returns:
        bool: true if name contains a title, false if not
    """
    titles = ['dr','dr.','mr','mr.','ms','mrs','mrs.','miss']
    name = lowercase(join_list(name)).split(' ')
    return name[0] in titles

def last_name_contains_hyphen(name):
    """
    takes a name and returns true if last name has a hyphen.
    Args:
        name (str): name which will be checked for hyphen.
    Returns:
        bool: true if last name contains hyphen
    Raises:
        TypeError: If the input is not a string
    """
    if type(name) != type('a'): raise TypeError(f'Input type must be a string, not {type(name).__name__}')    # raises error if wrong type is inputted
    if get_last_name(name) != None:
        return '-' in get_last_name(name)
    else: return False
def randomize_name(name):
    """
    Args:
        name (str): the name which will be randomized
    Returns:
        str: randomizes the positions of each character in the name
    Raises:
        none
    """
    scrambled_name = list(name)
    random.shuffle(scrambled_name)
    return join_list(scrambled_name,False)

def is_first_name_palindrome(name):
    """
    takes a name and returns true if name is a palindrome and false if not.
    Args:
        name (str): name which will be checked for a palindrome.
    Returns:
        bool: true if name is a palindrome and false if not.
    Raises:
        TypeError: If the input is not a string
    """
    if type(name) != type('a'): raise TypeError(f'Input type must be a string, not {type(name).__name__}')    # raises error if wrong type is inputted
    return get_first_name(name) == get_first_name(name)[::-1]

def get_initials(name):
    """
    takes a name as an input and returns a string with the initials of that name.
    Args:
        name (str): The name which will be used to get the initials
    Returns:
        str: String with the first character of each part of the name (excluding titles)
    Raises:
        TypeError: If the input is not a string
    """
    if type(name) != type('a'): raise TypeError(f'Input type must be a string, not {type(name).__name__}')    # raises error if wrong type is inputted
    initials = ''
    if get_first_name(name)!=None: initials+=get_first_name(name)[0]
    for i in get_middle_names(name): initials+=i[0]
    if get_last_name(name)!=None: initials+=get_last_name(name)[0]
    return initials

def get_sorted_first_name(name):
    """
    takes a name as an input and returns that name with all the characters sorted by ascii value
    Args:
        name (str): The name which will be sorted
    Returns:
        str: String with the characters of initial name sorted by ascii value
    Raises:
        TypeError: If the input is not a string
    """
    if type(name) != type('a'): raise TypeError(f'Input type must be a string, not {type(name).__name__}')    # raises error if wrong type is inputted

    sorted_list = list(name)
    sorted_list.sort()
    sorted_name = ''
    for c in sorted_list:
        sorted_name+=c
    return sorted_name


#print(get_sorted_first_name("freddrick figglebottom junior"))
#print(get_sorted_first_name(9))


#print(type(0).__name__)
#print()
#name=9
#if type(name) != type('a'): raise TypeError(f'Input type must be a string, not {type(name).__name__}')
#check_if_valid(9)
#print(int('a'))