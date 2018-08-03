'''# Write a python program to find the square root of the given number'''
def main():
    '''to find the square root by newton rapson method'''
    num = int(input())
    epsilon = 0.01
    guess = num/2.0
    while (guess*guess-num) >= epsilon and guess <= num:
        guess = guess-(((guess**2)-num)/(2*guess))
    print(guess)
if __name__ == "__main__":
    main()
