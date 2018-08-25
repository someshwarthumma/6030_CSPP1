'''
Write a function to tokenize a given string and return a dictionary with the frequency of
each word
'''
import re

def tokenize(string):
    '''
    :param input is a list of list 
    return a dictionary with word frequency
    '''
    dictionary = {}
    for list_ in string:
        for word in list_:
            if word in dictionary.keys():
                dictionary[word] = dictionary[word] + 1

            else:
                dictionary[word] = 1
    return dictionary
            
def main():
    '''
    Initialisation for Tokenise the given string
    '''
    string = []
    no_of_lines = int(input())
    for _ in range(no_of_lines):
        temp_input = input()
        regex = re.compile("[^A-Za-z0-9 ]")
        temp_input = regex.sub('', temp_input)
        string.append(temp_input.split())
    print(tokenize(string))


if __name__ == '__main__':
    main()
