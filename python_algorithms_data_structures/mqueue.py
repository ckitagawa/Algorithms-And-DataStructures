class Node:
	def __init__(self, value):
		self.value = value
		self.next_in_queue = None

class Queue:
	def __init__(self):
		self.head = None
		self.tail = None

	def enqueue(self, value):
		if self.head == None:
			self.head = Node(value)
		elif self.tail == None:
			self.head.next_in_queue = Node(value)
			self.tail = self.head.next_in_queue
		else:
			self.tail.next_in_queue = Node(value)
			self.tail = self.tail.next_in_queue

	def dequeue(self):
		if self.head == None:
			return None
		value = self.head.value
		self.head = self.head.next_in_queue
		if self.head == None:
			self.tail = None
		return value

if __name__ == "__main__":
	queue = Queue()
	for i in range(0, 10):
		queue.enqueue(i)
		if i == 7:
			print(queue.dequeue())

	for i in range(0, 10):
		print(queue.dequeue())