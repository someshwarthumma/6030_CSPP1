'''
Given a  number int_input, find the product of all the digits
example: 
	input: 123
	output: 6
'''
def main():
    '''
    To display the product of all the digits in a given number
    '''
    int_input = int(input())
    temp2 = 0
    temp1 = 1
    #if input >= 1 then perform while loop 
    while int_input/10>=1:
    	temp2 = int_input%10
    	temp1 = temp1*temp2
    	int_input = int_input//10
    if int_input == 0 :
        print(temp2)
    else:
    	print(temp1)
if __name__ == "__main__":
    main()
