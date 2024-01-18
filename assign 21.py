class Node:
    def __init__(self,left=None,item=None,right=None):
        self.left=left
        self.item=item
        self.right=right
class BST:
    def __init__(self,root=None):
        self.root=root
    def insert(self,data):
        self.root=self.rinsert(self.root,data)
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
    def minimum_value(self):
        min=self.rminimum(self.root)
        return min
    def rminimum(self,root):
        if root is None or root.left is None:
            return root.item
        else: 
            return self.rminimum(root.left)
        
    def maximum_value(self):
        max=self.rmaximum(self.root)
        return max
    def rmaximum(self,root):
        if root is None or root.right is None:
            return root.item
        else: 
            return self.rmaximum(root.right)
    def delete(self,data):
        self.rdelete(self.root,data)
    def rdelete(self,root,data):
        if root is None:
            return root
        elif data<root.item:
            root.left=self.rdelete(root.left,data)
        elif data> root.item:
            root.right=self.rdelete(root.right,data)
        else:
            if root.left is None:
                return root.right
            elif root.right is None:
                return root.left
            root.item=self.rminimum(root.right)
            root.right=self.rdelete(root.right, root.item)
        return root
            
        
    def size(self):
        return len(self.inorder())
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
print()
print(b.minimum_value())
print()
print(b.maximum_value())
print()
print("size of the BST: ",b.size())
print()
print("After deleter function call:")
b.delete(65)
print()
print("Print list in inorder(mean: L,Rt,R):")
print(b.inorder())
print()
print("size of the BST: ",b.size())
