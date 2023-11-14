from tkinter import N
from types import resolve_bases


class Node :
    #  a value and a pointer
    def __init__(self,data=None):
        self.data = data
        self.nextval =None

class SlinkedLIst:
    def __init__(self):
        self.head = None
    
    def listPrint(self):
        printval =self.head
        while printval.nextval is not None:
            print(printval.data)
            printval = printval.nextval
    
    def insertNode(self,newdata):
        NewNode = Node(newdata)
        self.head = NewNode
        NewNode.nextval = self.head

    def contains (self,data):
        if self.isEmpty():
            raise StopIteration("list is empty")
        if  self.head == data:
            return True
        self.head = self.head.nextval
            
            
    
    def __len__(self):
        count = 0
        node =self.head
        while node:
            count +=1
            node = node.nextval
        return count
   
    def __node_iter(self):
       node = self.head
       while node:
           yield node
           node = node.next
    
    def __str__(self):
        return '->'.join(str[node] for node in self)      
     
    def __iter__(self):
       """ returns a vlue iterator""" 
       return iter(map(lambda node:self.value, self.__node_iter()))

    def deleteNode (self, key):
        temp = self.head

        if temp is not None:
            if (temp.data ==key):
                self.head = temp.nextval
                temp =None 
                return 
        while (temp is not None):
            if temp.data == key:
                break 
            prev = temp
            temp = temp.nextval

            # if key is not present 
        if (temp == None):
            return 
        prev.nextval = temp.nextval

        temp = None


            
