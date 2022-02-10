# LC48m 
# given n*n matrix, rotate 90 clockwise. O(n*n)
def rotate(matrix):
    l,r = 0,len(matrix) -1
    while l < r:
        for i in range(r-l):
            top,bot = l,r #square
            print(top,bot,l,r)

            # store the top left 
            temp = matrix[top][l + i]

            # move bottom left to top left 
            matrix[top][l + i] = matrix[bot - i][l]

            #move bottom right to bottom left
            matrix[bot -i][l] = matrix[bot][r - i]

            #move top right to bottom right 
            matrix[bot][r -i ] = matrix[top + i][r]

            #move top left to top right
            matrix[top + i ][r]= temp
        r -= 1
        l += 1

# Solution 2: Transpose + fold = rotate 
# flip diagonally, then vertically => rotated (it's magic 0o0)
def rotateMagic(matrix):
    n = len(matrix)
    # flit diagonally
    for i in range(n):
        for j in range(i,n):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
    
    for i in range(n):
        for j in range(n//2):
            matrix[i][j], matrix[i][n-j-1] = matrix[i][n-j-1], matrix[i][j]
    

matrix = [[1,2,3],[4,5,6],[7,8,9]]
rotateMagic(matrix)
print(matrix)