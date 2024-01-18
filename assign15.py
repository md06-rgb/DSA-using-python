class Node:
    def __init__(self,prev=None,item=None,next=None):
        self.prev=prev
        self.item=item
        self.next=next
class Dequeue:
    def __init__(self):
        self.front=None
        self.rear=None
        self.count=0
    def is_empty(self):
        return self.front is None
    def insert_front(self,data):
        n=Node(None,data,self.front)
        if self.is_empty():
            self.rear=n
        else:
            self.front.prev=n
        self.front=n
        self.count+=1
    def insert_rear(self,data):
        n=Node(self.rear,data,None)
        if self.is_empty():
            self.front=n
        else:
            self.rear.next=n
        self.rear=n
        self.count+=1
    def delete_front(self):
        if self.is_empty():
            raise IndexError("Dequeue is empty")
        else:
            self.front.next.prev=None
            self.front=self.front.next
        self.count-=1
    def delete_rear(self):
        if self.is_empty():
            raise IndexError("Dequeue is empty")
        else:
            self.rear.prev.next=None
            self.rear=self.rear.prev
        self.count-=1
    def get_front(self):
        if self.is_empty():
            raise IndexError("Dequeue is empty")
        else:
            return self.front.item
    def get_rear(self):
        if self.is_empty():
            raise IndexError("Dequeue is empty")
        else:
            return self.rear.item
    def size(self):
        return self.count
d=Dequeue()
d.insert_front(20)
d.insert_front(10)
print("front element is:",d.get_front())
print("rear element is:",d.get_rear())
print("size of Dequeue is:",d.size())
print()
d.insert_rear(30)
print("front element is:",d.get_front())
print("rear element is:",d.get_rear())
print("size of Dequeue is:",d.size())
print()
d.insert_rear(40)
print("front element is:",d.get_front())
print("rear element is:",d.get_rear())
print("size of Dequeue is:",d.size())
print()
d.delete_front()
print("front element is:",d.get_front())
d.delete_rear()
print("Rear element is:",d.get_rear())
print("size of Dequeue is:",d.size())
