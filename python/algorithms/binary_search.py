from nums_list import long_list
from isaac.my_utils import time_it

list_ = [23,5,89,7,23,11, 87,34,66,90]

#For integers only
@time_it
def binarySearch(list_, number_to_find):
	#Binary search is only effective on a sorted list only
	list_.sort() 
	left_index = 0
	#right_index = len(list_) -1 
	right_index = list_.index(list_[-1])

	while left_index <= right_index:
		mid_index = (left_index + right_index) // 2
		mid_number = list_[mid_index]

		if mid_number == number_to_find:
			return mid_index
		if mid_number < number_to_find:
			left_index = mid_index + 1
		else:
			right_index = mid_index -1 
	return -1
#print(f'Element at index: {binarySearch(long_list, 999999)}')


#For strings
def binarySearch_string(array, string):
	pass


#using recursion
@time_it
def recursion_binarySearch(list_, number_to_find, left_index, right_index):
	list_.sort()
	if right_index <= left_index:
		return -1

	if list_[0] == number_to_find:
		return 0
	if list_[-1] == number_to_find:
		return list_.index(list_[-1])

	mid_index = (left_index + right_index) //2
	if mid_index >= len(list_):
		return -1
	mid_number = list_[mid_index]

	if mid_number == number_to_find:
		return mid_index
	if mid_number < number_to_find:
		left_index = mid_index + 1
	else:
		right_index = left_index -1

	return recursion_binarySearch(list_, number_to_find, left_index, right_index)
#index = recursion_binarySearch(long_list,999999,list_.index(list_[0]),len(list_)-1)
#print(f'Elment at index: {index}')



#duplicate_list = [1,4,6,9,11,15,15,15,17,21,34,34,56]
duplicate_list = [2,5,7,8,13,21,21,21]
def occurrences_binarySearch(list_,number_to_find):
	pass
	
@time_it
def not_search_rotated_sorted_array(list_, number_to_find):
	try:
		return list_.index(number_to_find)
	except ValueError:
		return -1

	'''
	the above algorithm uses inbuilt index method who Tn = O(n) because at 
	the worst case scenario where the target is not found, the method has 
	to iterate the entire list to prove it's absence
	Therefore, this does not at all implement the use of BS whose Tn = log(n)
	'''