'''Given a  number int_input, find the product of all the digits'''
def main():
    '''To display the product of all the digits in a given number'''
    int_input = int(input())
    flag=0
    if int_input < 0:
        flag = 1
        str_input=str(int_input)
        str_input=str_input[1:]
    else:
        str_input=str(int_input)
        str_input=str_input[0:]
    temp2 = 0
    temp1 = 1
    #if input >= 1 then perform while loop 
    for var in str_input:
        temp2=int(var)
        temp1 = temp1*temp2
    if int_input == 0 :
        print(temp2)
    else:
        if flag == 1:
            temp1 = -temp1
            print(temp1)
        else:
            print(temp1)
if __name__ == "__main__":
    main()
