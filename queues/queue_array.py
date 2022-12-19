class QueueArray:
    def __init__(self) -> None:
        self._data = []

    def __len__(self):
        return len(self._data)

    def is_empty(self):
        return len(self) == 0

    def enqueue(self, ele):
        self._data.append(ele)

    def dequeue(self):
        if self.is_empty():
            print("Queue is Empty!")
            return

        return self._data.pop(0)

    def first(self):
        if self.is_empty():
            print("Queue is Empty!")
            return

        return self._data[0]

q = QueueArray()
q.enqueue(5)
q.enqueue(3)
q.enqueue(7)
print(q._data)
print("Length: ", len(q))
q.dequeue()
print(q._data)
print("Length: ", len(q))
