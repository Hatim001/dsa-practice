class _Node:
    __slots__ = '_element', '_next'

    def __init__(self, element, next) -> None:
        self._element = element
        self._next = next

    def __str__(self) -> str:
        return '{0} -> {1}'.format(self._element, self._next)

class StackLinkedList:
    def __init__(self) -> None:
        self._top = None
        self._size = 0

    def __len__(self):
        return self._size

    def is_empty(self):
        return len(self) == 0

    def push(self, ele):
        newest = _Node(ele, None)
        if self.is_empty():
            self._top = newest
        else:
            newest._next = self._top
            self._top = newest
        self._size += 1

    def pop(self):
        if self.is_empty():
            print("Stack is Empty!!")
            return

        ele = self._top._element
        self._top = self._top._next
        self._size -= 1
        return ele

    def top(self):
        if self.is_empty():
            print("Stack is Empty!!")
            return

        return self._top._element

    def display(self):
        p = self._top
        while p:
            print(p._element, end="-->")
            p = p._next
        print()

s = StackLinkedList()
s.push(45)
s.push(7)
s.push(2)
s.display()
print("Length: ", len(s))
s.pop()
s.display()
s.top()
