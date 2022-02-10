'''
Created on Jun 11, 2021
@author: phoebedo
'''
#Last in first out (push-pop)
#Restrictions: Push - pop - top - is_empty

#Different implementations: Fixed Array| Dynamic Array | Head Linked List | Tail Linked List

#Implementation with Fixed Array 
#pseudo code:
# struct stack{
    # int items[];
    # int top;
    # int maxsize;
# }

# FIXED SIZE
class Stack:
    def __init__(self, maxsize):
        self.items = [None] * maxsize
        self.maxsize = maxsize
        self.top = 0
    
    def push(self, value): #O(1)
        if (self.top < self.maxsize):
            self.items[self.top] = value
            self.top += 1
            return self.items
        else:
            return None

    def pop(self): #O(1)
        if self.top > 0:
            value = self.items[self.top - 1]
            self.items[self.top - 1] = None #No need
            self.top -= 1
            return value
        else:
            return None

    def peek(self): #O(1) //return top elem in the stack without removing it
        return self.stk[self.top-1]
    
    def is_empty(self): #O(1)
        return self.top == 0 

# stack = Stack(10)
# stack.push(1)
# stack.push(10)
# stack.pop()
# stack.pop()
# stack.pop()

#DYNAMIC ARRAY
           
class Stack:
    
    def __init__(self):
        self.items = []
    def top(self):
        return len(self.items - 1)
    def push(self,value):
        return self.items.append(value)
    def pop(self):
        if len(self.items) > 0:
            return self.items.pop()
        else:
            return None


#Linked List => Push to the Head  
# struct stack{
#     Node* head
#     Node* tail
#     int count
# }

class StackNode: 
    def __init__(self, data): #init a Node
        self.data = data
        self.next = None

class Stack:
    def __init__(self):
        self.head = None
    
    def is_empty(self):
        return True if self.head is None else False
    
    def push(self, data):
        newNode = StackNode(data)
        newNode.next = self.head
        self.head = newNode

        return
        
    def pop(self):
        if self.is_empty():
            return None
        temp = self.data
        self.data = self.data.next
        popped = temp.data
        return popped

    def top(self):
        if self.is_empty():
            return None
        return self.head.data




