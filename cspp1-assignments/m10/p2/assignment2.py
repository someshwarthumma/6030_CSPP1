'''
Exercise : Assignment-2
implement the function hangman, which takes one parameter - the secretWord 
the user is to guess. This starts up an interactive game of Hangman between 
the user and the computer. Be sure you take advantage of the three helper functions, 
isWordGuessed, getGuessedWord, and getAvailableLetters, 
that you've defined in the previous part.
'''

# -----------------------------------
# Helper code
# You don't need to understand this helper code,
# but you will have to know how to use the functions
# (so be sure to read the docstrings!)

import random

WORDLIST_FILENAME = "words.txt"

def loadWords():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print("Loading word list from file...")
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r')
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = line.split()
    print("  ", len(wordlist), "words loaded.")
    return wordlist

def chooseWord(wordlist):
    """
    wordlist (list): list of words (strings)

    Returns a word from wordlist at random
    """
    return random.choice(wordlist)

# end of helper code
# -----------------------------------

# Load the list of words into the variable wordlist
# so that it can be accessed from anywhere in the program
wordlist = loadWords()

def is_word_guessed(secret_word, letters_guessed):
    '''
    secret_word: string, the word the user is guessing
    letters_guessed: list, what letters have been guessed so far
    returns: boolean, True if all the letters of secret_word are in letters_guessed;
      False otherwise
    '''
    flag = len(secret_word)
    for var in secret_word:
        if var in letters_guessed:
            flag = flag-1
    if flag == 0:
        return True
    return False

def get_guessed_word(secret_word, letters_guessed):
    '''
    secret_word: string, the word the user is guessing
    letters_guessed: list, what letters have been guessed so far
    returns: string, comprised of letters and underscores that represents
      what letters in secret_word have been guessed so far.
    '''
    string = ""
    for var in secret_word:
        if var in letters_guessed:
            string = string + var
        else:
            string = string + "_"
    return string

def get_available_letters(letters_guessed):
    '''
    :param letters_guessed: list, what letters have been guessed so far
    returns: string, comprised of letters that represents what letters have not
      yet been guessed.
    '''
    available_letters = "abcdefghijklmnopqrstuvwxyz"
    for each_element_in_available_letter in available_letters:
        if each_element_in_available_letter in letters_guessed:
            available_letters = available_letters.replace(each_element_in_available_letter, '')
    return available_letters

def is_letter_in_letter_guessed(guess,letters_guessed):
    '''
    :param guess: character 
    letters_guessed: list
    retrun: boolean

    '''
    if guess in letters_guessed:
        return True
    else:
        return False

def hangman(secret_word):
    '''
    secretWord: string, the secret word to guess.

    Starts up an interactive game of Hangman.'''
    print("I am thinking of a word that is "+str(len(secret_word))+" letters long.")
    iterator = 8
    flag_2 = False
    letters_guessed=[]
    while iterator >= 1 and flag_2==False:
        print("You have "+str(iterator)+" guesses left.")
        print("Available letters: "+get_available_letters(letters_guessed))
        guess= input("Please guess a letter: ").lower()
        flag=is_letter_in_letter_guessed(guess,letters_guessed)
        if flag!=True:
            letters_guessed.append(guess)
        if flag:
            print("Oops! You've already guessed that letter: "+get_guessed_word(secret_word, letters_guessed))
        else:
            if guess in secret_word: 
                print("Good guess: "+get_guessed_word(secret_word, letters_guessed))
                if get_guessed_word(secret_word, letters_guessed)==secret_word:
                    flag_2= True
            else:
                print("Oops! That letter is not in my word:"+get_guessed_word(secret_word, letters_guessed))
                iterator -= 1  
        print("********************************************* ")

        
    if get_guessed_word(secret_word, letters_guessed)==secret_word:
        print("Wow! You won the game.")
    else:
        print("Oops you Lost the game! ")
    print("secretword is :"+secret_word)

def main():
    '''
    Main function for the given program
    
    When you've completed your hangman function, uncomment these two lines
    and run this file to test! (hint: you might want to pick your own
    secretWord while you're testing)
    '''
    print("Welcome to the game, Hangman!")
    secretword = chooseWord(wordlist).lower()
    #secretWord = "secre.lower()
    hangman(secretword)

if __name__ == "__main__":
    main()
