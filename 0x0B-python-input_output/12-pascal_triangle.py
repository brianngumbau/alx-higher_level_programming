#!/usr/bin/python3
"""
Module for pascal_triangle method.
"""


def pascal_triangle(n):
    """
    returns a list of lists of integers
        Args:
            n : number of lists and digits
        Returns: list of lists
    """
    rows = [[1 for k in range(p + 1)] for p in range(n)]
    for n in range(n):
        for p in range(n - 1):
            rows[n][p + 1] = sum(rows[n - 1][p:p + 2])
    return rows
