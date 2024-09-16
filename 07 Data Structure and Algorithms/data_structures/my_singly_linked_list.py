"""
Implementing Singly Linked List in Python
"""

import os
from typing import Any


class Node:
    def __init__(self, data: Any | None = None, next: "Node | None" = None):
        self.data = data
        self.next = next

    def __repr__(self):
        return f"Node({self.data})"


class LinkedList:
    def __init__(self, head: Node | None = None):
        self.head = head

    def push(self, data: Any) -> None:
        """
        Inserts the given data at the head of the list.
        """
        node = Node(data)
        node.next = self.head
        self.head = node

    def append(self, data: Any) -> None:
        """
        Inserts the given data at the end of the list.
        """
        node = Node(data)
        if self.empty():
            self.head = node
            return
        tail = self.tail()
        tail.next = node

    def insert(self, index: int, data: Any) -> None:
        """
        Inserts the given data at the given index.
        """
        if index == 0:
            self.push(data)
            return
        if index == self.size():
            self.append(data)
            return
        prev_node = self.index(index - 1)
        node = Node(data)
        node.next = prev_node.next
        prev_node.next = node

    def search(self, data: Any) -> Node | None:
        """
        Searches for the given data in the list and returns the node if found.
        """
        current = self.head
        while current is not None:
            if current.data == data:
                return current
            current = current.next
        return current

    def remove(self, data: Any) -> None:
        """
        Removes the Node with the given data from the list.
        """
        current = self.head
        previous = None
        while current is not None:
            if current.data == data:
                if previous is None:
                    self.head = current.next
                    current = None
                    return
                else:
                    previous.next = current.next
                    current = None
                    return
            previous = current
            current = current.next
        raise ValueError("Data not found.")

    def pop(self, index: int) -> Node:
        """
        Removes the node at the given index.
        """
        if self.head is None:
            raise IndexError("List is empty.")
        self._check_index(index)
        if index == 0:
            current = self.head
            self.head = self.head.next
            return current

        prev_node = self.index(index - 1)
        current = prev_node.next
        prev_node.next = current.next  # type: ignore
        return current  # type: ignore

    def index(self, index: int) -> Node:
        """
        Returns the node at the given index.
        """
        self._check_index(index)
        current = self.head
        i = 0
        while current is not None:
            if i == index:
                return current
            current = current.next
            i += 1
        raise IndexError("Index out of range")

    def node_at_index(self, index: int) -> Node:
        """
        Returns the node at the given index.
        """
        self._check_index(index)
        current = self.head
        position = 0
        while position < index and current is not None:
            current = current.next
            position += 1
        return current  # type: ignore

    def tail(self) -> Node:
        """
        Returns the tail node.
        """
        current = self.head
        if current is None:
            raise IndexError("List is empty")
        while current.next is not None:
            current = current.next
        return current

    def empty(self) -> bool:
        """
        Checks if the list is empty.
        """
        return self.head is None

    def size(self) -> int:
        """
        Returns the number of nodes in the list.
        """
        current = self.head
        n = 0
        while current is not None:
            n += 1
            current = current.next
        return n

    def clear(self) -> None:
        """
        Deletes the entire list.
        """
        self.head = None

    def _check_index(self, index: int) -> None:
        """
        Checks if the index is valid.
        """
        if not isinstance(index, int):
            raise TypeError(f"Index must be an integer, not {type(index).__name__}")
        if index < 0 or index >= self.size():
            raise IndexError("Index out of range")

    def __repr__(self) -> str:
        if self.empty():
            return "(Empty)"
        sep = " -> "
        result = "(Head) "
        current = self.head
        while current is not None:
            result += str(current) + sep
            current = current.next
        return result[:-4] + " (Tail)"


def main():
    os.system("clear" if os.name == "posix" else "cls")

    linked_list = LinkedList()
    print(linked_list)
    try:
        linked_list.pop(0)
    except IndexError as e:
        print("IndexError:", e)
    print(linked_list)
    linked_list.append(10)
    print(linked_list)
    linked_list.pop(0)
    print(linked_list)
    linked_list.push(20)
    print(linked_list)
    linked_list.push(30)
    print(linked_list)
    linked_list.insert(0, 25)
    print(linked_list)
    linked_list.insert(2, 45)
    print(linked_list)
    linked_list.append(60)
    print(linked_list)
    linked_list.pop(4)
    print(linked_list)
    linked_list.remove(20)
    print(linked_list)
    try:
        linked_list.remove(32)
    except ValueError as e:
        print("ValueError:", e)

    for i in range(linked_list.size()):
        assert linked_list.node_at_index(i) is linked_list.index(i)

    new_list = LinkedList()
    new_list.append(50)
    assert new_list.node_at_index(0) is new_list.index(0)
    print("No assertions failed.")


if __name__ == "__main__":
    main()
