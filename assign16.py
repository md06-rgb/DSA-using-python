class PriorityQueue:
    def __init__(self):
        self.list=[]
    def push(self, data, priority):
        index=0
        while index<len(self.list) and self.list[index][1]<=priority:
            index+=1
        self.list.insert(index,(data,priority))
    def pop(self):
        if self.is_empty():
            raise IndexError("priorityQueue is empty")
        else:
            return self.list.pop(0)[0]
    def is_empty(self):
        return len(self.list)==0
    
    def size(self):
        return len(self.list)
p=PriorityQueue()
p.push("mohammad",1)
p.push("mohd",6)
p.push("md",8)
p.push("Ali",9)
p.push("me",2)
p.push("my",5)
print("size of priority queue is:",p.size())

while not p.is_empty():
    print(p.pop())
