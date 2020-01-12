#!/usr/bin/python3
def matrix_divided(matrix, div):
    """
       Returns a matrix divided by the scalar number
       provided in the second parameter
       Args:
           matrix: a list of lists of integers
           div: an integer
       Return: a new matrix of divided numbers
    """
    new_list = []
    msg1 = "matrix must be a matrix (list of lists) of integers/floats"

    if type(matrix) != list:
        raise TypeError(msg1)
    if type(div) not in [int, float]:
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    size = len(matrix[0])
    for row in matrix:
        if len(row) != size:
            raise TypeError("Each row of the matrix must have the same size")
        if type(row) != list:
            raise TypeError(msg1)
        for item in row:
            if type(item) not in [int, float]:
                raise TypeError(msg1)
    new_list = [[float("{:0.2f}".format(matrix[y][x] / div))
                 for x in range(size)] for y in range(len(matrix))]
    return new_list
