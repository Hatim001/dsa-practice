def selection_sort(arr):
    """sorts the array using selection sort technique"""

    n = len(arr)
    for i in range(n - 1):
        position = i

        for j in range(i + 1, n):
            if arr[j] < arr[position]:
                position = j

        print("Swapped ", arr[i], " -> ", arr[position])
        temp = arr[i]
        arr[i] = arr[position]
        arr[position] = temp

    return arr


arr = [3, 5, 8, 9, 6, 2]
print("Original Array: ", arr)
selection_sort(arr)
print("Sorted Array: ", arr)
