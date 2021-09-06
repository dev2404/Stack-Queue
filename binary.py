def MAH(arr):

    left = []
    stack = []

    for i in range(0, len(arr)):
        if stack == []:
            left.append(0)

        if stack and stack[-1] < arr[i]:
            left.append(stack[-1])

        if stack and stack[-1] >= arr[i]:
            while stack and stack[-1] >= arr[i]:
                stack.pop()

            if len(stack) == 0:
                left.append(0)
            else:
                left.append(stack[-1])
        stack.append(arr[i])        

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
    # print(right)  

    area = 0
    width = [0]*len(arr)
    for i in range(len(arr)):
        width[i] = int(right[i]) - int(left[i]) - 1
    # print(width)    

    for i in range(len(arr)):
        area = max(area, arr[i]*width[i])
    # print(width)  

    return (area)     


    




arr = [["1","0","1","0","0"],["1","0","1","1","1"],["1","1","1","1","1"],["1","0","0","1","0"]]
# arr = [["1"]]
arr = ( [list( map(int,i) ) for i in arr] )
n = len(arr)
m = len(arr[0])
vec = []
for j in range(0,m):
    vec.append(arr[0][j])

res_max = 0
res_max = MAH(vec)

for i in range(0, n):
    for j in range(1, m):

        if arr[i][j] == 0:
            vec[j] = 0
        else:
            vec[j] = arr[i-1][j] + arr[i][j]
    res_max = max(res_max, MAH(vec))

print(res_max)          


# from typing import List


# class Solution:
#     def maximalRectangle(self, matrix: List[List[str]]) -> int:
#         if not matrix: 
#             return 0
        
#         res, histogram = 0, [0] * (len(matrix[0]) + 2)
#         print(histogram)
        
#         for row in matrix:
#             for i, val in enumerate(row):
#                 if val == '0':
#                     histogram[i + 1] = 0
#                 else:
#                     histogram[i + 1] += 1
                    
#             res = max(res, self.maxInHistogram(histogram))
#             print(res, histogram)
        
#         return res
        
        
#     def maxInHistogram(self, hist: List[int]) -> int:
#         res, stack = 0, []
        
#         for i, h in enumerate(hist):
            
#             while stack and hist[stack[-1]] > h:
#                 j = stack.pop()
#                 res = max(res, (i - stack[-1]-1) * hist[j])
            
#             stack.append(i)
        
#         return res
# matrix = [["1","0","1","0","0"],["1","0","1","1","1"],["1","1","1","1","1"],["1","0","0","1","0"]]
# Sol = Solution()
# print(Sol.maximalRectangle(matrix))