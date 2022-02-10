# LC200m 

def num_of_island(grid):
    def sinkIsland(grid,row,col):
        if grid[row][col] == "1":
            grid[row][col] ="0" 
        else: 
            return 
        if row+1 < len(grid):
            sinkIsland(grid, row+1, col)
        if row-1 >=0:
            sinkIsland(grid, row-1, col)
        if col+1 < len(grid[0]):
            sinkIsland(grid, row, col+1)
        if col-1 >= 0:
            sinkIsland(grid, row, col-1)
        

    count = 0
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == "1":
                count +=1
                sinkIsland(grid,i,j)
    return count
grid = [
  ["1","1","1","1","0"],
  ["1","1","0","1","0"],
  ["1","1","0","0","0"],
  ["0","0","0","0","0"]
]
print(num_of_island(grid))

# Time: O(m*n)
# Space O(m*n) - when pass grid into sinkIsland, it is passed grid as a copy => use extra memory 

