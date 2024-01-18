class Node:
    def __init__(self,item=None,next=None):
        self.item=item
        self.next=next
class SLL:
    def __init__(self,start=None):
        self.start=start
    def is_empty(self):
        return self.start==None
    def insert_at_start(self,data):
        n=Node(data)
        if self.start is None:
            self.start=n
        else:
            n.next=self.start
            self.start=n
    def insert_at_last(self,data):
        n=Node(data)
        if self.start is None:
            self.start=n
        else:
            temp=self.start
            while temp is not None:
                if temp.next==None:
                    temp.next=n
    def search(self,data):
            temp=self.start
            while temp is not None:
                if temp.item==data:
                    return temp
                temp=temp.next
            return None
    def insert_after(self,temp,data):
        if temp is not None:
            n=Node(data,temp.next)
            temp.next=n
    def print_list(self):
        temp=self.start
        while temp is not None:
            print(temp.item,end=' ')
            temp=temp.next
    def delete_at_first(self):
        if self.start is not None:
            self.start=self.start.next
        else:
            return None
    def delete_at_last(self):
        if self.start is not None:
            temp=self.start
            while temp.next.next is not None:
                temp=temp.next
            temp.next=None
        else:
            return None
    def delete_item(self,data):
        if self.start is None:
            return None
        elif self.start.next is None and self.start.item is data:
            self.start=None
        else:
            temp=self.start
            while temp.item !=data:
                temp=temp.next
            n=self.start
            while n is not None:
                if n.next is  temp:
                    return n
                else:
                    n=n.next
            n.next=temp.next            
#driver code
# mylist=SLL()
# mylist.insert_at_last(30)
# mylist.insert_at_start(20)
# mylist.insert_at_start(10)
#mylist.insert_after(mylist.search(20),25)
#mylist.print_list() #print 10 20 25 30
#print()
#print("now deleting one by one:")
#mylist.delete_at_first()
#mylist.print_list()
#print()
#mylist.delete_at_last()
#mylist.print_list()
#print()
#mylist.delete_item(20)
#mylist.print_list()
#print()


