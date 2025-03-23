def dfs(graph, start, visited=None):
	if visited is None:
		visited = set()
	visited.add(start)
	print('visited', start)

	#for next in graph[0]
	for next in graph[start] - visited: #ensure iteration starts at index 0
		dfs(graph, next, visited)
	return visited

graph = {
		  '0': set(['1', '2']),
		  '1': set(['0', '3', '4']),
		  '2': set(['0']),
		  '3': set(['1']),
		  '4': set(['2', '3'])
		}
#print(type(graph))
print(dfs(graph, '0'))
v = set('0')
for i in graph['0'] - v:
	#print(i)
	pass