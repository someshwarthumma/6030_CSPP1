'''Assume s is a string of lower case characters.

Write a program that prints the longest substring of s in which the letters occur in alphabetical order.
For example, if s = 'azcbobobegghakl', then your program should print

Longest substring in alphabetical order is: beggh

In the case of ties, print the first substring.
For example, if s = 'abcbcd', then your program should print

Longest substring in alphabetical order is: abc.'''

def main():
    string = input()
    end=0
    highest=0
    count=0
    for var in range(len(string)-1):
        if string[var]<= string[var+1]:
            count += 1
            if count > highest:
                highest = count
                end =  var + 1
        else:
            count=0
    num = end-highest
    print(string[num:end+1])
# the input string is in s
# remove pass and start your code here
if __name__ == "__main__":
    main()
