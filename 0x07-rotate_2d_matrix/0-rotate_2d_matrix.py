#!/usr/bin/python3
"""
matrix, rotate it 90 degrees clockwise.
"""


def rotate_2d_matrix(matrix):
    n = len(matrix)

    # Step 1: Transpose the matrix
    for i in range(n):
        for j in range(i):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

    # Step 2: Reverse each row
    for i in matrix:
        i.reverse()
