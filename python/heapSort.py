
unsorted_list = [5,16,8,14,20,1,26]

#heapify the list
def heapify(array):
	try:
		n = len(array)
		i = array.index(array[-1])
		#print(i)
		leftC = 2*i+1
		rightC = 2*i+2
		return array[leftC],array[rightC]
	except Exception as e:
		print(e)

heapify(unsorted_list)

