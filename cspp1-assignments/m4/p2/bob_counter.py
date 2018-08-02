'''Assume s is a string of lower case characters.

Write a program that prints the number of times the string 'bob' occurs in s. For example, if s = 'azcbobobegghakl', then your program should print

Number of times bob occurs is: 2'''

def main():
    s = input()
    # the input string is in s
    # remove pass and start your code here
    """"This program is used to count the 'bob' in a given string."""
    COUNT = 0
    for i in range(len(s)-2):
        if (s[i] == "b" and s[i+1] == "o" and s[i+2] == "b"):
            COUNT = COUNT+1
    print(COUNT)
if __name__== "__main__":
    main()
