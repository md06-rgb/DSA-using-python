class Node:
    def __init__(self,item=None,next=None):
        self.item=item
        self.next=next
class Queue:
    def __init__(self):
        self.front=None
        self.rear=None
        self.count=0
    def is_empty(self):
        return self.front is None
    def enqueue(self,data):
        n=Node(data)
        if self.is_empty():
            self.front=n
        else:
            self.rear.next=n
        self.rear=n
        self.count+=1
    def dequeue(self):
        if self.is_empty():
            raise IndexError("queue is empty")
        elif self.front==self.rear:
            self.front=None
            self.rear=None
        else:
            self.front=self.front.next
        self.count-=1
    def get_front(self):
        if self.is_empty():
            raise IndexError("Queue is empty")
        else:
            return self.front.item
    def get_rear(self):
        if self.is_empty():
            raise IndexError("Queue is empty")
        else:
            return self.rear.item
    def size(self):
        return self.count
q=Queue()
q.enqueue(10)
q.enqueue(20)
q.enqueue(30)

print("Front element is:",q.get_front())
print("Rear element is:",q.get_rear())
print("Size of Queue is:",q.size())

q.dequeue()
print()
print("After call dequeue function:")
print("Front element is:",q.get_front())
print("Rear element is:",q.get_rear())
print("Size of Queue is:",q.size())
q.dequeue()
print()
print("once again after call dequeue function:")
print("Front element is:",q.get_front())
print("Rear element is:",q.get_rear())
print("Size of Queue is:",q.size())