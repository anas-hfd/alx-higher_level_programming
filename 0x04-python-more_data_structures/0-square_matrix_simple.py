#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    rws = len(matrix)
    cls = len(matrix[0])
    new_matrix = [[0] * cls for _ in range(rws)]

    for i in range(rws):
        for j in range(cls):
            new_matrix[i][j] = matrix[i][j] ** 2

    return new_matrix
