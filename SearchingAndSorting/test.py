def counting_sort(arr):
    max_val=max(arr)
    min_val=min(arr)
    n=abs(max_val - min_val )+1
    count=[0]*n
    print(count)
    for i in range(len(arr)):
        count[arr[i]-min_val]+=1
    print(count)
    sorted_array=[]
    for i in range(len(count)):
        for k in range(count[i]):
            sorted_array.append(i+min_val)
    
    
    return sorted_array



print(counting_sort([3,3,4,2,2,7,7,4,3,2]))