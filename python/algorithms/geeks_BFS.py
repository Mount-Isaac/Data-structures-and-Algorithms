from collections import defaultdict


class Graph:
	def __init__(self):
		self.graph = defaultdict(list)

	#adding an edge
	def addEdge(self, u, v):
		self.graph[u].append(v)

	#print the BFS graph
	def BFS(self, s):
		#mark all vertices as !visited
		visited = [False] * (max(self.graph) + 1)
		queue = [] #create a queue
		queue.append(s)
		visited[s] = True

		#iterate while len(queue) =! 0
		while queue:
			#dequeue a vertex 
			s = queue.pop(0)
			print(s, end=' ')

			'''
			get all adjacent vertices of
			dequeued vertex s, if adjacent
			!visited, mark, visit & enqueue
			'''
			for i in self.graph[s]:
				if visited[i] == False:
					queue.append(i)
					visited[i] = True


#instantiate a class object 
g = Graph()
g.addEdge(0,1)
g.addEdge(0,2)
g.addEdge(1,2)
g.addEdge(2,0)
g.addEdge(2,3)
g.addEdge(3,3)

print('[+] BFS traversal from vertex 2')
print(f'{g.graph[0:]}')
g.BFS(2)