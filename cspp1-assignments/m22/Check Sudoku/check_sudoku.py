'''
    Sudoku is a logic-based, combinatorial number-placement puzzle.
    The objective is to fill a 9×9 grid with digits so that
    each column, each row, and each of the nine 3×3 subgrids that compose the grid
    contains all of the digits from 1 to 9.

    Complete the check_sudoku function to check if the given grid
    satisfies all the sudoku rules given in the statement above.
'''
def sub_marix(sudoku, temp1, temp2):
    '''
    To extract a sub matrix
    '''
    sub = []
    for i in range(3):
        i = i + temp1
        for j in range(3):
            j = j + temp2
            sub.append(sudoku[i][j])
    return sub



def transpose_of_matrix(sudoku):
    '''
    to find transpose of a matrix
    '''
    temp_matrix = [['4', '3', '5', '2', '6', '9', '7', '10', '1'], ['6', '8', '2', '5', '7', '1', '4', '9', '3'], ['1', '9', '7', '8', '3', '4', '5', '6', '2'], ['8', '2', '6', '1', '9', '5', '3', '4', '7'], ['3', '7', '4', '6', '8', '2', '9', '1', '5'], ['9', '5', '1', '7', '4', '3', '6', '8', '2'], ['5', '1', '9', '3', '2', '6', '8', '7', '4'], ['2', '4', '8', '9', '5', '7', '1', '3', '6'], ['7', '6', '3', '4', '1', '8', '2', '5', '9']]
    for i in range(9):
        for j in range(9):
            temp_matrix[j][i] = sudoku[i][j]
    return temp_matrix

def check_sudoku(sudoku):
    '''
        Your solution goes here. You may add other helper functions as needed.
        The function has to return True for a valid sudoku grid and false otherwise
    '''
    transpose_matrix = transpose_of_matrix(sudoku)
    for i in range(9):
        if len(set(sudoku[i])) != 9:
            #print("horizontal, line 44")
            #print("Horizontal matrix: ",sudoku[i],"set matrix: ", set(sudoku[i]))
            return False
        if len(set(transpose_matrix[i])) != 9:
            #print("vertical ,line 47")
            #print("vertical matrix: ",transpose_matrixb[i],"set matrix: ", set(transpose_matrix[i]))
            return False
        if len(set(sub_marix(sudoku, 0, 0))) != 9:
            #print("line 50")
            return False
        if len(set(sub_marix(sudoku, 0, 3))) != 9:
            #print("line 53")
            return False
        if len(set(sub_marix(sudoku, 0, 6))) != 9:
            #print("line 56")
            return False
        if len(set(sub_marix(sudoku, 3, 0))) != 9:
            #print("line 51")
            return False
        if len(set(sub_marix(sudoku, 3, 3))) != 9:
            #print("line 62")
            return False
        if len(set(sub_marix(sudoku, 3, 6))) != 9:
            #print("line 65")
            return False
        if len(set(sub_marix(sudoku, 6, 0))) != 9:
            #print("line 68")
            return False
        if len(set(sub_marix(sudoku, 6, 3))) != 9:
            #print("line 71")
            return False
        if len(set(sub_marix(sudoku, 6, 6))) != 9:
            #print("line 74")
            return False
    return True

def main():
    '''
        main function to read input sudoku from console
        call check_sudoku function and # the result to console
    '''

    # initialize empty list
    sudoku = []

    # loop to read 9 lines of input from console
    for _ in range(9):
        # read a line, split it on SPACE and append row to list
        row = input().split(' ')
        sudoku.append(row)
    # call solution function and print result to console
    #print("sudoku:",sudoku)

    print(check_sudoku(sudoku))

if __name__ == '__main__':
    main()
