#Matrix Determinant (https://www.codewars.com/kata/52a382ee44408cea2500074c)
# Write a function that accepts a square matrix (N x N 2D array) and returns the determinant of the matrix.

# How to take the determinant of a matrix -- it is simplest to start with the smallest cases:

# A 1x1 matrix |a| has determinant a.

# A 2x2 matrix [ [a, b], [c, d] ] or

# |a  b|
# |c  d|
# has determinant: a*d - b*c.

# The determinant of an n x n sized matrix is calculated by reducing the problem to the calculation of the determinants of n matrices ofn-1 x n-1 size.

# For the 3x3 case, [ [a, b, c], [d, e, f], [g, h, i] ] or

# |a b c|  
# |d e f|  
# |g h i|  
# the determinant is: a * det(a_minor) - b * det(b_minor) + c * det(c_minor) where det(a_minor) refers to taking the determinant of the 2x2 matrix created by crossing out the row and column in which the element a occurs:

# |- - -|
# |- e f|
# |- h i|  
# Note the alternation of signs.

# The determinant of larger matrices are calculated analogously, e.g. if M is a 4x4 matrix with first row [a, b, c, d], then:

# det(M) = a * det(a_minor) - b * det(b_minor) + c * det(c_minor) - d * det(d_minor)





def minors(matrix):
    small_matrices = []  # list of all minors
    for i in range(len(matrix)):  # counter to exclude columns
        a = []  # list of required columns for each minor
        for j in range(len(matrix)):
            if j != i:
                a.append(j)
        b = []  # minor
        for line in range(1, len(matrix)):
            micro_line = []
            for column in a:
                micro_line.append(matrix[line][column])
            b.append(micro_line)
        small_matrices.append(b)
    return small_matrices


def determinant(matrix):
    if len(matrix) == 2:
        return matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0]
    elif len(matrix) == 1:
        return matrix[0][0]
    else:
        minors_of_matrix = minors(matrix)
        det = 0
        for i in range(len(matrix)):
            if i % 2 == 0:
                det += matrix[0][i] * determinant(minors_of_matrix[i])
            else:
                det -= matrix[0][i] * determinant(minors_of_matrix[i])
        return det