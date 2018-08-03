# Write a python program to find the square root of the given number
# using approximation method

# testcase 1
# input: 25
# output: 4.999999999999998

# testcase 2
# input: 49
# output: 6.999999999999991

def main():
    num= int(input())
    epsilon = 0.01
    guess = num/2.0
    while (guess*guess-num) >= epsilon and guess <= num:
        guess=guess-(((guess**2)-num)/(2*guess))
    print(guess)
if __name__== "__main__":
    main()
