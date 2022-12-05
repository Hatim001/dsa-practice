

class _Node:

    __slots__ = '_element', '_next'

    def __init__(self, element, next) -> None:
        self._element = element
        self._next = next

    def __str__(self) -> str:
        return '{0} -> {1}'.format(self._element, self._next)

# n1 = _Node(7, None)
# n2 = _Node(8, None)
# n3 = _Node(9, None)
# n4 = _Node(10, None)
# n5 = _Node(11, None)
# n1._next = n2
# n2._next = n3
# n3._next = n4
# n4._next = n5
# print(n1)
