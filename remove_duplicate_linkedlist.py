class Node: 
    def __init__(self,value, next=None) -> None:
        self.value = value 
        self.next = next 
    def __repr__(self) -> str:
        return f"{self.value},{self.next}"
def remove_duplicate(lst):
    prev = curr = lst
    if curr.next == None:
        return lst
    curr = curr.next 
    seen = set()
    
    while curr:
        seen.add(prev.value)
        print(seen)
        print(prev,curr)
        if curr.value in seen:
            prev.next = curr.next
            curr = curr.next
        else:
            prev = prev.next 
            curr = curr.next 
    return lst


lst = Node(1,Node(2, Node(3,Node(2,Node(4,Node(3,Node(1)))))))
remove_duplicate(lst)
print(lst)

# easier if linked list is sorted 
