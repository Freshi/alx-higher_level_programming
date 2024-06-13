#!/usr/bin/python3
"""
A function that divided all elements
of a given matrix by a divisor.
"""


def matrix_divided(matrix, div):
    """
    Function that divides provided matrix by a divisor
    Args:
        matrix (list[list]) - Matrix whose elements to divide
        div (int, float) - divisor to the elements of the matrix

    returns: divided_matrix(list[list]) - matrix with elements divided by the
    divisor.
    """
    if (matrix == [] or not isinstance(matrix, list) or
        not all(isinstance(row, list) for row in matrix) or
        not all((isinstance(el, int) or isinstance(el, float))
                for el in [num for row in matrix for num in row])):
        raise TypeError('matrix must be a matrix (list of lists) '
                        'of integers/floats')

    if not all(len(row) == len(matrix[0]) for row in matrix):
        raise TypeError('Each row of the matrix must have the same size')

    if all((not isinstance(div, int), not isinstance(div, float))):
        raise TypeError('div must be a number')

    if div == 0:
        raise ZeroDivisionError('division by zero')

    return [[round(_/div, 2) for _ in row] for row in matrix]
