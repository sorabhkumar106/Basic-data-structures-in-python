class Queue:
    def __init__(self):
        self.queue=[]
    def enqueue(self,data):
        self.queue.append(data)
    def dequeue(self):
        value=self.queue[0]
        del self.queue[0]
        return value
    def size(self):
        return  len(self.queue)
    def is_empty(self):
        return self.queue==[]
    def show(self):
        for comp in self.queue:
            print(comp)
q=Queue()
q.enqueue("tata motors")
q.enqueue("kia motors")
q.enqueue("yamaha motors")
q.enqueue("tvs motors")
q.enqueue("hero motors")
q.enqueue("hundayi motors")
q.show()
print()
print(q.dequeue())
print(q.show())