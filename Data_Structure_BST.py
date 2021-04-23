class Node:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None

class BST:
    def __init__(self):
        self.root=None
    def insert1(self,data,node):
        if self.root == None:
            self.root=Node(data)
            return
        if data<node.data:
            if node.left is None:
                node.left=Node(data)
                return
            else:
                self.insert1(data,node.left)
        elif data>node.data:
            if node.right is None:
                node.right=Node(data)
            else:
                self.insert1(data,node.right)
        else:
            print("Sorry , You are trying to insert duplicate value")
            return
    def insert(self,data):
        self.insert1(data,self.root)
    def search(self,data):
        return self.search1(data,self.root)
    def search1(self,data,node):
        if node:
            if data==node.data:
                return True
            elif  data<node.data:
                return self.search1(data,node.left)
            elif data>node.data:
                return  self.search1(data,node.right)
            else:
                return "your given data not found"
    def show(self):
        self.inorder(self.root)
    def inorder(self,start):
        if start:
            self.inorder(start.left)
            print(start.data)
            self.inorder(start.right)
        return
    def getmax(self,node):
        if node:
            if node.right:
                return  self.getmax(node.right)
            return node.data
    def get_min(self,node):
        if node:
            if node.left:
                return self.get_min(node.left)
        return  node.data
    def removeNode(self,data,node):
        if not node:
            return node
        if data<node.data:
            node.left=self.removeNode(data,node.left)
        elif data>node.data:
            node.right=self.removeNode(data,node.right)
        else:
            if not node.left and not node.right:
                print("removing leaf node")
                del node
                return None
            if not self.left:
                print("removing node with right child")
                temp=node.right
                del node
                return temp
            elif not self.right:
                print("removing node with left child ")
                temp=node.left
                del node
                return temp
            tempnode=self.get_preceddor(node.left )
            node.data=tempnode.data
            node.left=self.removeNode(tempnode.data,node.left)
    def get_preceddor(self,node):
        if node.right:
            return  self.get_preceddor(node.right)
        return node
bst=BST()
bst.insert(2)
bst.insert(25)
bst.insert(7)
bst.insert(645)
bst.insert(87)
bst.show()
print(bst.removeNode(7,bst.root))
bst.show()