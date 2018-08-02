'''Assume s is a string of lower case characters.

Write a program that prints the number of times the string 'bob' occurs in s. For example,
if s = 'azcbobobegghakl', then your program should print

Number of times bob occurs is: 2'''

def main():
    """"This program is used to count the 'bob' in a given string."""
    string = input()
    count_ = 0
    for i in range(len(string)-2):
        if (string[i] == "b" and string[i+1] == "o" and string[i+2] == "b"):
            count_ = count_+1
    print(count_)
if __name__== "__main__":
    main()
