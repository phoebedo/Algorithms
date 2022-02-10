# LC110e

from typing import Tuple
class Node:
    def __init__(self,val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def is_balanced(root) -> bool:
    def is_balanced_helper(root)->Tuple[bool,int]:
        if root == None:
            return (True,0)

        left_balanced, left_high = is_balanced_helper(root.left)
        right_balanced, right_high = is_balanced_helper(root.right)

        return(left_balanced and right_balanced and abs(left_high - right_high)<=1, max(left_high, right_high)+1)
    
    return is_balanced_helper(root)[0] #return boolean only


