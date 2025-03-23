from nums_list import string_
new_string =[]
#string_ = ''
for i in range(len(string_)):
	if string_[i] == 'v':
		pass
	else:
		new_string.append(string_[i])

def partition(l, r, nums):
	#l = nums[0]
	#r = nums[-1]

	pivot, ptr = r, l
	for i in range(l, r):
		if nums[i] <= pivot:
			nums[i],nums[ptr] = nums[ptr], nums[i]
			ptr += 1
	nums[ptr], nums[r] = nums[r], nums[ptr]
	return ptr

def quick_sort(l, r , nums):

	if len(nums) == 1:
		return nums
	if l< r:
		pi = partition(l, r, nums)
		quick_sort(l, pi-1, nums)
		quick_sort(pi+1, r, nums)
	return nums
#nums =  [4, 5, 1, 2, 3]
print(quick_sort(0, len(new_string)-1, new_string))
