def binary_search(array, target):
    """
    Binary search algorithm with O(log n) time complexity.
    """
    first = 0
    last = len(array) - 1

    while first <= last:
        midpoint = (first + last) // 2
        if target == array[midpoint]:
            return midpoint
        if target < array[midpoint]:
            last = midpoint - 1
        else:
            first = midpoint + 1
    return None
