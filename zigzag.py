def zigzag(matrix):
    result = []
    m = len(matrix)
    n = len(matrix[0])
    i = 0
    j = 0
    dir_ = 1

    for _ in range(m*n):
        result.append(matrix[i][j])
        if dir_ == 1:
            if  j == n - 1:
                i += 1
                dir_ = -1
            elif i == 0:
                j += 1
                dir_ =-1
            else:
                i -= 1
                j += 1

        else:
            if i == m - 1:  
                j += 1
                dir_ = 1
            elif j == 0:    
                i += 1
                dir_ = 1
            else:
                i += 1
                j -= 1
                
    return result
