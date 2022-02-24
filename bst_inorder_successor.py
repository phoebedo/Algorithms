# Note:
# - If  right child. To right then go as left as possible 
#If no right child, go up until first right

from logging.config import valid_ident


class Node:
    def __init__(self,value, left=None, right=None, parent = None) -> None:
        self.value = value
        self.left = left 
        self.right = right
        self.parent = parent
    def __repr__(self) -> str:
        return f"Value:{self.value} Left:{self.left} Right: {self.right}"


    
def successor(node):
    if node.right:
        curr = node.right
        while curr.left:
            curr = curr.left
        return curr.value
    
    curr = node 
    parent = node.parent
    while parent and parent.left is not curr:
        curr = parent
        parent = parent.parent
    return parent.value

    
tree = Node(3)
tree.left= Node(2)
tree.right = Node(4)
tree.left.parent = tree
tree.right.parent = tree
tree.left.left = Node(1)
tree.left.left.parent = tree.left
tree.right.right = Node(5)
tree.right.right.parent = tree.right

print(successor(tree.left))



# if dont have pointer back to parent?


class TreeNode:
    def __init__(self,val,left=None,right=None) -> None:
        self.val = val
        self.left = left 
        self.right = right


def inorderSucessor(root:TreeNode, p:TreeNode)->TreeNode:

    if not root:
        return None
    cur = root 
    prev = None
    while cur:
        if cur.val>p.val:
            prev= cur
            cur = cur.left
        else:
            cur = cur.right

    return prev

