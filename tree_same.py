# LC100e same tree. return true if 2 trees are the same else false 

class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def isSameTree(p,q):
    if not p and not q:
        return True 
    if not p or not q or p.val != q.val:
        return False
    return isSameTree(p.left,q.left) and isSameTree(p.right,q.right)