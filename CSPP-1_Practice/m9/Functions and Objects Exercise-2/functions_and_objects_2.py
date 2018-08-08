'''
#Exercise : Function and Objects Exercise-2
Implement a function that converts the given
testList = [1, -4, 8, -9] into [2, -3, 9, -8]
'''
def inc(var):
    '''
    increments the given number
    :param var: int 
    :return: int , incremented value
    '''
    var = var +1
    return var
def apply_to_each(L, f):
    '''
    To assgin a value to inc funtion
    :param L=list ,f=inc
    retun: list
    '''
    for i in range(len(L)):
        L[i] = f(L[i])
    return L

def main():
    '''
    Initialisation
    input int
    prints incremented list
    '''
    data = input()
    data = data.split()
    list1 = []
    for j in data:
        list1.append(int(j))
    print(apply_to_each(list1, inc))

if __name__ == "__main__":
    main()
