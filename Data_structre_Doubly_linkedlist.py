class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
        self.prev=None
class DoublyLinkedList:
    def __init__(self):
        self.head=None
        self.trail=None
        self.size=0
    def add(self, data):
        if self.head == None:
            new_node=Node(data)
            self.head=new_node
            self.size=self.size+1
            return
        new_node=Node(data)
        is_next=self.head
        while is_next.next != None:
            is_next = is_next.next
        is_next.next = new_node
        new_node.prev=is_next
        self.trail = new_node

    def show(self):
        if self.head is None:
            return
        is_prev=self.trail
        while is_prev:
            print(is_prev.data)
            is_prev = is_prev.prev
    def show2(self):
        if self.head is None:
            return
        is_next=self.head
        while is_next:
            print(is_next.data)
            is_next=is_next.next
    def remove(self,data):
        if self.head.data == data:
            self.head = self.head.next
            self.head.prev = None
            return
        is_next= self.head
        back=None
        while is_next:
            if is_next.data == data:
                back.next = is_next.next
                is_next.next.prev = back
                return
            back = is_next
            is_next = is_next.next
dl=DoublyLinkedList()
dl.add("tata motors")
dl.add("kia motors")
dl.add("Nissan")
dl.show()
print()
dl.show2()
print()
dl.remove("kia motors")
dl.show2()