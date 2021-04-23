class Node:
    def __init__(self,data):
        self.data=data
        self.rightchild=None
        self.leftchild=None
        self.height=0
class AVL:
    def __init__(self):
        self.root=None
    def calcHeight(self,node):
        if not node:
            return -1
        return node.height
    def calcBalance(self,node):
        if not node:
            return 0
        return self.calcHeight(node.leftchild)-self.calcHeight(node.rightchild)
    def rotateRight(self,node):
        print("Rotating to the right on node",node.data)
        templeftchild=node.leftchild
        t=templeftchild.rightchild
        templeftchild.rightchild=node
        node.leftchild=t
        templeftchild.height=max(self.calcHeight(templeftchild.leftchild),self.calcHeight(templeftchild.righchild))+1
        node.height=max(self.calcHeight(node.righchild),self.calcHeight(node.leftchild))+1
        return templeftchild
    def rotateLeft(self,node):
        print("Roatataing to left on node",node.data)
        temprightchild=node.rightchild
        temp=temprightchild.leftchild
        temprightchild.leftchild=node
        node.rightchild=temp
        node.height=1+max(self.calcHeight(node.rightchild),self.calcHeight(node.leftchild))+1
        temprightchild.height=1+max(self.calcHeight((temprightchild.rightchild),temprightchild.leftchild))
        return temprightchild
    def getPredecessor(self,node):
        if node.rightchild:
            return self.getPredecessor(node.rightchild)
        return node
    def settleViolance(self,data,node):
        balance=self.calcBalance(node)
        if balance>1 and data<node.leftchild.data:
            print("left heavy situation")
            return self.rotateRight()
        if balance<0 and data>node.rightchild.data:
            print("Right heavy situation")
            return self.rotateLeft(node)
        if balance>1 and data>node.leftchild.data:
            node.leftchild=self.rotateLeft(node.leftchild)
            return self.rotateRight(node)
        if balance<0 and data<node.rightchild.data:
            print("right left situation")
            node.rightchild=self.rotateRight(node.rightchild)
            return  self.rotateLeft(node)
    def remove(self,data):
        if self.root:
            self.root=self.removeNode(data,self.root)
    def removeNode(self,data,node):
        if not node:
            return node
        if data<node.data:
            node.leftchild=self.removeNode(data,node.leftchild)
        elif data>node.data:
            node.rightchild=self.removeNode(data,node.rightchild)
        else:
            if not node.leftchild and not node.rightchild:
                del node
                return None
            if not node.rightchild:
                print("removing node with single leftchild")
                tempLeft=node.leftchild
                del node
                return tempLeft
            elif not node.leftchild:
                print("Removing node with single rightchild")
                tempRight=node.rightchild
                del node
                return tempRight
            print("removing node with two children")
            tempNode=self.getPredecessor(node.leftchild)
            node.data=tempNode.data
            node.leftchild=self.removeNode(tempNode.data,node.leftchild)
            if not node:
                return node
            node.height=max(self.calcHeight(node.leftchild),self.calcHeight(node.rightchild))+1
            balance=self.calcBalance(node)
            if balance>1 and self.calcBalance(node.leftchild)>=0:
                return self.rotateRight()
            if balance<-1 and self.calcBalance(node.rightchild)<0:
                node.leftchild=self.rotateLeft(node.leftchild)
                return self.rotateRight(node)
            if balance<-1 and self.calcBalance(node.rightchild)<=0:
                return self.rotateLeft(node)
            if balance<-1 and self.calcBalance(node.rightchild)>0:
                node.rightchild=self.rotateRight(node.rightchild)
                return  self.rotateLeft(node)
            return node
    def insert(self,data):
        if self.root is None:
            self.root=Node(data)
            return
        self.root=self.insertNode(data,self.root)
    def insertNode(self,data,node):
        if node is None:
            return 0
        if data<node.data:
            if node.leftchild is None:
                node.leftchild=Node(data)
            else:
                self.insertNode(data,node.leftchild)
        elif data>node.data:
            if node.rightchild is None:
                node.rightchild=Node(data)
                return True
            else:
                self.insertNode(data,node.rightchild)
        else:
            return None
        node.height=max(self.calcHeight(node.rightchild),self.calcHeight(node.rightchild))+1
        return self.settleViolance(data,node)
    def show(self , node):
        if node == None:
            return
        print(node.data)
        self.show(node.leftchild)
        self.show(node.rightchild)
v=AVL()
v.insert(1)
v.insert(2)
v.show(v.root)