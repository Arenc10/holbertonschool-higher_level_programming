#!/usr/bin/python3
"""Divide all elements of a matrix"""


def matrix_divided(matrix, div):
    """Returns a new matrix
    Args:
        matrix: list of list of int or floats
        div: number that elements of matrix should be divided
    Raises:
        raise TypeError if matrix is not a list of list of int or floats
        raise TypeError if rows have not the same size
        raise TypeError if div is not a number
        raise ZeroDivisionError if div is equal to 0
    """

    newmatrix = []
    if div == 0:
        raise ZeroDivisionError("division by zero")
    if type(div) != int and type(div) != float:
        raise TypeError("div must be a number")
    for row in range(len(matrix)):
        if len(matrix[0]) != len(matrix[row]):
            raise TypeError("Each row of the matrix must have the same size")
        for val in range(len(matrix[row])):
            if type(matrix[row][val]) != int and\
                    type(matrix[row][val]) != float:
                raise TypeError("matrix must be a matrix (list of lists) of "
                                "integers/floats")
    newmatrix = [[round(val / div, 2) for val in row] for row in matrix]
    return newmatrix
