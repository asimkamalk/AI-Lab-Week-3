from collections import defaultdict

# Graph class using adjacency list representation
class Graph:
    # Constructor to initialize the graph
    def __init__(self):
        # Using defaultdict to store the graph, which will have a list as default value
        self.graph = defaultdict(list)

    # Function to add an edge to the graph (u -> v)
    def addEdge(self, u, v):
        # Appending the node v to the adjacency list of u
        self.graph[u].append(v)

    # Function to perform BFS traversal starting from vertex s
    def BFS(self, s):
        # Check if the starting vertex exists in the graph
        if s not in self.graph:
            print(f"Vertex {s} does not exist.")
            return

        # Initialize all vertices as not visited
        visited = [False] * (len(self.graph))
        # Queue for BFS
        queue = []

        # Mark the source node as visited and enqueue it
        queue.append(s)
        visited[s] = True

        while queue:
            # Dequeue a vertex from the queue
            s = queue.pop(0)
            # Print the dequeued vertex
            print(s, end=" ")

            # Get all adjacent vertices of the dequeued vertex s
            for i in self.graph[s]:
                # If an adjacent vertex has not been visited, mark it visited and enqueue it
                if not visited[i]:
                    queue.append(i)
                    visited[i] = True

    # Function to print the adjacency list of the graph
    def printAdjList(self):
        # Iterate over the vertices in the graph
        for vertex in self.graph:
            # Print the vertex and its adjacency list
            print(f"{vertex}: {self.graph[vertex]}")

    # Function to count the number of vertices in the graph
    def countVertices(self):
        # Return the number of keys in the graph dictionary
        return len(self.graph)

    # Function to count the number of edges in the graph
    def countEdges(self):
        # Sum the lengths of all adjacency lists in the graph
        return sum(len(edges) for edges in self.graph.values())

# Example usage of the Graph class
g = Graph()
# Adding edges to the graph
g.addEdge(0, 1)
g.addEdge(0, 2)
g.addEdge(1, 2)
g.addEdge(2, 0)
g.addEdge(2, 3)
g.addEdge(3, 3)

# Printing the adjacency list of the graph
print("Adjacency List:")
g.printAdjList()

# Printing the number of vertices and edges in the graph
print("\nNumber of vertices:", g.countVertices())
print("Number of edges:", g.countEdges())

# Performing BFS traversal starting from vertex 2
print("\nBFS Traversal starting from vertex 2:")
g.BFS(2)
