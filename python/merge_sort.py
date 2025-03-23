from isaac.my_utils import time_it
list_ = [14,23,27,10,35,19,-6,42,44]

@time_it
def merger_sort(array):
	if len(array) > 1:
		mid = len(array) // 2
		#divide the array into two parts
		left_sublist = array[:mid]
		right_sublist = array[mid:]
		#print(f'array: {array}\nleft: {left_sublist}\nright: {right_sublist}\n')

		#recurse to further divide the array until atomic values are obtained
		merger_sort(left_sublist)
		merger_sort(right_sublist)

		i=j=k=0
		#copy data to temporary array l[], r[]
		while i < len(left_sublist) and j < len(right_sublist):
			if left_sublist[i] < right_sublist[j]:
				array[k] = left_sublist[i]
				#print(array)
				i +=1
			else:
				array[k] = right_sublist[j]
				j +=1
				#print(array)
			k +=1

		#check if any element was left
		while i < len(left_sublist):
			array[k] = left_sublist[i]
			i += 1
			k += 1
			#print(array)

		while j < len(right_sublist):
			array[k] = right_sublist[j]
			j += 1
			k += 1
			#print(array)
	return (f'Merge sorted array--> {array}')
#print(f'Array--> {list_}')
#print(merger_sort(list_))

#variant code of the above merge sort


def merge_sorted_array(left_arrary, right_array, array):
	i=j=k=0 #(left,right,merged) arrays indexes respectively

	while i < len(left_arrary) and j < len(right_array):
		if left_arrary[i] <= right_array[j]:
			array[k] = left_arrary[i]
			i += 1
		else:
			array[k] = right_array[j]
			j += 1
		k += 1
	#check for omitted elements
	while i < len(left_arrary):
		array[k] = left_arrary[i]
		i += 1
		k += 1
	while j < len(right_array):
		array[k] = right_array[j]
		j += 1
		k += 1
	#returning sorted array
	return array

def merge_sort_two(array):
	if len(array) <= 1:
		return

	mid = (len(array) // 2)
	left_arrary = array[:mid]
	right_array = array[mid:]

	merge_sort_two(left_arrary)
	merge_sort_two(right_array)

	#returning sorted array
	return merge_sorted_array(left_arrary, right_array, array)

array = [14,23,27,10,35,19,-6,42,44]
#print(merge_sort_two(array))