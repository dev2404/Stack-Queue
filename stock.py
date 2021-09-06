def stockSpan(arr):
    n = len(arr)
    stack = []
    res = []

    for i in range(0, n):

        if len(stack) == 0:
            res.append(-1)

        if stack and stack[-1][0] > arr[i]:
            res.append(stack[-1][1])

        if stack and stack[-1][0] <= arr[i]:
            while stack and stack[-1][0] <= arr[i]:
                stack.pop()

            if len(stack) == 0:
                res.append(-1)
            else:
                res.append(stack[-1][1])
                
        stack.append([arr[i], i])
    for i in range(len(res)):
        res[i] = i - res[i]    
    return res   

arr = [100, 80, 60, 70, 60, 75, 85]
print(stockSpan(arr))             
