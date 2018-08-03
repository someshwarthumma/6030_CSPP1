''' Write a python program to find if the given number is a perfect cube or not'''
def main():
    '''This program is to find wheather the given number is perfect cube or not'''
    given_number = int(input())
    guess = 0
    step = 1
    while guess < given_number :
        if abs(guess**3 - given_number) == 0:
            break
        guess = guess+step 
    if (guess**3 - given_number) == 0:
        print(str(given_number)+" is a perfect cube")
    else :
        print(str(given_number)+" is not a perfect cube")
if __name__ == "__main__":
    main()
