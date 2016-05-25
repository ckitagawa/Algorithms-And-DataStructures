class Block:
	def __init__(self, value, next_block):
		self.value = value
		self.next = next_block

	# def block_recurse(self, curr):
	# 	if curr.next == None:
	# 		return 1
	# 	return curr.block_recurse(curr.next) + 1

class Stack:
	def __init__(self):
		self.list = None
		self.size = 0

	def push(self, data):
		self.list = Block(data, self.list)
		self.size += 1

	def pop(self):
		data = self.list.value
		self.list = self.list.next
		self.size -= 1
		return data

	def top(self):
		return self.list.value

	def is_empty(self):
		if self.list == None:
			return True
		return False

	def size(self):
		return self.size


if __name__ == "__main__":
	stack = Stack()
	print(stack.is_empty())
	for i in range(0, 10):
		print(stack.size())
		stack.push(i)
	for i in range(0, 5):
		print(stack.top())
		stack.pop()
	print(stack.is_empty())
