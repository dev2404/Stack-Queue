def max_area(arr):
    
    stack = []
    left = [0]*len(arr)

    for i in range(0, len(arr)):
        if len(stack) == 0:
            left[i] = -1

        elif len(stack) > 0 and arr[stack[-1]] < arr[i]:
            left[i] = stack[-1]

        elif len(stack) > 0 and arr[stack[-1]] >= arr[i]:
            while len(stack) > 0 and arr[stack[-1]] >= arr[i]:
                stack.pop()

            if len(stack) == 0:
                left[i] = -1
            else:
                left[i] = stack[-1]
        stack.append(i)
    print(left)    

    stack = []
    right = [0]*len(arr)

    for i in range(len(arr)-1, -1, -1):
        if len(stack) == 0:
            right[i] = len(arr)

        elif len(stack) > 0 and arr[stack[-1]] < arr[i]:
            right[i] = stack[-1]

        elif len(stack) > 0 and arr[stack[-1]] >= arr[i]:
            while len(stack) > 0 and arr[stack[-1]] >= arr[i]:
                stack.pop()

            if len(stack) == 0:
                right[i] = len(arr)
            else:
                right[i] = stack[-1]
        stack.append(i)
    # right = right[::-1]
    print(right)  

    area = 0
    width = [0]*len(arr)
    for i in range(len(arr)):
        width[i] = right[i] - left[i] - 1
    print(width)    

    for i in range(len(arr)):
        area = max(area, arr[i]*width[i])
    print(width)  

    return (area)  


# arr = [2,1,5,6,2,3]
arr = [1]

print(max_area(arr))                                 