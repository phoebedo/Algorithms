# LC160e
def intersection_node(headA, headB):
    def get_length(head):
        if not head:
            return 0 
        return 1+get_length(head.next)
    lenA, lenB = get_length(headA), get_length(headB)
    currA, currB = headA, headB
    if lenA > lenB:
        for _ in range(lenA-lenB):
            currA = currA.next
    else:
        for _ in range(-lenA+lenB):
            currB = currB.next
    while currA != currB:
        currB = currB.next
        currA = currA.next
    

    return currA