class Heap(object):
    def __init__(self,size):
        self.size=size
        self.heap=[0]*size
        self.current_index=-1
    def insert(self,data):
        if self.isFull():
            return
        self.current_index+=1
        self.heap[self.current_index] = data
        self.fixUp(self.current_index)
    def fixUp(self,index):
        parent_index=int((index-1)/2)
        while parent_index >= 0 and self.heap[parent_index] < self.heap[index]:
            temp=self.heap[parent_index]
            self.heap[parent_index]=self.heap[index]
            self.heap[index] = temp
            index = parent_index
            parent_index = int((index-1)/2)
    def show(self):
        s=self.current_index+1
        for i in range(s):
            print(self.heap[i]," ",end="")

    def isFull(self):
        if self.current_index==self.size:
            return True
        else:
            return False
    def remove(self):
        self.heap[0]=self.heap[self.current_index]
        self.heap[self.current_index] = 0
        self.current_index = self.current_index-1
        self.fixDown()
    def fixDown(self):
        index=0
        upto=self.current_index
        while index <= upto:
            lefchild=int(2*index+1)
            rightchild=int(2*index+2)
            if lefchild < upto:
                if rightchild>upto:
                    swapindex=lefchild
                    if self.heap[rightchild]<self.heap[lefchild]:
                        swapindex=lefchild
                    else:
                        swapindex=rightchild
                    if self.heap[swapindex] < self.heap[index]:
                        break
                    else:
                        temp=self.heap[swapindex]
                        self.heap[swapindex]=self.heap[index]
                        self.heap[index]=temp
                        index=swapindex
                else:
                    break
t=Heap(5)
t.insert(44)
t.insert(64)
t.insert(876)
t.insert(120)
t.show()
t.remove()
print()
t.show()