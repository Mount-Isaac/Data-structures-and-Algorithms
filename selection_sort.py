from isaac.my_utils import time_it

list_ = [14,23,27,10,35,19,42,44]

@time_it
def selection_sort(list_):
	for index in range(len(list_)): # O(n)
		Min = index

		for j in range(index+1, len(list_)): #O(n)
			if list_[j] < list_[Min]:
				Min = j
		list_[index], list_[Min] = list_[Min], list_[index]
	return list_ # Tn = n.n == O(n²)

#print(selection_sort(list_))