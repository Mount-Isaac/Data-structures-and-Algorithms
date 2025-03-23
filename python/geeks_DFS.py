'''
printing DFS traversal using 
a directed graph that implements 
the use of adjacency list representation
'''

#complete graph DFS algorithm
from collections import defaultdict

class Graph:
	def __init__(self):
		self.graph = defaultdict(list)

	#adding an edge to the graph
	def addEdge(self, u, v):
		self.graph[u].append(v)

	#DFS method
	def dfs_util(self, v, visited):
		#mark current node as visited
		visited.add(v)
		print(v, end=' ')

		for neighbor in self.graph[v]:
			if neighbor not in visited:
				self.dfs_util(neighbor, visited)

	def DFS(self):
		visited = set()

		for vertex in self.graph:
			if vertex not in visited:
				self.dfs_util(vertex, visited)

#create a graph
try:
    g = Graph()
    g.addEdge(0, 1)
    g.addEdge(0, 9)
    g.addEdge(1, 2)
    g.addEdge(2, 0)
    g.addEdge(2, 3)
    g.addEdge(9, 3)
    #print(type(g.graph))
    print('Depth First Search:')
    g.DFS()

except Exception as e:
	#print('\nException:',e)
	pass