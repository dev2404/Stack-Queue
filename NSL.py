def NSL(arr, n):
    stack, res = [], []

    for i in range(0, n):
        
        if len(stack) == 0:
            res.append(-1)

        elif len(stack) > 0 and stack[-1] < arr[i]:
            res.append(stack[-1])
            # print(res, stack)

        elif len(stack) > 0 and stack[-1] >= arr[i]:
            while len(stack) > 0 and stack[-1] >= arr[i]:
                stack.pop()
            # print(res, stack)


            if len(stack) == 0:
                res.append(-1)
            else:
                res.append(stack[-1])
        stack.append(arr[i]) 
    return res

arr = [4, 5,2,10,8]
n = len(arr)
print(NSL(arr, n))                                     