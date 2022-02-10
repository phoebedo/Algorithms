# Linked list: each Node has value and pointer to the next Node (address: 0x00009)
#Implementation in C:
# struct Node{
#     int value;
#     struct Node*next;
# }

class Node:
    def __init__(self, value=0, next=None):
        self.value = value
        self.next = next


#Disadv: get_nth_elem: must go from head to second, to third.... -> nth. Because address of nth Node is retrieved by the pointer in the (n-1)th Node ===> O(n)

#Advantages: 
# links can be changed and does not have to be known in advance
# Dynamically allocates nodes >< Arr needs to be allocated with fixed amount of memory 
#Remove/add at front O(1) >< Array O(n)


#IMPLEMENTATIONS
#GET the Nth Elem
def get_nth_elem(head, n):
    count = 0
    current = head
    while current is not None:
        if count == n:
            return current.value
        count += 1
        current = current.next
    return None


#Search value in list 
'''return True if value is in the list. 
False if not'''
def search_value(head, val):
    current = head
    while current is not None:
        if current.value == val:
            return True
        current = current.next
    return False

#insert at front
def insert_front(head, val):
    node = Node()
    node.value = val
    node.next = head
#insert back
#     
#Remove with a given value
def remove_value(head, val):
    current = head
    if current.value == val:
        head = current.next
        current = None
        return
    while current is not None:
        previous = current
        if current.value == val:
            break
        current = current.next
    if current is None:
        return 
    previous.next = current.next
    current = None


class LinkedList:
    class Node:
        def __init__(self):
            pass
        def __init__(self):
            pass
    
        

#Linked List optimization, gonna take more memory 
# struct LinkedList{
#     Node * head;
#     Node * tail; => insertBack
#     int length; => length of linked list
# }
