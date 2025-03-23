import numpy as np
grid = np.random.randint(0, 9, size=(4, 4))


class Dijkstra:
	#initializing game mode by required args
	def __init__(self, grid, height, width, path, cost):
		self.grid = grid
		self.posx = 0
		self.posy = 0
		self.height = height
		self.width = width
		self.path = path
		self.cost = cost

	def minPathSum(self):
		grid = self.grid
		min_queue = []

		row = [None] * width
		visited = [row[:] for i in range(height)]
		goal = (height-1, width-1)
		top_left = (grid[0][0], (0,0))
		heapq.heappush(min_queue, top_left)
		cur_path_cost = self.grid[0][0]
		while min_queue:
			(cur_path_cost, coordinates) = heapq.heappop(min_queue)
			(cur_height, cur_width) = coordinates
			#cell already visited
			if visited[cur_height][cur_width]:
				continue
			else:
				visited[cur_height][cur_width] = True

			if coordinates == goal