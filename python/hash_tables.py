#These are basically dictonaries in Python
list_ = [3,2,9,11,7]
list_len = len(list_)

def hash_key(key, list_len):
	return key % list_len

'''
newList = []
for i in range(list_len):
	newList.insert(hash_key(list_[i], list_len), list_[i])
	#print(f'Hash value for {list_[i]} is {hash_key(list_[i], list_len)}')
print(newList, ':new')
print(list_, ':odd')
'''

hashTable = [[],] * 10

def checkPrime(n):
	if n == 1 or n == 0:
		return 0

	for i in range(2, n//2):
		if n % i == 0:
			return 0
	return 1

def getPrime(n):
	if n % 2 == 0: 
		n += 1
	while not checkPrime(n):
		n +=2
	return n

def hashFunction(key):
	capacity = getPrime(10)
	return key % capacity

def insertData(key, data):
	index = hashFunction(key)
	hashTable[index] = [key, data]

def removeData(key):
	index = hashFunction(key)
	hashTable[index] = 0

insertData(1, 'Apple')
insertData(0, 'Acute bean')
insertData(5, ' ')
print(hashTable)