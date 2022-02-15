# aka Prefix tree. A trie is an variant of an n-ary tree  in which characters are stored at each node. each path down the tree may represent a word. The null nodes are often used to indicate a complete word. 

class Node: 
    def __init__(self) -> None:
        self.children = {}
        self.count = 0 #how far is it from root 


class Trie:
    def __init__(self) -> None:
        self.root = Node()

    def insert(self, word):
        curr_node = self.root
        for c in word:
            if c not in curr_node.children:
                curr_node.children[c] = Node()
            curr_node = curr_node.children[c]
            curr_node.count += 1

    def unique_prefix(self, word):
        curr_node = self.root
        
        prefix = ""

        for c in word: 
            if curr_node.count == 1:
                return prefix
            else:
                curr_node = curr_node.children[c]
                prefix += c
        return prefix
        
    
def shortest_unique_prefix(words):
    trie = Trie()

    for word in words: 
        trie.insert(word)
    
    unique_pref = []
    for word in words:
        unique_pref.append(trie.unique_prefix(word))
    
    return unique_pref

print(shortest_unique_prefix(["joma", "jack", "jock", "john"]))
