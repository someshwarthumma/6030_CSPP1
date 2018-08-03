# Write a python program to find the square root of the given number
# using approximation method

# testcase 1
# input: 25
# output: 4.999999999999998

# testcase 2
# input: 49
# output: 6.999999999999991

def main():
    given_number = int(input())
    epsilon = 0.01
    guess = 0
    step = 0.1
    while guess < given_number:
        if abs(guess**2 - given_number) < epsilon:
            break
        guess = guess+step 
    #guess = round(guess)
    #if (guess**2-given_number) < epsilon:
    print(str(guess))
    #else :
    #print(str(guess))
    # your code starts here

if __name__== "__main__":
    main()
