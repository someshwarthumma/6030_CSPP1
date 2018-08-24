'''
To announce the winner of the game for the given inputs
'''
def transpose_of_matrix(matrix):
    '''
    To tranpose the given matrix
    '''
    tr_matrix = []
    string_ = "0 0 0"
    for i in range(3):
        tr_matrix.append(string_.split())
    temp_matrix = matrix[:]
    for i in range(3):
        for j in range(3):
            tr_matrix[j][i] = temp_matrix[i][j]
    return tr_matrix

def valid_game(matrix):
    '''
    To check for a valid game
    '''
    temp = 0
    for i in range(3):
        if len(set(matrix[i])) == 1:
            temp = temp +1
    temp_matrix = transpose_of_matrix(matrix)
    for i in range(3):
        if len(set(temp_matrix[i])) == 1:
            temp = temp +1
    # if temp <= 1:
    #     return True
    # return False
    return bool(temp)


def who_is_winner(matrix):
    '''
    To return the winner of the game
    '''
    if matrix[0][0] == matrix[1][1] == matrix[2][2] == 'x':
        return 'x'
    if matrix[0][0] == matrix[1][1] == matrix[2][2] == 'o':
        return 'o'
    if matrix[0][2] == matrix[1][1] == matrix[2][0] == 'x':
        return 'x'
    if matrix[0][2] == matrix[1][1] == matrix[2][0] == 'o':
        return 'o'
    for i in range(3):
        if list(set(matrix[i])) == ['x'] and len(set(matrix[i])) == 1:
            return 'x'
        if list(set(matrix[i])) == ['o'] and len(set(matrix[i])) == 1:
            return 'o'
    temp_matrix = transpose_of_matrix(matrix)
    for i in range(3):
        if list(set(temp_matrix[i])) == ['x'] and len(set(temp_matrix[i])) == 1:
            return 'x'
        if list(set(temp_matrix[i])) == ['o'] and len(set(temp_matrix[i])) == 1:
            return 'o'
    return "draw"

def read_input():
    '''
    To read the input matrix
    '''
    matrix = []
    for _ in range(3):
        matrix.append(input().split())
    return matrix

def valid_input(matrix):
    '''
    To check for valid input
    '''
    for i in range(3):
        for j in range(3):
            if matrix[i][j] in "xo.":
                pass
            else:
                return False
    return True

def main():
    '''
    Initialisation
    '''
    matrix = read_input()
    if not valid_input(matrix):
        print("invalid input")
    else:
        if valid_game(matrix):
            print(who_is_winner(matrix))
        else:
            print("invalid game")
if __name__ == '__main__':
    main()
