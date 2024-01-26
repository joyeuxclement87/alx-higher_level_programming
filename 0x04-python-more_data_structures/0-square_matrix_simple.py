#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    square = []
    for ln in matrix:
        square.append([c**2 for c in ln])
    return square
