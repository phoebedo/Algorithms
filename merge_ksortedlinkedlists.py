class ListNode:
    def __init__(self, val) -> None:
        self.val = val
        self.next = None


def merge_klist(lists):
    def merge_2lists(l1,l2):
        dummy = curr = ListNode(0)
        while l1 and l2:
            if l1.val < l2.val:
                curr.next = l1
                l1 = l1.next 
            else:
                curr.next = l2
                l2 = l2.next
            curr = curr.next
        if not l1:
            curr.next = l2
        else:
            curr.next= l1
        return dummy.next
    
    k = len(lists)
    if k == 0:
        return None
    if k == 1:
        return lists[0]
    #recursive
    # else: 
    #     left = merge_klist(lists[:k//2])
    #     right = merge_klist(lists[k//2:])
    #     return merge_2lists(left, right)

    # iterative
    interval = 1
    while interval < k: #log(k) times
        for i in range(0, k - interval, interval*2):
            lists[i]= merge_2lists(lists[i],lists[i+interval])
        interval *= 2
    return lists[0]
