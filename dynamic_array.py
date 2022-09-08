class DynamicArray(object):
	def __init__(self):
		#actual number of elements in dynamic array
		self.size = 0
		#max capacity of the dynamic array
		self.capacity = 1
		self.array = self.createArray(self.capacity)

	def len(self):
		#determine lenght of the array
		return self.size

	def getItem(self, index):
		if not 0 <= index < self.size:
			raise IndexErro('Given index {0} is larger than arrya size {1}'.format(index, self.size))
		element = self.array[index]
		size = self.size
		for i in range(1, self.size+3):
			print(f'Element {index + 1} index {[index]} -> {element}')
			break			

	def createArray(self, length):
		#create array with given size
		return [None] * length

	def resize(self, new_capacity):
		#resize the array to the new capacity
		new_array = self.createArray(new_capacity)
		#resize the elements in the old array to the new array
		for i in range(self.size):
			new_array[i] = self.array[i]

		self.array = new_array
		self.capacity = new_capacity

	def appendElements(self, element):
		#add new element to the end of the array
		if self.size == self.capacity:
			self.resize(2*self.capacity)

		self.array[self.size] = element
		self.size +=1

	def popElement(self):
		#pop the last element from the end of the array
		element = None
		if self.size > 0:
			element = self.array[self.size - 1]
			self.array[self.size -1 ] = None
			self.size -=1



dynamic1 = DynamicArray()
dynamic1.createArray(5)
dynamic1.appendElements(5)
dynamic1.appendElements(12)
dynamic1.appendElements(7)
dynamic1.appendElements(23)
dynamic1.getItem(0)
dynamic1.getItem(1)
dynamic1.getItem(2)
dynamic1.getItem(3)
