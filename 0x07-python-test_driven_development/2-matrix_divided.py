#!/usr/bin/python3
def matrix_divided(matrix, div):
    if div == 0:
        raise ZeroDivisionError("division by zero")
    if type(div) != float or type(div) != int:
        raise TypeError("div must be a number")
    for row in range(len(matrix)):
        if len(matrix[0]) != len(matrix[row]):
            raise TypeError("Each row of the matrix must have the same size")
        for value in range(len(row)):
            if type(matrix[row][value] != int and\
                    type(matrix[row][value] != float:
                       raise TypeError("matrix must be a matrix (list of lists) of integers/floats") 

    return [[round(value/div, 2)for value in row] for row in matrix]
