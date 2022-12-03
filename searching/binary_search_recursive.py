

def binary_search_recursive(arr, value, left, right):
    """ searches the element using binary search """

    if left > right:
        return -1

    middle = (left + right) // 2
    if arr[middle] == value:
        return middle
    elif value < arr[middle]:
        return binary_search_recursive(arr, value, left, middle - 1)
    elif value > arr[middle]:
        return binary_search_recursive(arr, value, middle + 1, right)


arr = [23, 34, 45, 57, 69, 98]
found = binary_search_recursive(arr, 69, 0, len(arr)-1)
print("Result: ", found)
