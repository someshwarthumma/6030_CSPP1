'''
Write a python program to read multiple lines of text input and store the input into a string.
'''

def main():
    text = []
    number_of_line = int(input())
    for var in range(number_of_line):
        text.append(input())
    for var in text:
        print(var)

if __name__ == '__main__':
    main()
