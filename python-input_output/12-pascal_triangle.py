#!/usr/bin/python3
"""Define a module"""


def pascal_triangle(n):
    """Define a pascal class"""
    if n <= 0:
        return []

    triangle = []
    for i in range(n):
        if i == 0:
            triangle.append([1])
        else:
            last_item = triangle[-1]  # previous list in triangle
            new_row = [1]
            for j in range(1, i):
                add_val = last_item[j-1] + last_item[j]
                new_row.append(add_val)
            new_row.append(1)
            triangle.append(new_row)

    return triangle
