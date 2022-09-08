'''
Bellford's Algorithm for finding the shortest
path from a vertex to all other vertices of a
weighted graph
'''

class Graph:
	def __init__(self, vertices):
		self.V = vertices #total no. of vertices
		self.graph = []

	#add edges 
	def addEdge(self, s,d,w):
		self.graph.append([s,d,w])

	#print solution
	def print_solution(self, dist):
		print('Vertex Distance from the source')
		for i in range(self.V):
			print(f'{i}\t\t{dist[i]}')

	def bellmanFord(self,src):
		#1-> Fill the distance array & predecessor array
		dist = [float('Inf')] * self.V 
		#mark the source vertex 
		dist[src] = 0
		#2-> relax edges |V| - 1 times
		for _ in range(self.V-1):
			for s,d,w in self.graph:
				if dist[s] != float('Inf') and dist[s] + w < dist[d]:
					dist[d] = dist[s] + w
		#3-> detect negative cycle
		for s,d,w in self.graph:
			if dist[s] != float('Inf') and dist[s] + w < dist[d]:
				print('Graph contains negative cycles')
				return
		self.print_solution(dist)

g = Graph(5)
g.addEdge(0, 1, 5)
g.addEdge(0, 2, 4)
g.addEdge(1, 3, 3)
g.addEdge(2, 1, 6)
g.addEdge(3, 2, 2)

g.bellmanFord(0)