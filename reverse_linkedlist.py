# reverse a singly linked list 

class Node:
    def __init__(self,value=0, next = None) -> None:
        self.value = value
        self.next = next
    def __repr__(self) -> str:
        return f"{self.value}{self.next}"
#recursive 
def reverse_list(head):
    if head is None or head.next is None:
        return head
    p = reverse_list(head.next)
    head.next.next= head
    head.next = None
    return p
# iterative 
def iter_reverse(head):
    prev =None
    curr = head
    while curr is not None:
        temp = curr.next 
        curr.next  = prev
        prev = curr
        curr = temp
    
    return prev

head = Node(1)
head.next = Node(2,Node(3,Node(4)))
print(iter_reverse(head))
