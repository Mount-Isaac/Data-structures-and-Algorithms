from isaac.my_utils import time_it
from nums_list import string_
#list_ = [14,33,27,10,35,19,6,42,44]
list_ = [88,18,-3,-11,4,-2]

@time_it
def insertion_sort(list_):
	for i in range(1,len(list_)): #traverse thro' index 1 to last element
		key = list_[i]
		j = i-1
		while j >=0 and key < list_[j]:
			list_[j+1] = list_[j]
			j -= 1
		list_[j+1] = key
	return list_

#print(insertion_sort(list(string_)))