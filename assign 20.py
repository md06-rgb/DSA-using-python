class Node:
    def __init__(self,left=None,item=None,right=None):
        self.left=left
        self.item=item
        self.right=right
class BST:
    def __init__(self,root=None):
        self.root=root
        self.size=0
    def insert(self,data):
        self.root=self.rinsert(self.root,data)
        self.size+=1
    def rinsert(self,root,data):
        if root is None:
            return Node(None,data,None)
        elif data < root.item:
            root.left=self.rinsert(root.left,data)
        elif data > root.item:
            root.right=self.rinsert(root.right,data)
        return root
    def search(self,data):
        return self.rsearch(self.root,data)
    def rsearch(self,root,data):
        if root is None or root.item==data:
            return root.item
        elif data<root.item:
            return self.rsearch(root.left,data)
        else:
            return self.rsearch(root.right,data)
    def inorder(self):
        result=[]
        self.rinorder(self.root,result)
        return result
    def rinorder(self,root,result):
        if root:
            self.rinorder(root.left,result)
            result.append(root.item)
            self.rinorder(root.right,result)
    def preorder(self):
        result=[]
        self.rpreorder(self.root,result)
        return result
    def rpreorder(self,root,result):
        if root:
            result.append(root.item)
            self.rpreorder(root.left,result)
            self.rpreorder(root.right,result)
    def postorder(self):
        result=[]
        self.rpostorder(self.root,result)
        return result
    def rpostorder(self,root,result):
        if root:
            self.rpostorder(root.left,result)
            self.rpostorder(root.right,result)
            result.append(root.item)
b=BST()
b.insert(50)
b.insert(65)
b.insert(20)
b.insert(30)
b.insert(40)
b.insert(10)
b.insert(60)
b.insert(70)
print()
print("searching 70 is:",b.search(70))
print()
print("Print list in inorder(mean: L,Rt,R):")
print(b.inorder())
print()
print("Print list in preorder(mean: Rt,L,R):")
print(b.preorder())
print()
print("Print list in postorder(mean: L,R,Rt)")
print(b.postorder())