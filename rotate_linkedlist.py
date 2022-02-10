# given a linked list and a number k , rotate the linked list by k places

class Node:
    def __init__(self, value, next = None) -> None:
        self.value = value 
        self.next = next

    def __str__(self) -> str:
        current = self 
        ret = ''
        while current:
            ret += str(current.value)
            current = current.next
        return ret

def rotate_list(lst, k):
    dummy = Node(0)
    dummy.next = lst
    prev = curr = lst
    for i in range(k):
        curr = curr.next 
    while curr.next:
        prev = prev.next 
        curr = curr.next 
    curr.next = dummy.next 
    dummy.next = prev.next 
    prev.next = None 
        
    return dummy.next

lst= Node(1,Node(2, Node(3, Node(4, Node(5)))))
print(rotate_list(lst,2))