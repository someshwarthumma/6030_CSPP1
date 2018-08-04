'''
Replace all the special characters(!, @, #, $, %, ^, &, *) in a given string with a space.
example : ab!@#cd is the input, the output is ab   cd
Output has three spaces, which are to be replaced with these special characters
'''
def main():
    '''
    Replace all the special characters(!, @, #, $, %, ^, &, *) in a given string with a space.
    '''
    str_input = input()
    temp = ""#Temporary variable
    for variable in str_input:
        #if the character in variable is a special character then append a space
        if variable in "!@#$%^&*":
            temp = temp+" "
        #else append the same
        else:
            temp = temp+variable
    print(temp)
if __name__ == "__main__":
    main()
