myArray = [170, 1234, 45, 75, 90, 802, 24, 2, 66]
print("Original array:", myArray)
radixArray = [[170], [], [], [], [1234], [], [], [], [], []]
maxVal = max(myArray)
exp = 1

while maxVal // exp > 0:

    while len(myArray) > 0:
        val = myArray.pop() # 1234
        radixIndex = (val // exp) % 10 # 4
        radixArray[radixIndex].append(val)

    for bucket in radixArray:
        while len(bucket) > 0:
            val = bucket.pop()
            myArray.append(val)

    exp *= 10

print("Sorted array:", myArray)