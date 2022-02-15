# LC230 m 
# Given the root of a binary search tree, and an integer k, return the kth smallest value (1-indexed) of all the values of the nodes in the tree.

# non-optimal: store tree in sorted array; 
# iterative dfs in-order and return the kth element processed,
# go left until null, pop, go right once;
from collections import deque


def kthSmallest(root,k):
    n = 0 
    stack = []
    cur = root

    while cur or stack:
        while cur:
            stack.append(cur)
            cur = cur.left 
        cur = stack.pop()
        n+=1
        if n == k :
            return cur.val
        cur = cur.right





    