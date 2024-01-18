class Node:
    def __init__(self,item=None,priority=None,next=None):
        self.item=item
        self.priority=priority
        self.next=next
class PriorityQueue:
    def __init__(self,start=None):
        self.start=start
        self.count=0
    def is_empty(self):
        return self.start is None
    def push(self,data,priority):
        n=Node(data,priority)
        if self.is_empty() or self.start.priority > priority:
            n.next=self.start
            self.start=n
            
        else:
            temp=self.start
            while temp.next is not None and temp.next.priority < priority:
                temp=temp.next
            n.next=temp.next
            temp.next=n
        self.count+=1
    def pop(self):
        if self.is_empty():
            raise IndexError("priority queue is empty")
        data=self.start.item
        self.start=self.start.next
        return data
        self.count-=1
    def size(self):
        return self.count
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
