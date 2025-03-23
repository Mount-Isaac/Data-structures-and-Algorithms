#MAX-HEAP 
'''
A Max-heap is a complete binary tree in which the value in each intenal node is greater than or equal to teh values in
children of that node
'''
import sys

class maxHeap:
	def __init__(self,max_size):
		self.max_size = max_size
		self.size = 0
		self.Heap = [0] * (self.max_size + 1)
		self.Heap[0] = sys.maxsize
		self.FRONT = 1


	#function to return the postion of parent
	def parent(self,post):
		return post // 2

	# return the position of the left child for the node 
	def leftChild(self,post):
		return 2*post

	#return the position of the right child
	def rightChild(self,post):
		return (2*post) + 1

	#return bool if passed node is a leaf node
	def isLeaf(self,post):
		return post >= (self.size//2) and post <= self.size

	#swap two nodes of the heap
	def swap(self, fpos, spos):
		self.Heap[fpos], self.Heap[spos] = self.Heap[spos], self.Heap[fpos]

	#heapify the node at pos
	def maxHeapify(self,post):
		#if node is non-leaf & smaller than its child
		if not self.isLeaf(post):
			if self.Heap[post] < self.Heap[self.leftChild(post)] or self.Heap[post] < self.Heap[self.rightChild(post)]:
				#swap with the left child & heapify the left child
				if self.Heap[self.leftChild(post)] > self.Heap[self.rightChild(post)]:
					self.swap(post, self.leftChild(post))
					self.maxHeapify(self.leftChild(post))
				else:
					self.swap(post, self.rightChild(post))
					self.maxHeapify(self.rightChild(post ))


	#insert a node in the heap
	def insert(self,element):
		if self.size >= self.max_size:
			return
		self.size +=1
		self.Heap[self.size] = element

		current = self.size

		while self.Heap[current] > self.Heap[self.parent(current)]:
			self.swap(current, self.parent(current))
			current = self.parent(current)

	#print the contents of the heap
	def printHeap(self):
		for i in range(1,(self.size //2 ) + 1):
			print('Parent =>' + str(self.Heap[i]) + ' Left child ->' + str(self.Heap[2*i]) + ' Right child ->' + str(self.Heap[2*i+1]))

	#remove and return the maximm element from the heap
	def extractMax(self):
		popped = self.Heap[self.FRONT]
		self.Heap[self.FRONT] = self.Heap[self.size]
		self.size -=1
		self.maxHeapify(self.FRONT)
		return popped

	def heapElement(self,post):
		return self.Heap[post]


if __name__ =='__main__':
	print('******** maxHeap is ********')
	max_Heap = maxHeap(15)
	max_Heap.insert(5)
	max_Heap.insert(3)
	max_Heap.insert(17)
	max_Heap.insert(10)
	max_Heap.insert(84)
	max_Heap.insert(19)
	max_Heap.insert(6)
	max_Heap.insert(22)
	max_Heap.insert(9)
	#max_Heap.maxHeapify(7)
	print(f'{max_Heap.heapElement(4)} Leaf? {max_Heap.isLeaf(4)}')	
	print('Max: ', str(max_Heap.extractMax()))
	print('')
	max_Heap.printHeap()
