
def func(input1, input2, input3):
    import numpy as np
    arr = []
    input3 = np.asarray(input3)
    arr = input3.reshape(input1, input2)

    # for i in range(input1):
    #     for j in range(input2-1):
    #         arr[i][j] = input3[i]
    max_row = 0
    max_col = 0

    for i in range(input1):
        temp_row = 0
        temp_col = 0
        for j in range(input2):
            temp_row += arr[i][j]        
            temp_col += arr[j][i]

            if temp_row > max_row:
                max_row = temp_row        

            if temp_col > max_col:
                max_col = temp_col     
    return max_col + max_row            

print(func(3,3,[3,6,9,1,4,7,2,8,9]))