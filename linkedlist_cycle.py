class Node:
    def __init__(self, value, next) -> None:
        self.value = value 
        self. next = next 

# Tortoise and Hare: Time O(n), Space O(1)
def cycle_linked_list(head):
    slow, fast = head, head
    while fast and fast.next is not None:
        slow = slow.next 
        fast = fast.next.next 
        if slow == fast:
            return True

    return False

# Hashmap/Hash set : Time O(n), Space O(n)
