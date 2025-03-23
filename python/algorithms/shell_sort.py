from isaac.my_utils import time_it
#array = [35,33,42,10,14,19,27,44]

@time_it
def shell_sort(array):
	#initialize interval, using shell original sequence
	interval = len(array) // 2

	while interval > 0:
		for i in range(interval, len(array)):
			temp = array[i]
			j = i 
			while j >= interval and array[j-interval] > temp:
				array[j] = array[j-interval]
				j -= interval
			array[j] = temp
		interval //=2
	return array
#print(shell_sort(array))
