'''# Write a python program to find the square root of the given number'''
def main():
    '''This is to find the square root given number '''
    num = int(input())
    epsilon = 0.01
    mid = num/2
    low = 0
    high = num
    while abs(mid**2-num) >= epsilon:
        if mid**2 < num:
            low = mid
        else: 
            high = mid  
        mid = (low+high)/2 
    print(str(mid))
if __name__ == "__main__":
    main()
