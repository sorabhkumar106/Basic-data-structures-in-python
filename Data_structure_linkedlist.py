class Node:
    def __init__(self,data):
        self.data=data
        self.next_node=None
class Linkedlist:
    def __init__(self):
        self.head=None
        self.size=0
    def inseart_at_beging(self,data):
        if self.head is None:
            self.size=self.size+1
            self.head=Node(data)
            return
        self.size=self.size+1
        new_node=Node(data)
        new_node.next_node=self.head
        self.head=new_node
    def inseart_at_end(self,data):
        if self.head is None:
            self.head=Node(data)
            self.size=self+1
            return
        is_next=self.head
        while is_next.next_node is not None:
            is_next=is_next.next_node
        is_next.next_node=Node(data)
        self.size=self.size+1
        return
    def __len__(self):
        return self.size
    def show(self):
        is_next=self.head
        while is_next:
            print(is_next.data)
            is_next=is_next.next_node
    def remove_at_first(self):
        if self.head is None:
            return
        value=self.head.data
        self.head=self.head.next_node
        self.size=self.size-1
        return value
    def remove(self,data):
        if self.head is None:
            return
        is_next=self.head
        previous=None
        while is_next.next_node:
            if is_next.data == data:
                previous.next_node=is_next.next_node
                self.size=self.size-1
                return
            previous=is_next
            is_next=is_next.next_node

l=Linkedlist()
l.inseart_at_beging("tata motors")
l.inseart_at_beging("maruti suzuki")
l.inseart_at_beging("hundayi")
l.inseart_at_beging("mahindra rise")
l.inseart_at_beging("kia")
l.inseart_at_end("Nissan")
l.inseart_at_end("Renult")
print(len(l))
l.show()
print()
print(len(l))
print((l.remove("Nissan")))
print(len(l))
l.show()