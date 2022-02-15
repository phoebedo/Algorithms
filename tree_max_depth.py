# LC104 maximum depth of binary tree 
# Given the root of a binary tree, return its maximum depth.
from collections import deque


class TreeNode():
    def __init__(self, value:int, left=None, right=None) -> None:
        self.value = value
        self.left = left
        self.right = right
#Recursion
def maxDepth(root):
    if root is None:
        return 0

    return 1+ max(maxDepth(root.left), maxDepth(root.right))


# BFS 
def maxDepthBFS(root):
    if not root:
        return 0 
    level =0
    q = deque([root])

    while q:
        for i in range(len(q)):
            node = q.popleft()
            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)
        level += 1
    return level 

# Interative DFS. preorder dfs 
# adding tuple (node, depth) to the stack 

def maxDepthDFS(root):
    if not root:
        return 0
    stack = [(root,1)]
    res  = 1
    while stack:
        node, depth = stack.pop
        if node:
            res = max(res, depth)
            stack.append((node.left, depth+1))
            stack.append((node.left, depth+1))


    return res


# Time (all same) O(n) visit each node once. 