class StackArray:
    def __init__(self) -> None:
        self._data = []

    def __len__(self):
        return len(self._data)

    def is_empty(self):
        return len(self) == 0

    def push(self, ele):
        self._data.append(ele)

    def pop(self):
        if self.is_empty():
            print("Stack is Empty!!")
            return

        return self._data.pop()

    def top(self):
        if self.is_empty():
            print("Stack is Empty!!")
            return

        return self._data[-1]

s = StackArray()
s.push(45)
s.push(7)
s.push(2)
print(s._data)
print("Length: ", len(s))
s.pop()
print(s._data)
print(s.top())
