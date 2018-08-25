'''
Write a python program to read multiple lines of text input and store the input into a string.
'''

def main():
    '''
    Initialisation
    To read the text from a given file
    and print the file onto the console
    '''
    text = []
    number_of_line = int(input())
    for var in range(number_of_line):
        text.append(input())
    for var in text:
        print(var)

if __name__ == '__main__':
    main()
