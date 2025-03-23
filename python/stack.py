from collections import deque
#stack = deque()
'''
deque_methods = dir(stack)
for method in deque_methods:
	print(method)

stack.append('isak')
stack.append('mirry')
stack.append('sam')
stack.append('glor')
print(stack.pop())
print(stack)
'''
#Code below has used the deque class to create methods similar to those of inbuilt deque

class Stack:
	def __init__(self):
		self.container = deque()

	def push(self, element):
		self.container.append(element)

	def pop(self):
		return self.container.pop()

	def peek(self):
		return self.container[-1]

	def is_empty(self):
		return len(self.container) == 0

	def size(self):
		return len(self.container)

	def print_stack(self):
		return self.container

stack = Stack()
stack.push(89)
stack.push(34)
stack.push('Isak')
stack.push('Shark')
stack.pop()

'''
try:
	stack_elements = stack.print_stack()
	print(stack_elements)
	print(f'Empty?: {stack.is_empty()}')
	print(f'Size: {stack.size()}')
	print(f'peek element: {stack.peek()}')
except Exception as e:
	print('Exception: ', e, '\nCannot Peek empty list')
'''

#reverse a string 
def reverse_string(string):
	stack = Stack()
	for ch in string:
		stack.push(ch)

	rvstr = ''
	while stack.size() != 0:
		rvstr += stack.pop()
	return rvstr

#print(reverse_string('We will conquer Covid-19'))

def is_match(ch1,ch2):
	match_dict = {
	')' : '(',
	']' : '[',
	'}' : '{'
	}
	return match_dict[ch1] == ch2

def check_bracket(bracket):
	s = Stack()
	for ch in bracket:
		if ch == '(' or ch == '{' or ch == '[':
			s.push(ch)
		if ch == ')' or ch == '}' or ch ==']':
			if s.size() == 0:
				return False
			if not is_match(ch,stack.pop()):
				return False
	return stack.size() == 0

brack_valid = check_bracket("({a+b})")
print(brack_valid)
