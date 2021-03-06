'''
Write a function to print a dictionary with the keys in sorted order along with the
frequency of each word. Format of the printing should be one key per line and separate
the key and frequency with a SPACE - SPACE.
'''

def print_dictionary(dictionary):
    '''
    To print the dictionary after sorting in ascending order
    in the format of "key - value"
    '''
    keys = list(dictionary.keys())
    keys.sort()
    for key in keys:
        print(key, "-", dictionary[key])
def main():
    '''
    Initialisation for reading the dictionary
    '''
    dictionary = eval(input())
    print_dictionary(dictionary)

if __name__ == '__main__':
    main()
