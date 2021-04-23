class TreeNode(object):
    def __init__(self,val):
        self.val=val
        self.left=None
        self.right=None
        self.height=1


class AVL(object):
    def insert(self,root,key):
        if not root:
            return TreeNode(key)
        elif key<root.val:
            root.left=self.insert(root.left,key)
        else:
            root.right=self.insert(root.right,key)
        root.height=1+max(self.getHeight(root.left),self.getHeight(root.right))
        balance=self.getBalance(root)
        if balance>1 and key<root.left.val:
            return self.rotateRight(root)
        if balance < -1 and key > root.right.val:
            return self.rotateLeft(root)
        if balance > 1 and key > root.left.val:
            root.left=self.rotateLeft(root.left)
            return self.rotateRight(root)
        if balance < -1 and key < root.right.val:
            root.right=self.rotateRight(root.right)
            return root.rotateLeft(root)
        return root
    def rotateLeft(self,z):
        y=z.right
        temp=y.left
        y.left=z
        z.right=temp
        z.height=max(self.getHeight(z.left),self.getHeight(z.right))+1
        y.height=max(self.getHeight(y.left),self.getHeight(y.right))+1
        return y
    def rotateRight(self,z):
        y=z.left
        temp=y.right
        y.right = z
        z.left = temp
        z.height=max(self.getHeight(z.left),self.getHeight(z.right))+1
        y.height=max(self.getHeight(y.left),self.getHeight(y.right))+1
        return y
    def getHeight(self,root):
        if not root:
            return
        return root.height
    def getBalance(self,root):
        if root is None:
            return 0
        return self.getHeight(root.left)-self.getHeight(root.right)
    def preorder(self,root):
        if root is None:
            return
        print(root.val,"  ",end='')
        self.preorder(root.left)
        self.preorder(root.right)
a=AVL()
root=None
root=a.insert(root,10)
root=a.insert(root,20)
root=a.insert(root,30)
root=a.insert(root,40)
root=a.insert(root,50)
root=a.insert(root,60)