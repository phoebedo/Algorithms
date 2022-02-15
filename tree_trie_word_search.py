# LC212h word search 2

class TrieNode:
    def __init__(self) -> None:
        self.children = {}
        self.end = False 

class Trie:
    def __init__(self) -> None:
        self.root = TrieNode()

    def insert(self,word):
        cur = self.root 
        for c in word: 
            if c not in cur.children[c]:
                cur.children[c] = TrieNode()
            cur = cur.children[c]
        cur.end = True


def findWord(board, words):
    trie = Trie()

    for w in words:
        trie.insert(w)
    
    rows, cols = len(board), len(board[1])
    res, visited = set(), set()


    def dfs(r,c,node,word):
        if r<0 or c<0 or r>rows or c>cols or (r,c) in visited or board[r][c] not in node.children:
            return
        visited.add((r,c))

        node = node.children[board[r][c]]
        word += board[r][c]

        if node.end:
            res.add(word) #res is a set to eliminate duplicates

        dfs(r+1,c,node,word)
        dfs(r-1,c,node,word)
        dfs(r,c+1,node,word)
        dfs(r,c-1,node,word)

        visited.remove((r,c))

        for i in range(rows):
            for j in range(cols):
                dfs(i,j,trie,"")


    return list(res)



