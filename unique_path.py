# LC62m
# Robot can move either down or right. How many unique path can it move from top left to top right corner of m*n grid
# similar to climbing stair problem 

def uniquePaths(m,n):
    matrix = []
    for i in range(m):
        matrix.append([0]*n)
    for i in range(m):
        matrix[i][0]=1
    for j in range(n):
        matrix[0][j]=1
    for i in range(1,m):
        for j in range(1,n):
            matrix[i][j] = matrix[i-1][j]+matrix[i][j-1]
    
    
    return matrix[m-1][n-1]


