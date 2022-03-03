import collections
def checkValid(matrix):

        n = len(matrix)
        standard = set(i for i in range(1,n+1))
        print(standard)
        
        rows = collections.defaultdict(set)
        cols = collections.defaultdict(set)
        
         
        for r in range(n):
            for c in range(n):
                rows[r].add(matrix[r][c])
            print(rows[r])
            if rows[r] != standard:
                return False
        
        for c in range(n):
            for r in range(n):
                cols[c].add(matrix[r][c])
            print(cols[c])
            if cols[c]!=standard:
                return False
              
            
        return True
    
checkValid([[1,2,3],[3,1,2],[2,3,1]])