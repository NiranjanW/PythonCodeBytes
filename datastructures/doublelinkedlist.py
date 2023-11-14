class Node :
    def __init__(self,data=None):
        self.data = data
        self.prev_node = None
        self.next_node = None

class doubleLinked:
    def __init__(self):
        self.head = None

def reversal(head):
    current = head
    prev=None
    next_node = None

    while current:

        next_node = current.next_node
        current.next_node = prev
        prev =current

        current = next_node

        return prev

def nth_last_node(n,head):

    pointer_1 = head
    pointer_2 =head

    for i in range(n-1):

        # if no nnext node raise error 
        if not pointer_1.next_node:
            raise  LookupError('Error"Command continues past index of list')

        pointer_1 = pointer_1.next_node

        while pointer_1.next_node:
            # once the right pointer hits the end the left pointer has found the
      # nth to last node from the end
            pointer_2 = pointer_2.nextnode
            pointer_1 = pointer_1.nextnode
   
  
  # return the nth to last node
    return pointer_2
    

