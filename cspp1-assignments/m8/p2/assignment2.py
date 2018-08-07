'''# Exercise: Assignment-2
# Write a Python function, sumofdigits
that takes in one number and returns the sum of digits of given number.
'''

def sum_of_digits(num):
    '''
    n is positive Integer
    returns: a positive integer, the sum of digits of n.
    '''
    if num <= 0:
        return 0
    return num%10+sum_of_digits(num//10)


def main():
    '''To find the sum of the digits in a number by recursion'''
    num = input()
    print(sum_of_digits(int(num)))

if __name__ == "__main__":
    main()
