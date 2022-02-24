# Path from root to a given node in a binary tree

from turtle import right
from typing import List


class TreeNode():
    def __init__(self,val,left=None,right=None) -> None:
        self.val = val
        self.left = left
        self.right = right


def findPath(root:TreeNode,x:int) -> List:
    res = []

    if not root:
        return None
    if root.val == x:
        return root
    leftpath = findPath(root.left,x)
    rightPath = findPath(root.right,x)

    res.append(root,leftpath) if leftpath else res.append(root,rightPath)

    return res

