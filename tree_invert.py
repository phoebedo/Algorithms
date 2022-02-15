# LC226 Invert Binary tree 
from operator import invert


class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def invertBinaryTree(root):
    if root==None:
        return root
    left = invertBinaryTree(root.right)
    right = invertBinaryTree(root.left)
    root.right = left 
    root.left = right
    
    return root