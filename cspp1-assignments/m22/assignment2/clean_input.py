'''
Write a function to clean up a given string by removing the special characters and retain
alphabets in both upper and lower case and numbers.
'''
import re

def clean_string(string):
    '''
    To clean the unwanted letters from a given string
    '''
    regex = re.compile("[^A-Za-z0-9]")
    return regex.sub('', string)

def main():
    '''
    Initialisation for reading the string
    '''
    string = input()
    print(clean_string(string))

if __name__ == '__main__':
    main()
