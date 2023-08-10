class Graph:
    def __init__(self):
        self.adj_list = {}

    def print_graph(self):
        for vertex in self.adj_list.keys():
            print(vertex, ':', self.adj_list[vertex])

    def add_vertex(self, vertex):
        if vertex not in self.adj_list.keys():
            self.adj_list[vertex] = []
            return True
        return False

    def add_edge(self, edge1, edge2):
        if edge1 in self.adj_list.keys() and edge2 in self.adj_list.keys():
            self.adj_list[edge1].append(edge2)
            self.adj_list[edge2].append(edge1)
            return True
        return False

    def remove_edge(self, edge1, edge2):
        if edge1 in self.adj_list.keys() and edge2 in self.adj_list.keys():
            try:
                self.adj_list[edge1].remove(edge2)
                self.adj_list[edge2].remove(edge1)
            except ValueError:
                return True
        return False

    def remove_vertex(self, vertex):
        if vertex in self.adj_list.keys():
            for other_vertex in self.adj_list[vertex]:
                self.adj_list[other_vertex].remove(vertex)
            del self.adj_list[vertex]
            return True
        return False
    
my_graph = Graph()
my_graph.add_vertex('A')
my_graph.add_vertex('B')
my_graph.add_vertex('C')
my_graph.add_vertex('D')
my_graph.add_edge('A','B')
my_graph.add_edge('A','C')
my_graph.add_edge('A','D')
my_graph.add_edge('B','D')
my_graph.add_edge('C','D')
my_graph.remove_vertex('D')
my_graph.print_graph()