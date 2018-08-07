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
    return num%10+sumofdigits(num//10)


def main():
    num = input()
    print(sum_of_digits(int(num)))

if __name__ == "__main__":
    main()

