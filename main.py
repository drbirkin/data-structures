# https://stackabuse.com/courses/graphs-in-python-theory-and-implementation/lessons/representing-graphs-in-code/

class Graph_List_Edges:
    # Constructor
    def __init__(self, num_of_nodes, directed=True):
        self.m_num_of_nodes = num_of_nodes
        self.m_directed = directed
        
        # Different representations of a graph
        self.m_list_of_edges = []
	
    # Add edge to a graph
    def add_edge(self, node1, node2, weight=1):        
        # Add the edge from node1 to node2
        self.m_list_of_edges.append([node1, node2, weight])
        
        # If a graph is undirected, add the same edge,
        # but also in the opposite direction
        if not self.m_directed:
            self.m_list_of_edges.append([node2, node1, weight])

	# Print a graph representation
    def print_edge_list(self):
        num_of_edges = len(self.m_list_of_edges)
        for i in range(num_of_edges):
            print("edge ", i+1, ": ", self.m_list_of_edges[i])
            
class Graph_Matrix:
    def __init__(self, num_of_nodes, directed=True):
        self.m_num_of_nodes = num_of_nodes
        self.m_directed = directed

        # Initialize the adjacency matrix
        # Create a matrix with `num_of_nodes` rows and columns
        self.m_adj_matrix = [[0 for column in range(num_of_nodes)] 
                            for row in range(num_of_nodes)]

    def add_edge(self, node1, node2, weight=1):
        self.m_adj_matrix[node1][node2] = weight

        if not self.m_directed:
            self.m_adj_matrix[node2][node1] = weight

    def print_adj_matrix(self):
        print(self.m_adj_matrix)
        
class Graph_List:
    def __init__(self, num_of_nodes, directed=True):
        self.m_num_of_nodes = num_of_nodes
        self.m_nodes = range(self.m_num_of_nodes)

        # Define the type of a graph
        self.m_directed = directed

        self.m_adj_list = {node: set() for node in self.m_nodes}      

    def add_edge(self, node1, node2, weight=1):
        self.m_adj_list[node1].add((node2, weight))
        
        if not self.m_directed:
        	self.m_adj_list[node2].add((node1, weight))
    
    def print_adj_list(self):
        for key in self.m_adj_list.keys():
            print("node", key, ": ", self.m_adj_list[key])
            
graph = Graph_List_Edges(5)

graph.add_edge(0, 0, 25)
graph.add_edge(0, 1, 5)
graph.add_edge(0, 2, 3)
graph.add_edge(1, 3, 1)
graph.add_edge(1, 4, 15)
graph.add_edge(4, 2, 7)
graph.add_edge(4, 3, 11)

graph.print_edge_list()

graph = Graph_Matrix(5)

graph.add_edge(0, 0, 25)
graph.add_edge(0, 1, 5)
graph.add_edge(0, 2, 3)
graph.add_edge(1, 3, 1)
graph.add_edge(1, 4, 15)
graph.add_edge(4, 2, 7)
graph.add_edge(4, 3, 11)

graph.print_adj_matrix()

graph = Graph_List(5)

graph.add_edge(0, 0, 25)
graph.add_edge(0, 1, 5)
graph.add_edge(0, 2, 3)
graph.add_edge(1, 3, 1)
graph.add_edge(1, 4, 15)
graph.add_edge(4, 2, 7)
graph.add_edge(4, 3, 11)

graph.print_adj_list()