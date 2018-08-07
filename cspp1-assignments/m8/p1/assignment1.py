'''# Exercise: Assignment-1
# Write a Python function, factorial(n), that takes in one number and returns the factorial of given number.
# This function takes in one number and returns one number.'''
def factorial(fact):
    '''
    n is positive Integer
    returns: a positive integer, the factorial of n.
    '''
    if fact == 0:
        return 1
    else:
        return fact*factorial(fact-1)
def main():
    '''This function is used to find factorial of number using recursion'''
    fact = input()
    print(factorial(int(fact))) 

if __name__ == "__main__":
    main()
