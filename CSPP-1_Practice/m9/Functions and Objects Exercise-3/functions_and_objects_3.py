#Exercise : Function and Objects Exercise-3
#Implement a function that converts the given testList = [1, -4, 8, -9] into [1, 16, 64, 81]

def square(var):
    '''
    :param var: int
    return: int , square of the given number

    '''
    var = var*var
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
    data = input()
    data = data.split()
    list1 = []
    for j in data:
        list1.append(int(j))
    print(apply_to_each(list1, square))

if __name__== "__main__":
    main()