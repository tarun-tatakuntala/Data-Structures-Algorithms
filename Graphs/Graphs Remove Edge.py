class Graph:
    def __init__(self):
        self.adj_list = {}  #Initializing an empty dictionary

    def add_vertex(self, vertex):
        if vertex not in self.adj_list.key():
            self.adj_list[vertex] = []
            return True
        return False
    
    def add_edge(self, v1, v2):
        if v1 in self.adj_list.key() and v2 in self.adj_list.key(): #make sure whether edges are present or not
            self.adj_list[v1].append[v2]
            self.adj_list[v2].append[v1]
            return True                                             #executes after dict consists of vertices
        return False                                                #executes if vertex are not present
    
    def remove_edge(self, v1, v2):
        if v1 in self.adj_list.key() and v2 in self.adj_list.key():
            self.adj_list[v1].remove[v2]
            self.adj_list[v2].remove[v1]
            return True
        return False
        