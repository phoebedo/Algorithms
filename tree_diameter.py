# LC543e. diameter of binatry tree 

# The diameter of a binary tree is the length of the longest path between any two nodes in a tree. dont have to travel thru root

from turtle import left


class TreeNode():
    def __init__(self, value:int, left=None, right=None) -> None:
        self.value = value
        self.left = left
        self.right = right


def diameterOfBinaryTree(root):
    res = [0] 

    def dfs(root):
        # find the high
        if not root:
            return -1
        left = dfs(root.left)
        right = dfs(root.right)

        res[0] = max(res[0], 2+left+right)

        return 1+max(left,right)
    
    dfs(root)
    return res[0]