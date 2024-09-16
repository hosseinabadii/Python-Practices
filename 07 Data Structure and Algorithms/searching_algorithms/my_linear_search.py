def linear_search(array, target):
    """
    Linear search algorithm with O(n) time complexity.
    """
    for index, item in enumerate(array):
        if item == target:
            return index
    return None
