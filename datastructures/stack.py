
class Node:
    def __init__(self,value):
        self.value = value
        self.next = None

class Stack:

    def __init__(self):
        self.head = Node("head")
        self.size = 0
    
    def __str__(self):
        cur = self.head.next

        while cur:
            print(cur.value)
            

    def size(self):
        return self.size
    
    def isEmpty(self):
        return self.size == 0

    def peek(self):
        if self.isEmpty():
            raise Exception("Peeking from a empty stack")
        return self.head.next.value

    
    def push(self ,value):
        node = Node(value)
        node.next = self.head.next
        self.head.next = node
        self.size += 1

      