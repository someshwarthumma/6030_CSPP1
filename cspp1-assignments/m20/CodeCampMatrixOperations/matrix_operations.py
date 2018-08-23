
def mult_matrix(m1, m2,d1, d2):
    '''
        check if the matrix1 columns = matrix2 rows
        mult the matrices and return the result matrix
        print an error message if the matrix shapes are not valid for mult
        and return None
        error message should be "Error: Matrix shapes invalid for mult"
    '''
    multiplication = []
    if d1[1] != d2[0]:
        print("Error: Matrix shapes invalid for mult")
        raise Exception("Error: Matrix shapes invalid for mult")
    for i in range(int(d1[1])):
        temp = []
        for j in range(int(d2[0])):
            temp.append(j)
        multiplication.append(temp)
    print(multiplication)    
    for i in range(int(d1[0])):
        for j in range(int(d2[1])):
            for k in range(int(d2[0])):
                multiplication[i][j] += int(m1[i][k])*int(m2[k][j])
    print("Multipication: ",multiplication)
     




    pass

def add_matrix(m1, m2,d1, d2):
    '''
        check if the matrix shapes are similar
        add the matrices and return the result matrix
        print an error message if the matrix shapes are not valid for addition
        and return None
        error message should be "Error: Matrix shapes invalid for addition"
    '''
    if d1[0] != d2[0] or d1[1] != d2[1]:
        print("Error: Matrix shapes invalid for addition")
        raise Exception("Error: Matrix shapes invalid for addition")
    addition = [] 
    for i in range(int(d1[0])):
        temp = []
        for j in range(int(d1[1])):
            print("m1[i][j]",m1[i][j])
            print("m2[i][j]",m2[i][j])
            temp.append(int(m1[i][j])+int(m2[i][j]))
            print("temp: ",temp)
        addition.append(temp)
        print("addition: ",addition)
    return addition

def read_matrix(dimensions):
    '''
        read the matrix dimensions from input
        create a list of lists and read the numbers into it
        in case there are not enough numbers given in the input
        print an error message and return None
        error message should be "Error: Invalid input for the matrix"
    '''
    rows = int(dimensions[0])
    columns = int(dimensions[1])
    matrix = []
    #print("rows: "+str(type(rows)),"columns: "+str(type(columns)))
    for i in range(rows):
        colum_data = input()
        if len(colum_data) == 0:
            raise Exception("Error: Invalid input for the matrix")
        colum_data = colum_data.split(" ")
        if len(colum_data) != columns:
            raise Exception("Error: Invalid input for the matrix")
        matrix.append(colum_data)
    return matrix

def main():
    # read matrix 1
    dimensions1 = input()
    dimensions1 = dimensions1.split(',')
    matrix1 = read_matrix(dimensions1)
    print("matrix1: ",matrix1)
    # read matrix 2
    dimensions2 = input()
    dimensions2 = dimensions2.split(',')
    matrix2 = read_matrix(dimensions2)
    print("matrix2: ",matrix2)
    # add matrix 1 and matrix 2
    addition = add_matrix(matrix1,matrix2,dimensions1,dimensions2)
    # multiply matrix 1 and matrix 2
    multiplication = mult_matrix(matrix1,matrix2,dimensions1,dimensions2)
    pass

if __name__ == '__main__':
    main()
