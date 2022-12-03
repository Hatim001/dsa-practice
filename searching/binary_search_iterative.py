

def binary_search_iterative(arr, value):
    """ searches the element using binary search """

    length = len(arr)
    left = 0
    right = length - 1

    while left <= right:
        middle = (left + right) // 2
        if arr[middle] == value:
            return middle
        elif value < arr[middle]:
            right = middle - 1
        elif value > arr[middle]:
            left = middle + 1

    return - 1


arr = [23, 34, 45, 57, 69, 98]
found = binary_search_iterative(arr, 45)
print("Result: ", found)