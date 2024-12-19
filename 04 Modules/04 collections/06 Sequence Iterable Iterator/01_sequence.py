from collections.abc import Sequence


class Items(Sequence):
    def __init__(self, *values):
        self._values = values

    def __len__(self):
        return len(self._values)

    def __getitem__(self, item):
        return self._values.__getitem__(item)

    def __repr__(self):
        return self._values.__repr__()


my_items = Items("apple", "banana", "cherry", "date")
print(f"my_items      : {my_items}")
print(f"my_items[1]   : {my_items[1]}")
print(f"my_items[-1]  : {my_items[-1]}")
print(f"my_items[1:3] : {my_items[1:3]}")
print(f"my_items[::2] : {my_items[::2]}")
print(f"len(my_items) : {len(my_items)}")
print("-" * 50)

print("for item in my_items:\n")
for item in my_items:
    print(item, end=", ")
print()
print("-" * 50)

print("for index, item in enumerate(my_items):\n")
for index, item in enumerate(my_items):
    print(f"{index}: {item}")
print("-" * 50)

print(f"'apple' in my_items       : {('apple' in my_items)}")
print(f"'banana' not in my_items  : {('banana' not in my_items)}")
print("-" * 50)

print(f"sorted(my_items)          : {sorted(my_items)}")
print(f"list(reversed(my_items))  : {list(reversed(my_items))}")
print("-" * 50)
