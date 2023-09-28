from node import _Node


class LinkedList:
    """ this is normal linked list """
    def __init__(self) -> None:
        self._head = None
        self._tail = None
        self._size = 0

    def __len__(self) -> int:
        return self._size

    def is_empty(self) -> bool:
        return self._size <= 0

    def add_last(self, ele) -> None:
        new = _Node(ele, None)
        if self.is_empty():
            self._head = new
        else:
            self._tail._next = new

        self._tail = new
        self._size += 1

    def display(self) -> None:
        p = self._head
        while p:
            print(p._element, end=" -> ")
            p = p._next
        print(None)

    def node_display(self) -> None:
        print(self._head)

    def search(self, ele) -> int:
        p = self._head
        index = 0
        while p:
            if p._element == ele:
                return index
            p = p._next
            index += 1

        return -1

    def add_first(self, ele) -> None:
        new = _Node(ele, None)
        if self.is_empty():
            self._head = new
            self._tail = new
        else:
            new._next = self._head
            self._head = new
        self._size += 1

    def add_between(self, ele, position) -> None:
        new = _Node(ele, None)
        p = self._head
        index = 1
        while index < position - 1:
            p = p._next
            index += 1

        new._next = p._next
        p._next = new
        self._size += 1

    def remove_first(self):
        if self.is_empty():
            print("List is empty")
            return

        ele = self._head._element
        self._head = self._head._next
        self._size -= 1
        if self.is_empty():
            self._tail = None

        return ele

    def remove_end(self):
        if self.is_empty():
            print("List is empty")
            return

        p = self._head
        i = 1
        while i < len(self) - 1:
            p = p._next
            i += 1

        self._tail = p
        p = p._next
        self._tail._next = None
        self._size -= 1

        return p._element

    def remove_any(self, position):
        p = self._head
        i = 1
        while i < position - 1:
            p = p._next
            i += 1

        ele = p._next._element
        p._next = p._next._next
        self._size -= 1
        return ele

L = LinkedList()
L.add_last(4)
L.add_last(10)
L.add_first(15)
L.add_last(9)
L.add_first(5)
L.add_between(8, 2)

L.node_display()
print("Size: ", len(L))

print("Search: ", L.search(15))

L.remove_first()
L.node_display()

L.remove_end()
L.node_display()

L.remove_any(2)
L.node_display()
