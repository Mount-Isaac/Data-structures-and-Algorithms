class Node:
	def __init__(self, data=None, next=None):
		self.data = data
		self.next = next

class LinkedList:
	def __init__(self):
		self.head = None


	def insert_beginning(self, data):
		node = Node(data, self.head)
		self.head = node

	def print(self):
		if self.head is None:
			print(f'Empty LinkedList ')
			return
		itr = self.head
		llstr = ''
		while itr:
			llstr += str(itr.data) + '--> '
			itr = itr.next
		print(llstr)

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

	def get_length(self):
		count = 0
		itr = self.head
		while itr:
			count +=1
			itr = itr.next
		return count

	def remove_at(self,index):
		if index < 0 or index >= self.get_length():
			raise Exception("Invalid index")
			return
		if index == 0:
			self.head = self.head.next
			return
		count = 0
		itr = self.head
		while itr:
			if count == index -1:
				itr.next = itr.next.next
				break
			itr = itr.next
			count +=1

	def insert_at(self, index, data):
		if index < 0 or index > self.get_length():
			raise Exception('Invalid index')
			return
		if index == 0:
			node = Node(data, self.head)
			self.head = node
			return
		itr = self.head
		count = 0
		while itr:
			if count == index-1:
				node = Node(data,itr.next)
				itr.next = node
				break
			itr = itr.next
			count +=1

	def insert_after_value(self, data_after, data_to_insert):
		if self.head is None: 
			return

		if self.head.data == data_after:
			self.head.next = data_to_insert
			return
			
		itr = self.head
		while itr:
			if itr.data == data_after:
				node = Node(data_to_insert, itr.next)
				itr.next = node
				break
			itr = itr.next

	def remove_by_value(self, data):
		if self.head is None:
			return
		if self.head.data == data:
			self.head = self.head.next
			return
		itr = self.head
		while itr.next:
			if itr.next.data == data:
				itr.next = itr.next.next
				break
			itr = itr.next
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
'''
llst.insert_beginning(32)
llst.insert_at_end(88)
llst.print()

llst.insert_value(['Banana', 'Oranges', 'Tomatoes', 'Onions'])
llst.print()
print(f'Length: {llst.get_length()}')
llst.remove_at(32)
llst.print()
print(f'Length: {llst.get_length()}')
'''
llst.insert_value([2,5,4,6,8])
#llst.insert_after_value('Oranges', 'Lettuce')
llst.print()
possible_value = llst.getPossibleValue(2)
print(possible_value)
#llst.remove_by_value('Tomatoes')
#llst.print()