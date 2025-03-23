from isaac.my_utils import time_it
list_ = [14,33,27,35,10]

def swap(elem1, elem2):
	list_[elem1],list_[elem2] = list_[elem2],list_[elem1]

@time_it
def bubble_sort(list_):
	for loop in range(len(list_)-1):
		swapped = False
		for index in range(len(list_)-1):
			if list_[index] > list_[index+1]:
				list_[index],list_[index+1] = list_[index+1],list_[index]
				#swap(index, index+1)
				swapped = True
	return list_

print(bubble_sort(list_))


#reverse sorting
@time_it
def bubbleSort_reverse(list_):
	for element in range(len(list_)-1,0,-1):
		swapped = False
		for index in range(element):
			if list_[index] > list_[index+1]:
				list_[index], list_[index+1] = list_[index+1], list_[index]
				swapped = True
		if not swapped:
			return list_
print(bubbleSort_reverse(list_))