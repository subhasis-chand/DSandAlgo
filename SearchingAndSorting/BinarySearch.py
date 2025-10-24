def binary_search_iterative(arr, target): # [1,2,3,4,5,6] target=5
                                          # [0,1,2,3,4,5]
    left_index = 0
    right_index = len(arr) - 1

    while left_index <= right_index:
        mid = (left_index + right_index) // 2

        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left_index = mid + 1
        else:
            right_index = mid - 1

    return -1


def binary_search_recursive(arr, target, left_index, right_index):
    if left_index > right_index:
        return -1

    mid = (left_index + right_index) // 2

    if arr[mid] == target:
        return mid
    elif arr[mid] < target:
        return binary_search_recursive(arr, target, mid + 1, right_index)
    else:
        return binary_search_recursive(arr, target, left_index, mid - 1)


arr = [2, 4, 6, 8, 10, 12]
print(binary_search_iterative(arr, 10))  # Output: 4
print(binary_search_iterative(arr, 7))   # Output: -1


arr = [2, 4, 6, 8, 10, 12]
print(binary_search_recursive(arr, 8, 0, len(arr) - 1))  # Output: 3
print(binary_search_recursive(arr, 5, 0, len(arr) - 1))  # Output: -1
