def shell_short(arr):
    n = len(arr)
    gap = n // 2
    while gap > 0:
        for i in range(gap, n):
            gap_value = arr[i]
            j = i - gap
            while j >= 0 and arr[j] > gap_value:
                arr[j + gap] = arr[j]
                j = j - gap
            arr[j + gap] = gap_value
        gap = gap // 2


arr = [3, 5, 8, 9, 6, 2]
print("Original Array: ", arr)
shell_short(arr)
print("Sorted Array: ", arr)