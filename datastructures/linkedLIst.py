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


    

    def deleteNode (self, key):
        temp = self.head

        if temp is not None:
            if (temp.data =key):
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


            
