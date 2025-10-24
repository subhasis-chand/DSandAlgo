def bubble_sort(arr):
    n = len(arr)
    for i in range(n - 1):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

    return arr


arr = [64, 34, 25, 12, 22, 11, 90]
sorted_arr = bubble_sort(arr)
print("Sorted Array:", sorted_arr)
















def bubble_sort_optimized(arr):
    n = len(arr)
    for i in range(n - 1):
        swapped = False
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
        if not swapped:
            break  # Array already sorted
    return arr
arr = [64, 34, 25, 12, 22, 11, 90]
sorted_arr = bubble_sort_optimized(arr)
print("Optimized Sorted Array:", sorted_arr)