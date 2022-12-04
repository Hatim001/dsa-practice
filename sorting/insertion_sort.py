def insertion_sort(arr):
    """docstring"""

    n = len(arr)

    for i in range(1, n):
        current_value = arr[i]
        position = i

        while position > 0 and arr[position - 1] > current_value:
            arr[position] = arr[position - 1]
            position = position - 1
        arr[position] = current_value

    return arr


arr = [3, 5, 8, 9, 6, 2]
print("Original Array: ", arr)
insertion_sort(arr)
print("Sorted Array: ", arr)
