import sys
with open('nums.txt', 'w+') as file:
	sys.stdout = file
	numbers = [x for x in range(1000000)]
	print(numbers)
file.close()