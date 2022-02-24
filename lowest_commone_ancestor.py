# LC236m: lowest commong ancestor of binary tree 


class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
# p,q exist in the tree. No not found handling
def lowestCommonAncestor(self, root, p, q):
    # base case 
    if not root:
        return None 
    if root.val== p.val or root.val == q.val:
        return root

    left = lowestCommonAncestor(root.left, p,q)
    right = lowestCommonAncestor(root.right,p,q)

    if left and right:
        return root 
    elif not left and not right: 
        return None 
    return left if left else right
    

    
