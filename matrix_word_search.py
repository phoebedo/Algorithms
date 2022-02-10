# LC79m
# Given an m x n grid of characters board and a string word, return true if word exists in the grid.

def exist(board, word):
    rows,cols = len(board), len(board[0])
    path = set()

    def dfs(r,c,i):
        if i == len(word):
            return True
        # If go out of bound or not match or already visited 
        if (r<0 or c<0 or r>rows or c > cols 
        or word[i] != board[r][c] 
        or (r,c) in path):
            return False
        path.add((r,c))

        res = (dfs(r+1,c,i+1) or
        dfs(r-1,c,i+1) or
        dfs(r,c-1,i+1) or
        dfs(r,c+1,i+1))

        path.remove((r,c))
        return res
    
    for i in range(rows):
        for j in range(cols):
            if dfs(i,j,0):
                return True

    return False 

# Time complexity: for loop i,j => O(m*n*dfs)
# Time complexity of dfs, 4^w. w = len(word) 
# Overall time complexity is O(m*n*4^w)
        
                