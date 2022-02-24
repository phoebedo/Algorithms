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


class MyCircularQueue(object):

    def __init__(self, k):
        """
        :type k: int
        """
        self.front = self.rear = self.size = 0 
        self.items = [None]*k
        self.maxsize = k
        

    def enQueue(self, value):
        """
        :type value: int
        :rtype: bool
        """
        if self.isFull():
            return False
        
        self.items[self.rear] = value
        self.rear +=1 
        if self.rear >= self.maxsize:
            self.rear = 0 
        self.size +=1
        return True

    def deQueue(self):
        """
        :rtype: bool
        """
        if self.isEmpty():
            return False
        
        self.front += 1
        if self.front >= self.maxsize:
            self.front = 0
        self.size -= 1
        return True
        

    def Front(self):
        """
        :rtype: int
        """
        if self.isEmpty():
            return -1
        return self.items[self.front]
        

    def Rear(self):
        """
        :rtype: int
        """
        if self.isEmpty():
            return -1
        return self.items[self.rear-1]
        

    def isEmpty(self):
        """
        :rtype: bool
        """
        return self.size == 0 

    def isFull(self):
        """
        :rtype: bool
        """
        return self.size == self.maxsize
        


# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()


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
    
# Circular Queue - rewrite


