class Stack:
    def __init__(self):
        self.stack=[]
    def push(self,data):
        self.stack.append(data)
    def pop(self):
        value=self.stack[-1]
        del self.stack[-1]
        return value
    def peek(self):
        return self.stack[-1]
    def size(self):
        return  len(self.stack)
    def is_empty(self):
        return  self.stack==[]
    def show(self):
        for comp in self.stack:
            print(comp)
stack=Stack()
stack.push("tata motors")
stack.push("ford motors")
stack.push("kia motors")
stack.push("yamaha motors")
stack.show()
print()
print(stack.pop())
print()
stack.show()
print(stack.size())