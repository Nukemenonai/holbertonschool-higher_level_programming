#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    if not matrix:
        print("")
    else:
        for i in range(0, len(matrix)):
            for j in range(0, len(matrix[i])):
                if j < len(matrix[i]) - 1:
                    print("{}".format(matrix[i][j]), end=" ")
                else:
                    print("{}".format(matrix[i][j]))
