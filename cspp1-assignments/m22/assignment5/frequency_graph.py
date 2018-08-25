'''
Write a function to print a dictionary with the keys in sorted order along with the
frequency of each word. Display the frequency values using “#” as a text based graph
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

def sub(temp):
    '''
    To form a string with # such that it contains given number of # in the formed string
    return a string of #
    '''
    string = ""
    for _ in range(temp):
        string = string + "#"
    return string

def frequency_graph(dictionary):
    '''
    To for the dictinary with appended # in place of value in the given dictionary
    '''
    for key in dictionary:
        temp = dictionary[key]
        dictionary[key] = sub(temp)
    print_dictionary(dictionary)


def main():
    '''
    Initialisation for forming the frequency graph and printing the same
    '''
    dictionary = eval(input())
    frequency_graph(dictionary)

if __name__ == '__main__':
    main()
