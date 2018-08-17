'''
    Document Distance - A detailed description is given in the PDF
'''
import math
def similarity(dict1, dict2):
    '''
        Compute the document distance as given in the PDF
    '''
    dictionary={}
    keys = set(list(dict1.keys())+list(dict2.keys()))
    for word in keys:
        if len(word)==0:
            keys.remove(word)
    #print(keys)
    for i in keys:
        dictionary[i]=[0,0]
    for i in dict1.keys():
        dictionary[i][0] = dict1[i]
    for i in dict2.keys():
        dictionary[i][1] = dict2[i]
    sum1=0
    term1 = 0
    term2 = 0
    for i in dictionary.values():
        sum1  = sum1 + i[0]*i[1]
        term1 = term1 + i[0]**2
        term2 = term2 + i[1]**2
    distance = sum1/(math.sqrt(term1)*math.sqrt(term2))
    #print(distance)
    return distance

def load_stopwords(filename):
    '''
        loads stop words from a file and returns a dictionary
    '''
    stopwords = {}
    with open(filename, 'r') as filename:
        for line in filename:
            stopwords[line.strip()] = 0
    return stopwords

def clean_up_words(input_file):
    for i in input_file:
        if i in "!@$%^&*()_-+=<>?/.,:;|'~`1234567890":
            input_file=input_file.replace(i, '')
    #print(input_file)
    input_file = input_file.lower()
    input_file = input_file.split()
    #print(input_file)
    if '' in input_file:
        input_file.remove('')
    #print(input_file)
    return input_file

def remove_stopwords(input_list, filename):
    temp = input_list[:]
    for i in temp:
        if i in filename:
            input_list.remove(i)
    #print(input_list)
    return input_list
def word_freq(input_list):
    dictionary = {}
    for i in input_list:
        if i not in dictionary.keys():
            dictionary[i]=input_list.count(i)
    return dictionary

def main():
    '''
        take two inputs and call the similarity function
    '''
    input1 = input()
    input2 = input()
    filename = load_stopwords('stopwords.txt')
    list1 = clean_up_words(input1)
    #print(list1)
    list2 = clean_up_words(input2)
    list1_without_stopword = remove_stopwords(list1, filename)
    list2_without_stopword = remove_stopwords(list2, filename)
    print(list1_without_stopword)
    print(list2_without_stopword)
    dict1 = word_freq(list1_without_stopword)
    dict2 = word_freq(list2_without_stopword)
    print(similarity(dict1, dict2))

if __name__ == '__main__':
    main()
