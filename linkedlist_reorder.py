class Node:
    def __init__(self, value=0, next=None) -> None:
        self.value = value
        self.next=next

def reorderLinkedList(head):
    slow,fast = head,head.next
    # find second half of the list
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
    second = slow.next
    prev=slow.next=None

    # reverse second half
    while second:
        temp = second.next
        second.next=prev
        prev = second
        second=temp
    # prev become head of the reversed second half of the list
    # merge first half and second half(reversed)
    first,second = head,prev
    while second:
        temp1,temp2=first.next, second.next
        first.next = second
        second.next = temp1
        first,second=temp1,temp2
    

    
    

        
    