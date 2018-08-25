'''
Write a function to clean up a given string by removing the special characters and retain 
alphabets in both upper and lower case and numbers.
'''
import re

def clean_string(string):
    new_string = ""
    for character in string:
        if character in "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890":
            new_string = new_string + character

    return new_string

def main():
    string = input()
    print(clean_string(string))

if __name__ == '__main__':
    main()
