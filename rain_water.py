def func(arr):
    n = len(arr)
    max_r = [0]*n
    max_l = [0]*n
    max_l[0] = arr[0]
    max_r[n-1] = arr[n-1]

    for i in range(1, n):
        max_l[i] = max(max_l[i-1], arr[i])
    

    for i in range(n-2,-1, -1):
        max_r[i] = max(arr[i], max_r[i+1])
    print(max_l, max_r)
    return max_l, max_r
    

arr = [3,0,0,2,0,4]
max_l, max_r = func(arr)

res = 0
for i in range(len(arr)):
    res += min(max_r[i],max_l[i]) - arr[i]

print(res)

