#!/usr/bin/python3
"""finds a peak in a list of unsorted integers."""

def find_peak(list_of_integers):
    """
    Finds peak element in a list of unsorted integers.

    Args:
    - list_of_integers: list of unsorted integers.

    Returns:
    - peak element in the list.
    """
    if not list_of_integers:
        return None

    lo, hi = 0, len(list_of_integers) - 1

    while lo < hi:
        mid = (lo + hi) // 2

        if list_of_integers[mid] > list_of_integers[mid + 1]:
            hi = mid
        else:
            lo = mid + 1

    return list_of_integers[l]