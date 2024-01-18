from assign3 import *
class Stack(SLL):
    def __init__(self):
        super().__init__()
        self.count=0
    def is_empty(self):
        return super().is_empty()
    def push(self,data):
        self.insert_at_start(data)
        self.count+=1
    def pop(self):
        if not self.is_empty():
            self.delete_at_first()
            self.count-=1
        else:
            raise IndexError("stack underflow")
    def peek(self):
        if not self.is_empty():
            return self.start.item
        else:
            raise IndexError("stack underflow")
    def size(self):
        return self.count
s=Stack()
s.push(10)
s.push(20)
s.push(30)
print("Top element is",s.peek())
print(s.size()) 
s.pop()
print("Top element is:",s.peek())  
print(s.size())