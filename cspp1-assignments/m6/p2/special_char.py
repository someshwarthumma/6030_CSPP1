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
        if variable in "!@#$%^&*":#if the character in variable is a special character then append a space
            temp = temp+" "
        else:
            temp = temp+variable#else append the same
    print(temp)
if __name__ == "__main__":
    main()
