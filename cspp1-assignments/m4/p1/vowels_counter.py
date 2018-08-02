'''
#Assume s is a string of lower case characters.

#Write a program that counts up the number of vowels contained in the string s. Valid vowels are: 'a', 'e', 'i', 'o', and 'u'. For example, if s = 'azcbobobegghakl', your program should print:

#Number of vowels: 5
'''
def main()
"""This program is used to count the number of Vowels in a string. """
    var1_ = input()
    num = 0
    for var in var1_:
         if var in ('a', 'e', 'i', 'o', 'u'):
            num += 1
    print(num)
if __name__ == "__main__":
    main()
