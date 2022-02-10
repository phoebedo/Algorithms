# LC226e
# left child <--> right child 
class Node:
    def __init__(self,val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def invert_tree(root):
    if root== None:
        return root
        
    left = invert_tree(root.left)
    right = invert_tree(root.right)
    root.left = right
    root.right = left 
    
    return root
   