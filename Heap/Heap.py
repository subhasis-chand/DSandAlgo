def heapify(arr, n, i):
    largest_idx = i
    left_index = 2 * i + 1
    right_index = 2 * i + 2

    if left_index < n and arr[left_index] > arr[largest_idx]:
        largest_idx = left_index

    if right_index < n and arr[right_index] > arr[largest_idx]:
        largest_idx = right_index

    if largest_idx != i:
        arr[i], arr[largest_idx] = arr[largest_idx], arr[i]
        heapify(arr, n, largest_idx)

def create_heap(arr):
    n = len(arr)
    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)

def insert_heap(arr, key):
    arr.append(key)
    create_heap(arr)

def heap_sort(arr):
    n = len(arr)
    create_heap(arr)
    for i in range(n - 1, 0, -1):
        arr[0], arr[i] = arr[i], arr[0]
        heapify(arr, i, 0)
            #.  arr, len, index

# first parent node at index n // 2 - 1 or (n-2)//2

# stack and queue
# [] list


arr = [3, 9, 2, 5, 4, 1, 8, 7, 6]
heap_sort(arr)
print("Heap array:", arr)

from collections import deque
from collections import defaultdict
