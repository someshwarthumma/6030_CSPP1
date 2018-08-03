# Write a python program to find if the given number is a perfect cube or not
# using guess and check algorithm

# testcase 1
# Input: 24389
# Output: 24389 is a perfect cube

# testcase 2
# Input: 21950
# Output: 21950 is not a perfect cube

def main():
    # input is captured in s
    given_number = int(input('enterthe number'))
    guess = 0
    step = 1
    while guess < given_number :
        if abs(guess**3 - given_number) == 0:
            break
        guess = guess + step 
    if (guess**3 - given_number) == 0 :
        print(str(guess)+" is a perfect cube")
    else :
        print(str(guess)+" not a perfect cube")
    # watch out for the data type of value stored in s
    # your code starts here

if __name__ == "__main__":
    main()
