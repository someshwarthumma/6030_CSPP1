'''
    Tiny Search Engine - Part 1 - Build a search index

    In this programming assingment you are given with some text documents as input.
    Complete the program below to build a search index. Don't worry, it is explained below.
    A search index is a python dictionary.
    The keys of this dictionary are words contained in ALL the input text documents.
    The values are a list of documents such that the key/word appears in each document atleast once.
    The document in the list is represented as a tuple.
    The tuple has 2 items. The first item is the document ID.
    Document ID is represented by the list index.
    For example: the document ID of the third document in the list is 2
    The second item of the tuple is the frequency of the word occuring in the document.

    Here is the sample format of the dictionary.
    {
        word1: [(doc_id, frequency),(doc_id, frequency),...],
        word2: [(doc_id, frequency),(doc_id, frequency),...],
        .
        .
    }
'''
import re

# helper function to load the stop words from a file
def load_stopwords(filename):
    '''
        loads stop words from a file and returns a dictionary
    '''

    stopwords = {}
    with open(filename, 'r') as f_stopwords:
        for line in f_stopwords:
            stopwords[line.strip()] = 0
    return stopwords

def clean_up_words(line):
    '''
    To remove the unwanted letters in a line
    '''
    loclist=[]
    stop_words = load_stopwords('stopwords.txt')
    line = line.lower().split()
    for word in line:
        regex = re.compile('[^a-z]')
        every= regex.sub('', word)
        loclist.append(every)

    # temp = line[:]
    # for i in temp:
    #     if i in stop_words:
    #         line.remove(i)
    return loclist



def word_list(docs):
    '''
        Change case to lower and split the words using a SPACE
        Clean up the text by remvoing all the non alphabet characters
        return a list of words
    '''

    word_list = []
    for line in docs:
        word_list = word_list + clean_up_words(line)
    return word_list





def build_search_index(docs):
    '''
        Process the docs step by step as given below
    '''

    # initialize a search index (an empty dictionary)

    stop_words = load_stopwords('stopwords.txt')
    print(docs)
    dictionary = {}
    for index, line in enumerate(docs):
        upd_line = clean_up_words(line)
        for word in set(upd_line):
            if word not in stop_words:
                if word not in dictionary:
                    count_ = upd_line.count(word)
                    temp = (index, count_)
                    dictionary[word] = [temp]
                else:
                    count_ = upd_line.count(word)
                    temp = (index, count_)
                    dictionary[word].append(temp)
    
    '''
    #removing stop words
    wordlist = word_list(docs)
    print("wordlist: ",wordlist)
    for index, line in enumerate(docs):
        print("index:",index)
        print("line :",line)
        line = line.split()
        print("line_split :",line)
        for word in line:
            word=word.lower()
            regex = re.compile('[^a-z]')
            word = regex.sub('', word)
            if word not in load_stopwords('stopwords.txt'):
                line = line.split()
                loclist=[]
                for every in line:
                    regex = re.compile('[^a-z]')
                    every = regex.sub('', every)
                    loclist.append(every)

                if word in wordlist:
                    if word not in dictionary:
                        count_ = loclist.count(word)
                        temp = (index, count_)
                        dictionary[word] = [temp]
                    else:
                        count_ = line.count(word)
                        temp = (index, count_)
                        dictionary[word].append(temp)
    '''

    return dictionary



'''
    # iterate through all the docs

    # keep track of doc_id which is the list index corresponding the document
    # hint: use enumerate to obtain the list index in the for loop

        # clean up doc and tokenize to words list

        # add or update the words of the doc to the search index

    # return search index
'''
#helper function to print the search index
# use this to verify how the search index looks

def print_search_index(index):
    '''
        print the search index
    '''
    keys = sorted(index.keys())
    for key in keys:
        print(key, " - ", index[key])

# main function that loads the docs from files
def main():
    '''
        main function
    '''
    # empty document list
    documents = []
    # iterate for n times
    lines = int(input())
    # iterate through N times and add documents to the list
    for i in range(lines):
        documents.append(input())
        i += 1
    #build_search_index(document)
    # call print to display the search index
    print_search_index(build_search_index(documents))

if __name__ == '__main__':
    main()
