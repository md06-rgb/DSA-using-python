class Graph:
    def __init__(self,vno):
        self.vertex_count=vno
        self.adjmatrix=[ [0]*vno for e in range(vno)]
    def add_edge(self,u,v,weight=1):
        if 0<= u < self.vertex_count and 0<=v<self.vertex_count:
            self.adjmatrix[u][v]=weight
            self.adjmatrix[v][u]=weight
        else:
            print("Invalid vertex")
    def remove_edge(self,u,v):
        if 0<=u<self.vertex_count and 0<=v<self.vertex_count:
            self.adjmatrix[u][v]=0
            self.adjmatrix[v][u]=0
        else:
            print("Invalid vertex")
    def has_edge(self,u,v):
        if 0<=u<self.vertex_count and 0<=v<self.vertex_count:
            return self.adjmatrix[u][v] !=0
        else:
            print("Invalid vertex")
    def print_adj_matrix(self):
        for rowlist in self.adjmatrix:
            print(" ".join(map(str,rowlist)))
g=Graph(5)
g.add_edge(0,1)
g.add_edge(1,2)
g.add_edge(1,3)
g.add_edge(2,3)
g.add_edge(3,4)

g.print_adj_matrix()