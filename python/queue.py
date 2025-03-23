from collections import deque
import time
import sys
from termcolor import colored
import threading

q = deque()

#FIFO principle
q.appendleft(77)
q.appendleft(34)
q.appendleft(23)
#before popping out the last elemnet, first element to get inserted
#print(q)
#q.pop()
#print(q)

#OOP to implement deque
class Queue:
	def __init__(self):
		self.buffer = deque()

	def enqueue(self,val):
		self.buffer.appendleft(val)

	def dequeue(self):
		if len(self.buffer) == 0:
			sys.exit()
			return

		return self.buffer.pop()

	def IsEmpty(self):
		return len(self.buffer) == 0

	def size(self):
		return len(self.buffer)

	def printQueue(self):
		return self.buffer

	def peek(self):
		return self.buffer[-1]

	def clear(self):
		return self.buffer.clear()

	def search(self,val):
	    itr = self.buffer
	    for i in range(len(itr)):
	      if itr[i] == val:
	        return True
	        break
	      elif i+1 == len(itr):
	        return False

q = Queue()
q.enqueue(8)
q.enqueue(63)
q.enqueue(17)
q.enqueue(25)

'''
print('Queue: ', q.printQueue())
print('Size: ' ,q.size())
print('Empty: ', q.IsEmpty())
print('Peek: ', q.peek())
print('Search: ', q.search(63))
print('Search: ', q.search(74))

'''
''' Design a food ordering system where your python program will run two threads,

Place Order: This thread will be placing an order and inserting that into a queue. This thread places new order every 0.5 second. (hint: 
use time.sleep(0.5) function)
Serve Order: This thread will server the order. All you need to do is pop the order out of the queue and print it. This thread serves an 
order every 2 seconds. Also start this thread 1 second after place order thread is started.
Use this video to get yourself familiar with multithreading in python

Pass following list as an argument to place order thread,

orders = ['pizza','samosa','pasta','biryani','burger']
This problem is a producer,consumer problem where place_order thread is producing orders whereas server_order thread is consuming
 the food orders. Use Queue class implemented in a video tutorial. '''

#Food order implementation 1
orders = ['pizza', 'samosa', 'pasta', 'biryani', 'burger']
def placeOrder():
	order = Queue()
	for item in orders:
		order.enqueue(item)
		#time.sleep(0.5)
	return order.printQueue()
def serveOrder(placeOrder):
	order = Queue() 
	order.enqueue(placeOrder)
	Order_list = order.printQueue()
	for order_items in Order_list:
		for items in order_items:
			print('Order item: {} {}:)'.format(items, '\U0001F929'))
			time.sleep(3) 

#serveOrder(placeOrder())


#Food implementation 2

food_processing_queue = Queue()
def place_orders(orders):
	for order in orders:
		print(f'Placing order for: {order}')
		food_processing_queue.enqueue(order)
		time.sleep(2)

def server_orders():
	time.sleep(1)
	while True:
		order = food_processing_queue.dequeue()
		print(f'Now serving: {order}\n')
		time.sleep(2)

orders = ['pizza','samosa','pasta','biryani','burger']
t1 = threading.Thread(target=place_orders, args=(orders,))
t2 = threading.Thread(target=server_orders)


t1.start()
t2.start()













