from assign3 import *
class Stack:
    def __init__(self):
        self.mylist=SLL()
        self.count=0
    def is_empty(self):
        return self.mylist.is_empty()
    def push(self,data):
        self.mylist.insert_at_start(data)
        self.count+=1
    def pop(self):
        if not self.is_empty():
            self.mylist.delete_at_first()
            self.count-=1
    def peek(self):
        if not self.is_empty():
            return self.mylist.start.item
    def size(self):
        return self.count

s=Stack()
s.push(10)
s.push(20)
s.push(30)
print("top element is:",s.peek())
print(s.size())
s.pop()
print("Top element is:",s.peek())
print(s.size())
