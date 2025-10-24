def countingSort(arr):
    max_val = max(arr) #5
    count = [0] * (max_val + 1)

    while len(arr) > 0:
        num = arr.pop(0)
        count[num] += 1

    for i in range(len(count)):
        while count[i] > 0:
            arr.append(i)
            count[i] -= 1

    return arr

unsortedArr = [4, 2, 2, 3, 3, 5, 2, 3]

[0,1,2,3,4,5]
[0,0,0,0,0,0]

sortedArr = countingSort(unsortedArr)
print("Sorted array:", sortedArr)