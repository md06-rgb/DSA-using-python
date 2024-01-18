class Queue:
    def __init__(self):
        self.list=[]
    def is_empty(self):
        return len(self.list)==0
    def enqueue(self,data):
        self.list.append(data)
    def dequeue(self):
        if not self.is_empty():
            self.list.pop(0)
        else:
            raise IndexError("Queue underflow")
    def get_front(self):
        if not self.is_empty():
            return self.list[0]
        else:
            raise IndexError("Queue underflow")
    def get_rear(self):
        if not self.is_empty():
            return self.list[-1]
        else:
            raise IndexError("Queue underflow")
    def size(self):
        return len(self.list)
q=Queue()
try:
    print(q.get_front())
except IndexError as e:
    print(e.args[0])
q.enqueue(10)
q.enqueue(20)
q.enqueue(30)
print("Front=",q.get_front())
print("Rear=",q.get_rear())
q.dequeue()
print()
print('After call of dequeue function')
print("Front=",q.get_front())
print("Rear=",q.get_rear())

