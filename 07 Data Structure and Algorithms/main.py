import os
import random
from time import perf_counter

from sorting_algorithms.my_merge_sort import merge_sort
from sorting_algorithms.my_quick_sort import quick_sort
from sorting_algorithms.my_selection_sort import selection_sort


def main(n: int) -> None:
    os.system("clear" if os.name == "posix" else "cls")
    random_list = random.sample(range(0, n), n)

    start = perf_counter()
    quick_sort(random_list.copy())
    end = perf_counter()
    print(f"{'Quick sort':20}: {(end - start):.5f} seconds")

    start = perf_counter()
    merge_sort(random_list.copy())
    end = perf_counter()
    print(f"{'Merge sort':20}: {(end - start):.5f} seconds")

    start = perf_counter()
    selection_sort(random_list.copy())
    end = perf_counter()
    print(f"{'Selection sort':20}: {(end - start):.5f} seconds")


if __name__ == "__main__":
    main(10_000)
