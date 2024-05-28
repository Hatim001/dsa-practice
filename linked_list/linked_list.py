from node import _Node


class LinkedList:

    def __init__(self) -> None:
        self._head: _Node = None
        self._tail: _Node = None
        self._size = 0

    def is_empty(self):
        """
        Checks if the linked list is empty.

        Args:
            None

        Returns:
            bool: True if the linked list is empty, False otherwise.
        """
        return self._size == 0

    def __len__(self):
        return self._size

    def display(self):
        """
        Displays the elements of the linked list in order.

        Args:
            None

        Returns:
            None
        """
        p = self._head
        while p:
            print(p._element, end="-->")
            p = p._next
        print(None)

    def insert_last(self, element):
        """
        Inserts the given element at the beginning of the linked list.

        Args:
            element: The element to be inserted at the beginning of the linked list.

        Returns:
            None
        """
        newest = _Node(element, None)
        if self.is_empty():
            self._head = newest
        else:
            self._tail._next = newest

        self._tail = newest
        self._size += 1

    def insert_first(self, element):
        """
        Inserts the given element at the beginning of the linked list.

        Args:
            element: The element to be inserted at the beginning of the linked list.

        Returns:
            None
        """
        newest = _Node(element, None)
        if self.is_empty():
            self._head = newest
            self._tail = newest
        else:
            p = self._head
            self._head = newest
            self._head._next = p

        self._size += 1

    def search(self, key):
        """
        Searches for the given key in the linked list.

        Args:
            key: The key to search for in the linked list.

        Returns:
            None
        """
        p = self._head
        index = 0
        while p:
            if p._element == key:
                return index

            p = p._next
            index += 1

        return -1

    def insert_any(self, element, position):
        """
        Inserts the given element at the specified position in the linked list.

        Args:
            element: The element to be inserted.
            position: The position at which the element should be inserted.

        Returns:
            None
        """
        if position not in range(self._size):
            print("Position is Invalid!!")
            return

        if position == 1:
            self.insert_first(element)
        elif position == self._size + 1:
            self.insert_last(element)
        else:
            newest = _Node(element, None)
            p = self._head
            index = 1
            while index < position - 1 and p._next != None:
                p = p._next
                index += 1

            newest._next = p._next
            p._next = newest
            self._size += 1

    def remove_first(self):
        """
        Removes the first element from the linked list.

        Args:
            None

        Returns:
            Removed element
        """
        if self.is_empty():
            print("List is Empty!!")
            return

        p = self._head
        self._head = p._next
        self._size -= 1
        return p._element

    def remove_last(self):
        """
        Removes the last element from the linked list.

        Args:
            None

        Returns:
            Removed element
        """
        if self.is_empty():
            print("List is Empty!!")
            return

        p = self._head
        while p._next._next:
            p = p._next

        removed = p._next
        p._next = None
        self._tail = p
        self._size -= 1
        return removed._element

    def remove_any(self, position):
        """
        Removes an element from the linked list at a specified position.

        Args:
            position: The position of the element to be removed.

        Returns:
            Removed element
        """
        if self.is_empty():
            print("List is Empty!!")
            return

        p = self._head
        index = 1
        while index < position - 1:
            p = p._next
            index += 1

        removed = p._next
        p._next = p._next._next
        self._size -= 1
        return removed._element


linked_list = LinkedList()
linked_list.insert_last(2)
linked_list.insert_last(3)
linked_list.insert_first(10)
linked_list.insert_first(11)
linked_list.display()
print(len(linked_list))
print("Search 2: ", linked_list.search(2))
linked_list.insert_any(12, 3)
linked_list.display()
linked_list.insert_any(14, 1)
linked_list.display()
linked_list.insert_any(15, 5)
linked_list.display()
print(linked_list.remove_first())
linked_list.display()
print(linked_list.remove_last())
linked_list.display()
print(linked_list.remove_any(2))
print(linked_list.remove_any(3))
linked_list.display()