'''# Exercise: Is In
# Write a Python function, isIn(char, string), that takes in two arguments a character and String and returns the isIn(char, string) which retuns a boolean value.
'''
def is_in(char,string):
    '''
    char: a single character
    string: an alphabetized string
    
    returns: True if char is in string; False otherwise
    '''
    length =len(string)
    if length ==0:
        return False
    if length ==1:
        if char == string[0]:
            return True
        else:
            return False
    else:
        mid=len(string)//2
        if char==string[mid]:
            return True
        elif char<string[mid]:
            return is_in(char, string[:mid])
        else:
            return is_in(char, string[mid:])

def main():
    '''To check weather the given character is present in a string'''
    data = input()
    data = data.split()
    stri = sorted(data[1])
    print(is_in((data[0][0]), stri))


if __name__== "__main__":
    main()