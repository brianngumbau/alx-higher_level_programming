#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    newmatrix = matrix.copy()

    for a in range(len(matrix)):
        newmatrix[a] = list(map(lambda x: x**2, matrix[a]))

    return (newmatrix)
