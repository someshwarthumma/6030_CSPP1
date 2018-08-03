'''To guess the Number '''
given_num=input("Please think of a number !")
print("Enter h if the showed number is higher than your number,l if showed number is lower and c if it equls")
print("Is the number 50?")
low_vlaue=0
high_value=100
mid=((low_vlaue+high_value)//2)
while True :
    num=input("Enter your Response: ")
    if num=="h":
        high_value=mid
    if num=="l":
        low_vlaue=mid
    if num=="c":
        break
    mid=((low_vlaue+high_value)//2)
    print("is your guess "+str(mid))
print(" Your number is: "+str(mid))