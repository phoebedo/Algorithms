# TrieNode 

class TrieNode(object):
    def __init__(self) -> None:
        self.children = {}
        self.end = False

class Trie(object):
    def __init__(self) -> None:
        self.root = TrieNode()
    
    def insert(self,word):
        cur = self.root 

        for c in word:
            if c not in cur.children:
                cur.children[c] = TrieNode()
            cur = cur.children[c]

        cur.end = True
    
    def search(self, word):
        cur = self.root 
        for c in word:
            if c not in cur.children:
                return False 
            cur = cur.children[c]
        
        return True if cur.end else False
    
    def startWith(self, prefix):
        cur =self.root
        for c in prefix:
            if c not in cur.children:
                return False 
            cur= cur.children[c]
        return True
    

    def prefix(self,word):
        cur = self.root
        prefix = ''

        for c in word:
            if len(cur.children) ==1:
                return prefix 
            else:
                prefix += c
                cur = cur.children[c]
        return prefix


trie = Trie()
trie.insert("jack")
trie.insert("john")
trie.insert("jem")
print(trie.prefix("jack"))
