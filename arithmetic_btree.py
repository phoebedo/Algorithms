class Node:
    def __init__(self,val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

PLUS = "+"
MINUS = "-"
TIMES = "*"
DIVIDE = "/"

def evaluate(root):
    if root.val == PLUS:
        return evaluate(root.left)+ evaluate(root.right)
    elif root.val == MINUS:
        return evaluate(root.left)- evaluate(root.right)
    elif root.val == TIMES:
        return evaluate(root.left)* evaluate(root.right)
    elif root.val == DIVIDE:
        return evaluate(root.left)/ evaluate(root.right)
    else:
        return root.val

tree = Node(TIMES)
tree.left = Node(PLUS,Node(3), Node(2))
tree.right= Node(PLUS,Node(4), Node(5))
print(evaluate(tree))