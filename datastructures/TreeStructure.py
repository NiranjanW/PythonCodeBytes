
class Node:
    def __init__(self,data):
        self.data = data
        self.left =None
        self.right =None
    
    def PrintTree(self):
        if self.left:
            self.left.PrintTree()
        print(self.data)
        if self.right:
            self.right.PrintTree()

    def insert(self, data):
        if self.data:
            if data < self.data:
                if self.left == None:
                    self.left = Node(data)
                else:
                    self.left.insert(data)
            elif data > self.data:
                if self.right == None:
                    self.right = Node(data)
                else:
                    self.right.insert(data)
        else:
            self.data = data
# Inorder traversal
# Left -> Root -> Right      
    def inorderTraversal(self, root):
        res =[]
        if root:
            res = self.inorderTraversal(root.left)
            res.append(root.data)
            res = res + self.inorderTraversal(root.right)
        return res


root =Node(12)
root.insert(6)
root.insert(14)
root.insert(3)
root.PrintTree()

