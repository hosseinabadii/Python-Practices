import os
from typing import TypeVar

T = TypeVar("T", int, str)


def merge_sort(array: list[T]) -> list[T]:
    """
    Sort an array by devided into two halves and then merge them recursively
    Time Complexity:
    - Best case : O(n log n)
    - Worst case: O(n log n)
    """
    if len(array) <= 1:
        return array
    mid = len(array) // 2
    left = merge_sort(array[:mid])
    right = merge_sort(array[mid:])
    return merge(left, right)


def merge(left: list[T], right: list[T]) -> list[T]:
    sorted_array = []
    len_left = len(left)
    len_right = len(right)
    index_left = 0
    index_right = 0
    while index_left < len_left and index_right < len_right:
        if left[index_left] < right[index_right]:
            sorted_array.append(left[index_left])
            index_left += 1
        else:
            sorted_array.append(right[index_right])
            index_right += 1
    sorted_array += left[index_left:]
    sorted_array += right[index_right:]

    return sorted_array


def main():
    os.system("clear" if os.name == "posix" else "cls")
    my_list = [15, 5, 35, 45, 25, 50, 30, 10, 20, 40]
    sorted_list = merge_sort(my_list)
    print(sorted_list)

    list_names = ["John", "Sarah", "Michael", "Emily", "David", "Michael"]
    print(list_names)
    sorted_names = merge_sort(list_names)
    print(sorted_names)


if __name__ == "__main__":
    main()
