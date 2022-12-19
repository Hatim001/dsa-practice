class _Node:
    __slots__ = '_element', '_next'

    def __init__(self, element, next) -> None:
        self._element = element
        self._next = next

    def __str__(self) -> str:
        return '{0} -> {1}'.format(self._element, self._next)

class QueueLinkedList:
    def __init__(self) -> None:
        self._front = None
        self._rear = None
        self._size = 0

    def __len__(self):
        return self._size

    def is_empty(self):
        return len(self) == 0

    def enqueue(self, ele):
        newest = _Node(ele, None)
        if self.is_empty():
            self._front = newest
        else:
            self._rear._next = newest

        self._rear = newest
        self._size += 1

    def dequeue(self):
        if self.is_empty():
            print("Queue is Empty!")
            return

        ele = self._front._element
        self._front = self._front._next
        self._size -= 1
        if self.is_empty():
            self._rear = None

        return ele

    def first(self):
        if self.is_empty():
            print("Queue is Empty!")
            return

        return self._front._element

    def display(self):
        p = self._front
        while p:
            print(p._element, end="-->")
            p = p._next
        print()

q = QueueLinkedList()
q.enqueue(5)
q.enqueue(3)
q.enqueue(7)
q.display()
print("Length: ", len(q))
q.dequeue()
q.display()
print("Length: ", len(q))
