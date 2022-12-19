class _Node:
    __slots__ = '_element', '_next'

    def __init__(self, element, next) -> None:
        self._element = element
        self._next = next

    def __str__(self) -> str:
        return '{0} -> {1}'.format(self._element, self._next)

class DEQueLinkedList:
    def __init__(self) -> None:
        self._front = None
        self._rear = None
        self._size = 0

    def __len__(self):
        return self._size

    def is_empty(self):
        return len(self) == 0

    def add_last(self, ele):
        newest = _Node(ele, None)
        if self.is_empty():
            self._front = newest
        else:
            self._rear._next = newest

        self._rear = newest
        self._size += 1

    def add_first(self, e):
        newest = _Node(e, None)
        if self.is_empty():
            self._front = newest
            self._rear = newest
        else:
            newest._next = self._front
            self._front = newest
        self._size += 1

    def remove_first(self):
        if self.is_empty():
            print('DEQue is empty')
            return
        e = self._front._element
        self._front = self._front._next
        self._size -= 1
        if self.isempty():
            self._rear = None
        return e

    def remove_last(self):
        if self.is_empty():
            print('DEQue is empty')
            return
        p = self._front
        i = 1
        while i < len(self) - 1:
            p = p._next
            i = i + 1
        self._rear = p
        p = p._next
        self._rear._next = None
        self._size -= 1
        return p._element

    def first(self):
        if self.isempty():
            print('DEQue is empty')
            return
        return self._front._element

    def last(self):
        if self.isempty():
            print('DEQue is empty')
            return
        return self._rear._element

    def display(self):
        p = self._front
        while p:
            print(p._element,end=' --> ')
            p = p._next
        print()


D = DEQueLinkedList()
D.add_first(5)
D.add_first(3)
D.add_last(7)
D.add_last(12)
D.display()
print('Length:',len(D))
print(D.remove_first())
print(D.remove_last())
D.display()
print(D.first())
print(D.last())
