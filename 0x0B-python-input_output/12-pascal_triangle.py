#!usr/bin/python3
"""Defines pascal triangle function"""


def pascal_triangle(n):
    """Returns a list of lists representing Pascals triange"""
    if n <= 0:
        return ""

    triangle = [[1]]

    for currentRow in range(1, n):
        row = [1]
        previousRow = triangle[currentRow - 1]
        for el in range(1, currentRow):
            row.append(previousRow[el] + previousRow[el - 1])
        row.append(1)
        triangle.append(row)
    return triangle
