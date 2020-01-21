#!/usr/bin/python3

def pascal_triangle(n):
    """ returns a list of list of integers
    based on pascal triangle
    """
    if n == 1:
        return [[1]]
    triangle = [[1],[1,1]]
    prev = [1,1]
    count = 2
    while count < n:
        new = []
        new.append(1)
        for i in range(count-1):
            new.append(prev[i]+prev[i+1])
        new.append(1)
        triangle.append(new)
        prev = new
        count += 1
    return triangle
