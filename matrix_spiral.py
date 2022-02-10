#LC54m Spiral matrix 
# Given m*n matrix return in spiral order 


def spiralOrder(matrix):
    res = []
    left, right = 0 , len(matrix[0])
    top, bot = 0,len(matrix)

    while left <right and top<bot:
        # top row
        for i in range(left,right):
            res.append(matrix[top][i])
        top += 1

        #right column
        for i in range(top,bot):
            res.append(matrix[i][right-1])
        right -= 1

        if not (left<right and top<bot):
            break

        #bottom row
        for i in range(right-1,left-1,-1):
            res.append(matrix[bot-1][i])
        bot -=1

        #left column
        for i in range(bot-1, top-1, -1):
            res.append(matrix[i][left])
        left +=1

    return res