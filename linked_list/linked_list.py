from node import _Node

class LinkedList:

    def __init__(self) -> None:
        self._head = None
        self._tail = None
        self._size = 0

    def __len__(self):
        return self._size

    def is_empty(self):
        return self._size <= 0

    def add_last(self, ele):
        new = _Node(ele, None)
        if self.is_empty():
            self._head = new
        else:
            self._tail._next = new

        self._tail = new
        self._size += 1

    def display(self):
        p = self._head
        while p:
            print(p._element, end=" -> ")
            p = p._next
        print(None)

    def node_display(self):
        print(self._head)

L = LinkedList()
L.add_last(4)
L.add_last(10)
L.add_last(15)
L.add_last(9)
L.add_last(5)

L.node_display()
print("Size: ", len(L))
