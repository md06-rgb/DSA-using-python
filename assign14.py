class Deque:
    def __init__(self):
        self.list=[]
    def is_empty(self):
        return len(self.list) is None
    def insert_front(self,data):
        self.list.insert(0,data)
    def insert_rear(self,data):
        self.list.append(data)
    def get_front(self):
        if self.is_empty():
            raise IndexError("List is empty")
        else:
            return self.list[0]
    def get_rear(self):
        if self.is_empty():
            raise IndexError("List is empty")
        else:
            return self.list[-1]
    def delete_front(self):
        if self.is_empty():
            raise IndexError("List is empty")
        else:
            return self.list.pop(0)
    def delete_rear(self):
        if self.is_empty():
            raise IndexError("List is empty")
        else:
            return self.list.pop(-1)
    def size(self):
        return len(self.list)
    
d=Deque()
d.insert_front(20)
d.insert_front(10)
d.insert_rear(30)
d.insert_rear(40)
print("Front element is:",d.get_front())
print("Rear element is:",d.get_rear())
print("Size of list is:",d.size())
print()
print("After delete_front function call front element is:")
d.delete_front()
print("Front element is:",d.get_front())
print("Rear element is:",d.get_rear())
print("Size of list is:",d.size())
print()
print("After delete_rear function call Rear element is:")
d.delete_rear()
print("Front element is:",d.get_front())
print("Rear element is:",d.get_rear())
print("Size of list is:",d.size())