#interpolatin search 
#O(log(log)n) -> faster than binary search
#uses only sorted & uniform data sets
import sys
from isaac.my_utils import time_it
from binary_search import binarySearch, recursion_binarySearch
from nums_list import long_list
from linear_search import linearSearch, recursion_linearSearch



list_ = [1,2,3,4,5,6,7,8,9,10,11,12,13]
#list_ = []
search_term = 698383


linearSearch(long_list, search_term)
#recursion_linearSearch(long_list, search_term, len(long_list)-1) #useful when search from back of list only!
binarySearch(long_list, search_term)
recursion_binarySearch(long_list,search_term,list_.index(list_[0]),len(list_)-1)


@time_it
def interpolation_search(list_, search_term): #using while
	if len(list_) == 0:
		sys.exit('Empty List')

	Lo = 0
	Mid = -1
	Hi = list_.index(list_[-1])

	while Mid != search_term:
		if Lo == Hi or list_[Lo] == list_[Hi]:
			sys.exit('NULL LIST')

		#set MId
		Mid = Lo + ((Hi - Lo) // (list_[Hi] - list_[Lo]) * (search_term - list_[Lo]))
		if list_[Mid] == search_term:
			return Mid
		else:
			if list_[Mid] < search_term:
				Lo = Mid + 1
			elif list_[Mid] > search_term:
				Hi = Mid -1 
interpolation_search(long_list, search_term)
#print(f'Index: {index}-> Element: {long_list[index]}')

# Python3 program to implement
# interpolation search
# with recursion

# If x is present in arr[0..n-1], then
# returns index of it, else returns -1.


# interpolation search with recursion

@time_it
def interpolation_search_recursion(arr, lo, hi, search_term): #if else loop

	if lo <= hi and search_term >= arr[lo] and search_term <= arr[hi]:
		Mid = lo + ((hi - lo) // (arr[hi] - arr[lo]) * (search_term - arr[lo]))

		if arr[Mid] == search_term:
			return Mid
		if arr[Mid] < x:
			return interpolationSearch(arr, Mid+1, hi, search_term)
		if arr[Mid] > x:
			return interpolationSearch(arr, lo, Mid-1, search_term)
	return -1
interpolation_search_recursion(long_list, 0, long_list.index(long_list[-1]),search_term)



				

