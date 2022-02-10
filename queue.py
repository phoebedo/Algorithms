#FIFO 
# two pointers: front and rear. The front points the first and rear points to last item.

# enQueue() This operation adds a new node after rear and moves rear to the next node.

# deQueue() This operation removes the front node and moves front to the next node

#Circular queue : enQueue() deQueue() take constant time O(1)

# ARRAY IMPLEMENTATION
# struct queue{
#     int arr[]
#     int front
#     int rear
#     int maxsize
# }


class Queue:
    def __init__(self, maxsize):
        self.front = self.size = 0
        self.rear = maxsize - 1
        self.items = [None] * maxsize
        self.maxsize = maxsize
    
    def is_empty(self):
        return self.size == 0
    
    def is_full(self):
        return self.size == maxsize
        
    def enQueue(self, item):
        if self.is_full():
            return
        self.rear += 1
        self.items[self.rear] = item
        self.size += 1
        return self.items
    
    def deQueue(self):
        if self.is_empty():
            return
        dequeued = self.items[self.front]
        self.front += 1
        self.size -= 1
        return dequeued

    def front(self):
        return self.items[self.front]
    
    def rear(self):
        return self.items[self.rear]


# Enque    O(1)
# Deque    O(1)
# Front    O(1)
# Rear     O(1)      
        
# Auxiliary Space: O(N). 
# N is the size of array for storing elements.


# Linked List IMPLEMENTATION

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class Queue:
    def __init__(self):
        self.front = self.rear = None

    def is_empty(self):
        return self.front == None

    def enQueue(self, item):
        queue_node = Node(item)

        if self.rear == None:
            self.front = self.rear = queue_node
            return
        
        self.rear.next = queue_node
        self.rear = temp

    def deQueue(self):
        
        if self.is_empty():
            return
        
        temp = self.front
        self.front = temp.next

        if (self.front == None):
            self.rear = None
        
        
# Double-Ended Queues
# enqueue and dequeue from both front and back in constant time O(1)
#DOUBLY LINKED LIST
# pseudoCode:
# struct Node{
#     int value
#     Node * next
#     Node* prev
# }

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None    
        