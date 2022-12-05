

def bubble_sort(arr):
    """ sorts the arr using bubble sort """

    n = len(arr)
    for passes in range(n-1, 0, -1):
        for i in range(passes):
            if arr[i] > arr[i+1]:
                temp = arr[i]
                arr[i] = arr[i+1]
                arr[i+1] = temp

    return arr


arr = [3, 5, 8, 9, 6, 2]
print("Original Array: ", arr)
bubble_sort(arr)
print("Sorted Array: ", arr)
