# 2 binary trees ->
# Boolean(s has and equal subtree in t)

class Node:
    def __init__(self,value, left=None,right=None) -> None:
        self.value = value
        self.left = left
        self.right= right

    #Transform tree into string. Using preorder traveral. O(n)
    def __repr__(self) -> str:
        return f"Value:{self.value} Left:{self.left} Right:{self.right}"
        
def find_substr(s,t):
    #transform tree to string 
    def preorder_traversal(node):
        if node is None:
            return ''
        return str(node.value)+ "-" +preorder_traversal(node.left)+ "-"+preorder_traversal(node.right)
    
    return preorder_traversal(s) in preorder_traversal(t)

t3 = Node(4,Node(3),Node(2))
t2 = Node(5, Node(4), Node(-1))
t = Node(1, t3, t2)

s= Node(3, Node(2), Node(5))

print(find_substr(s,t))
#Time O(n+m) where length(t)= m, length(s) = n
#Space O(m+n)