import sys
import numpy as np
#vertices = 3
#[[None for column in range(vertices)] for row in range(vertices)]


class Graph:
    def __init__(self,vertices):
        self.V = vertices
        self.graph = [[0 for column in range(vertices)] for row in range(vertices)]

    def printSolution(self, dist):
        print('Vertex \tDistance from source')
        for node in range(self.V):
            print(node, '\t', dist[node])

    def minDistance(self, dist, sptSet):
        min_ = sys.maxsize

        for u in range(self.V):
            if dist[u] < min_ and sptSet[u] == False:
                min_ = dist[u]
                min_index = u
        return min_index


    def dijkstra(self,src):
        dist = [sys.maxsize] * self.V
        dist[src] = 0
        sptSet = [False] * self.V

        for count in range(self.V):
            x = self.minDistance(dist,sptSet)
            sptSet[x] = True

            for y in range(self.V):
                if self.graph[x][y] > 0 and sptSet[y] == False and dist[y] > dist[x] + self.graph[x][y]:
                    dist[y] = dist[x] + self.graph[x][y]
        self.printSolution(dist)


try:
    g = Graph(9)
    '''
    g.graph =[[0,4,0,0,0,0,8,0],
        [4,0,8,0,0,0,11,0],
        [0,4,0,0,0,0,8,0],
        [4,0,8,0,0,0,11,0],
        [0,4,0,0,0,0,8,0],
        [4,0,8,0,0,0,11,0],
        [0,4,0,0,0,0,8,0],
        [4,0,8,0,0,0,11,0]];
    '''
    g.dijkstra(0)
except Exception as e:
    sys.exit(e)

