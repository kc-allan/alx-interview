#!/usr/bin/python3
"""
A function that returns a list of lists of integers representing the Pascal’s triangle of n
"""
def pascal_triangle(n):
    """
    returns a list of lists of integers representing the Pascal’s triangle of n
    """
    triangle = [[1]]
    if n <= 0:
        return triangle
    for k in range(n-1):
        prev = triangle[-1]
        col = []
        for index, val in enumerate(prev):
            if index-1 < 0:
                col.append(val + 0)
            if index+1 >= len(prev):
                col.append(val+0)
            else:
                col.append(val + prev[index+1])
        triangle.append(col)
    return triangle
