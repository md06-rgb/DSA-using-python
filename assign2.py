class Person:
    def __init__(self,name=None,age=None):
        self.name=name
        self.age=age
    def show(self):
        if self.name is not None:
            print("Name of person is :",self.name)
        else:
            raise IndexError("No Name")
        if self.age is not None:
            print("Age of person is",self.age)
        else:
            raise IndexError("No Name")
class Circle:
    def __init__(self,redius=None):
        self.radius=radius
    def getArea(self,radius):
        return 3.14*radius**2
    def getCircumference(self,radius):
        return (3.14*radius**2)/2
class Rectangle:
    def __init__(self):
        self.length=0
        self.breadth=0
    def setDimensions(self,length,breadth):
        self.length=length
        self.breadth=breadth
    def showDimension(self):
        print(f"length:{self.length},breadth:{self.breadth}")
    def getArea(self):
        return self.length*self.breadth
class Book:
    def __init__(self,bookid=None,title=None,price=None):
        self.bookid=0
        self.title=title
        self.price=price  
    def show(self):
        print("book id is:",self.bookid)
        print("Book title is:",self.title)
        print("Book price is:",self.price)
class Team:
    def __init(self,name=None):
        self.name=name
        self.list=[]
    def input(self):
        while True:
            m_name=input("Enter a team member's name (or 'done' to finish)")
            if m_name.lower()=="done":
                break
            self.list.append(m_name)
    def display(self):
        print("Team Member are:")
        for member in self.list:
            print(member)
    
    
    
