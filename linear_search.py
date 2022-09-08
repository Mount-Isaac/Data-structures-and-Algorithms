#linear search algorithm
#iterates the list from index 0 until the search 
#variable is found else exits as False
#Tn -> O(v), the worst case scenario of Big O 
#in linear search algorith is linear time 
from nums_list import long_list
from isaac.my_utils import time_it
import sys
#print(len(long_list))

list_ = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,21,22,23]
'''
#for loop
print('[+]Iterative Linear Search using FOR LOOP')
@my_utils.time_it
def linear_search(list_, var):
	for element in range(len(list_)):
		if list_[element] == var:
			return element
	return False


result = linear_search(long_list, 999999)
if result is False:
	print('Element not found')
else:
	print(f'Element at index: {result}')
'''



#if else loop
#print('\n[+]Iterative Linear Search using IF-ELSE LOOP')
@time_it
def linearSearch(list_, var): #ifElse_linearSearch
	if var not in list_:
		return False
	else:
		return list_.index(var)

#print('Element at index: ',ifElse_linearSearch(long_list, 999999))

#using recursion
#Drawback: maximum recursion depth in Python is 1000
#therefore the program is unsuitable where len(array) > 1000
#Slowest algorithm when it comes to huge datasets
#suitable for sorted datasets when searching in descending order
sys.setrecursionlimit(1000002)
@time_it
def recursion_linearSearch(array, key, size):
	if size == 0:
		return -1
	elif size == 1 and array[0] != key:
		return -1
	elif array[size] == key:
		return size
	else:
		return recursion_linearSearch(array, key, size-1)

#print(recursion_linearSearch(long_list, 500000, len(long_list)-1)) #consumes lots of time
