class DEQueArray:
    def __init__(self) -> None:
        self._data = []

    def __len__(self):
        return len(self._data)

    def is_empty(self):
        return len(self) == 0

    def add_first(self, ele):
        self._data.insert(0, ele)

    def add_last(self, ele):
        self._data.append(ele)

    def remove_first(self):
        if self.is_empty():
            print("DEQue is empty!!")
            return

        return self._data.pop(0)

    def remove_last(self):
        if self.is_empty():
            print("DEQue is empty!!")
            return

        return self._data.pop()

    def first(self):
        if self.is_empty():
            print("DEQue is empty!!")
            return

        return self._data[0]

    def last(self):
        if self.is_empty():
            print("DEQue is empty!!")
            return

        return self._data[-1]

D = DEQueArray()
D.add_first(5)
D.add_first(3)
D.add_last(7)
D.add_last(12)
print(D._data)
print('Length:',len(D))
print(D.remove_first())
print(D.remove_last())
print(D._data)
print('First Element:',D.first())
print('Last Element:',D.last())
