import os
import random
import time
from typing import TypeVar

T = TypeVar("T", int, str)


def selection_sort(array: list[T]) -> list[T]:
    """
    Sort an array by comparing each element with the rest of the array
    Time Complexity:
    - Best case : O(n^2)
    - Worst case: O(n^2)
    """
    sorted_array = []
    for i in range(len(array)):
        min_index = 0
        for j in range(1, len(array)):
            if array[j] < array[min_index]:
                min_index = j
        sorted_array.append(array.pop(min_index))
    return sorted_array


def selection_sort_inplace(array: list[T]) -> list[T]:
    """
    Selection sort algorithm with O(n^2) time complexity.
    """
    for i in range(len(array)):
        min_index = i
        for j in range(i + 1, len(array)):
            if array[j] < array[min_index]:
                min_index = j
        array[i], array[min_index] = array[min_index], array[i]
    return array


def main():
    os.system("clear" if os.name == "posix" else "cls")
    k = 1000
    x = range(k)
    unsorted_list = random.choices(x, k=k)
    start = time.perf_counter()
    selection_sort_inplace(unsorted_list)
    end = time.perf_counter()
    duration_1 = end - start

    unsorted_list = random.choices(x, k=k)
    start = time.perf_counter()
    selection_sort(unsorted_list)
    end = time.perf_counter()
    duration_2 = end - start

    print(f"Selection sort inplace : {duration_1:.5f} seconds")
    print(f"Selection sort copy    : {duration_2:.5f} seconds")

    list_names = ["John", "Sarah", "Michael", "Emily", "David", "Michael"]
    print(list_names)
    sorted_names = selection_sort_inplace(list_names)
    print(sorted_names)


if __name__ == "__main__":
    main()
