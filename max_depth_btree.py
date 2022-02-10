class TreeNode:
    def __init__(self,value,left=None,right=None) -> None:
        self.value = value 
        self.left = left
        self.right = right 
# recursion
def max_depth(root):
    if  root is None:
        return 0
        
    return max(max_depth(root.left), max_depth(root.right)) +1

# iterative 
def max_iter(root):
    stack=[]
    if root is not None:
        stack.append((1,root))
    depth = 0
    while stack != []:
        curr_depth, root = stack.pop()
        if root is not None:
            depth = max(depth,curr_depth)
            stack.append((curr_depth+1,root.left))
            stack.append((curr_depth+1,root.right))
    return depth
