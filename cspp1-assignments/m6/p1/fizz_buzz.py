'''
Write a short program that prints each number from 1 to num on a new line.
For each multiple of 3, print "Fizz" instead of the number.
For each multiple of 5, print "Buzz" instead of the number.
For numbers which are multiples of both 3 and 5, print "FizzBuzz" instead of the number.
'''
def main():
    ''' To print "Fizz" for multiple of 3,"Buzz" for multiple of 5
    and "FizzBuzz" for multiple of both 3 and 5'''
    num = int(input())
    var = 1
    while var <= num:
        if var%3 == 0:#print Fizz for multiple of 3
            print("Fizz")
        if var%5 == 0:#print Buzz for a multiple of 5
            print("Buzz")
        if var%3 != 0 and var%5 != 0:#else print the number
            print(var)
        var = var+1
if __name__ == "__main__":
    main()
