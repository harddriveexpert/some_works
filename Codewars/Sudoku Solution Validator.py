# Sudoku Solution Validator (https://www.codewars.com/kata/529bf0e9bdf7657179000008)
# Sudoku Background

# Sudoku is a game played on a 9x9 grid. The goal of the game is to fill all cells of the grid with digits from 1 to 9, so that each column, each row, and each of the nine 3x3 sub-grids (also known as blocks) contain all of the digits from 1 to 9. 
# (More info at: http://en.wikipedia.org/wiki/Sudoku)

# Sudoku Solution Validator

# Write a function validSolution/ValidateSolution/valid_solution() that accepts a 2D array representing a Sudoku board, and returns true if it is a valid solution, or false otherwise. The cells of the sudoku board may also contain 0's, which will represent empty cells. Boards containing one or more zeroes are considered to be invalid solutions.

# The board is always 9 cells by 9 cells, and every cell only contains integers from 0 to 9.

# Examples

# validSolution([
#   [5, 3, 4, 6, 7, 8, 9, 1, 2],
#   [6, 7, 2, 1, 9, 5, 3, 4, 8],
#   [1, 9, 8, 3, 4, 2, 5, 6, 7],
#   [8, 5, 9, 7, 6, 1, 4, 2, 3],
#   [4, 2, 6, 8, 5, 3, 7, 9, 1],
#   [7, 1, 3, 9, 2, 4, 8, 5, 6],
#   [9, 6, 1, 5, 3, 7, 2, 8, 4],
#   [2, 8, 7, 4, 1, 9, 6, 3, 5],
#   [3, 4, 5, 2, 8, 6, 1, 7, 9]
# ]); // => true
# validSolution([
#   [5, 3, 4, 6, 7, 8, 9, 1, 2], 
#   [6, 7, 2, 1, 9, 0, 3, 4, 8],
#   [1, 0, 0, 3, 4, 2, 5, 6, 0],
#   [8, 5, 9, 7, 6, 1, 0, 2, 0],
#   [4, 2, 6, 8, 5, 3, 7, 9, 1],
#   [7, 1, 3, 9, 2, 4, 8, 5, 6],
#   [9, 0, 1, 5, 3, 7, 2, 1, 4],
#   [2, 8, 7, 4, 1, 9, 6, 3, 5],
#   [3, 0, 0, 4, 8, 1, 1, 7, 9]
# ]); // => false

def valid_solution(board):
    # checking for the presence of zeros in the matrix
    zeroes = 0
    for i in range(9):
        zeroes += board[i].count(0)
    if zeroes != 0:
        return False
    else:
        # check for the sum of columns
        for i in range(9):
            first_sum = 0
            for j in range(9):
                first_sum += board[j][i]
            if first_sum != 45:
                return False
        # checking the amount of lines
        for i in range(9):
            second_sum = 0
            for j in range(9):
                second_sum += board[i][j]
            if second_sum != 45:
                return False
        for line in range(0, 8, 3):  # start line of block
            for columns in range(0, 8, 3):  # start columns of block
                number_of_signs = 0
                matrix_sum = 0
                matrix = []  # list of block
                for n in range(line, line + 3):  # counter of line of block
                    for i in range(columns, columns + 3):  # counter of columns of block
                        matrix.append(board[n][i])  # creat list of block
                for value in range(1, 10):  # counter for sings
                    number_of_signs += matrix.count(value)
                for e in range(9):
                    matrix_sum += matrix[e]
                if number_of_signs != 9 or matrix_sum != 45:
                    return False
        return True