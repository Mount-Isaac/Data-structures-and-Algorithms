class Node:
	def __init__(self, data=None, next=None):
		self.data = data
		self.next = next

class LinkedList:
	def __init__(self):
		self.head = None

	def insert_at_end(self, data):
		if self.head is  None:
			self.head = Node(data, None)
			return
		itr = self.head
		while itr.next:
			itr = itr.next
		itr.next = Node(data, None)

	def insert_value(self, data_list):
		self.head = None
		for data in data_list:
			self.insert_at_end(data)

	
	def getPossibleValue(self,num):
		if self.head is None:
			return

			#if head data == num
		if self.head.data ==num:
			num *=2
			itr = self.head
			while itr:
				if itr.data == num:
					num *=2
				itr = itr.next
			return num

			#if head data != num then iterate over the entire Linkedlist
		itr = self.head
		while itr.next:
			if itr.next.data == num:
				num *=2
			itr = itr.next
		return num




llst = LinkedList()

llst.insert_value([2,5,4,6,8])
possible_value = llst.getPossibleValue(2)
print(possible_value)