#!/usr/bin/python3
def matrix_mul(m_a, m_b):
    if type(m_a) != list:
        raise TypeError("m_a must be a list")
    if type(m_b) != list:
        raise TypeError("m_b must be a list")
    for row in m_a:
        if type(row) != list:
            raise TypeError("m_a must be a list of lists")
        if len(row) == 0:
            raise ValueError("m_a can't be empty")
        for elem in row:
            if type(elem) not in [int, float]:
                raise TypeError("m_a should contain only integers or floats")
    for row in m_b:
        if type(row) != list:
            raise TypeError("m_b must be a list of lists")
        if len(row) == 0:
            raise ValueError("m_b can't be empty")
        for elem in row:
            if type(elem) not in [int, float]:
                raise TypeError("m_b should contain only integers or floats")
