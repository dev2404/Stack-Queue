def NSE(arr):
    arr1 = []
    for i in range(len(arr)):
        next = -1
        for j in range(i+1, len(arr)):
            if arr[i] > arr[j]:
                next = arr[j]
                break
        arr1.append(next)   
    return arr1     

arr = [11, 13, 21, 3] 
print(NSE(arr))     