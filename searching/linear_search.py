
def linear_search(arr, value):
    """ search the array and return the index """

    return next((index for index, ele in enumerate(arr) if ele == value), -1)


arr = [45, 23, 46, 34, 98, 57, 69]
found = linear_search(arr, 99)
print("Result: ", found)
