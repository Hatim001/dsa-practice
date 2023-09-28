from node import _Node

class CircularLinkedList:
    """ this is a circular linked list """
    def __init__(self) -> None:
        self._head = None
        self._tail = None
        self._size = 0

    def __len__(self):
        return self._size

    @property
    def is_empty(self):
        return self._size == 0

    def add_last(self, ele):
        newest = _Node(ele, None)
        if self.is_empty:
            newest._next = newest
            self._head = newest
        else:
            newest._next = self._tail._next
            self._tail._next = newest

        self._size += 1

    def display(self):
        p = self._head
        i = 0
        while i < len(self):
            print(p._element, end="\t-->\t")
            p = p._next
            i += 1
