'''# Write a python program to find the square root of the given number'''
def main():
    '''To find the square root of the given number'''
    given_number = int(input())
    epsilon = 0.01
    guess = 0
    step = 0.1
    while guess < given_number:
        if abs(guess**2 - given_number) < epsilon:
            break
        guess = guess+step 
    print(str(guess))
if __name__ == "__main__":
    main()
