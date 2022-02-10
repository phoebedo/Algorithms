# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        l = ListNode()
        exceed = 0
        result = l

        while (l1 or l2 or dec):
            if l1:
                l.value += l1.value
                l1 = l1.next
            if l2:
                l.value += l2.value
                l2 = l2.next
            
            l.value += exceed

            if l.value > 9:
                l.value = l.val%10
                exceed = 1
             
            else: exceed = 0
            
            if l1 or l2 or exceed:
                l_next = ListNode()
                l.next = l_next
                l = l_next
        
        return result

            
        
            
            
        