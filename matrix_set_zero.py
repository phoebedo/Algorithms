#LC73m set matrix seros
def setZeroes(matrix):
    pos = []
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if matrix[i][j]==0:
                pos.append((i,j))
    for row,col in pos:
        for i in range(len(matrix[row])):
            matrix[row][i] =0
        for j in range(len(matrix)):
            matrix[j][col]=0

    return matrix

matrix = [[0,1,2,0],[3,4,5,2],[1,3,1,5]]
print(setZeroes(matrix))