def NGR(arr, n):

    stack, res = [], []

    for i in range(n-1,-1, -1):

        if len(stack) == 0:
            res.append(-1)

        if stack and stack[-1] > arr[i]:
            res.append(stack[-1])

        if stack and stack[-1] <= arr[i]:
            while stack and stack[-1] <= arr[i]:
                stack.pop()

            if len(stack) == 0:
                res.append(-1)
            else:    
                res.append(stack[-1])
        stack.append(arr[i])    
    return res[::-1]                    

arr = [4, 5,2,10,8]
n = len(arr)
print(NGR(arr, n))          