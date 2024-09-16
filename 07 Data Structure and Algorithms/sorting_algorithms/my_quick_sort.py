import os
from typing import TypeVar

T = TypeVar("T", int, str)


def quick_sort(array: list[T]) -> list[T]:
    """
    Sort an array by devided into two halves and then merge them recursively
    The pivot is always the first element in this implementation
    Time Complexity:
    - Best case : O(n log n)
    - Worst case: O(n^2)
    """
    if len(array) <= 1:
        return array
    pivot = array[0]
    less = []
    greater = []
    for i in range(1, len(array)):
        if array[i] <= pivot:
            less.append(array[i])
        else:
            greater.append(array[i])
    return quick_sort(less) + [pivot] + quick_sort(greater)


def main():
    os.system("clear" if os.name == "posix" else "cls")
    my_list = [15, 5, 35, 45, 25, 50, 30, 10, 20, 40]
    sorted_list = quick_sort(my_list)
    print(sorted_list)

    list_names = ["John", "Sarah", "Michael", "Emily", "David", "Michael"]
    print(list_names)
    sorted_names = quick_sort(list_names)
    print(sorted_names)


if __name__ == "__main__":
    main()
