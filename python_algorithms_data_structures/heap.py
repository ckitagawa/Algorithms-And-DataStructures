import queue
import random

class HeapNode(object):
	def __init__(self, key, value, left=None, right=None, parent=None):
		self.key = key
		self.value = value
		self.lchild = left
		self.rchild = right
		self.parent = parent

	def __str__(self):
		return str(self.value)

	def has_lchild(self):
		return self.lchild

	def has_rchild(self):
		return self.rchild

	def is_lchild(self):
		return self.parent and self.parent.lchild == self

	def is_rchild(self):
		return self.parent and self.parent.rchild == self

	def is_root(self):
		return not self.parent

	def is_leaf(self):
		return not (self.lchild or self.rchild)

	def has_children(self):
		return self.lchild or self.rchild

	def has_both_children(self):
		return self.lchild and self.rchild

	def update_node(self, key, value, left, right, parent):
		self.key = key
		self.value = value
		self.lchild = left
		self.rchild = right
		if self.has_lchild():
			self.lchild.parent = self
		if self.has_rchild():
			self.rchild.parent = self

class Heap(object):
	def __init__(self, size):
		self.root = None
		self.size = size
		for i in range(0, size):
			self._insert(i, None)

	def __len__(self):
		return self.size

	def add(self, key, value):
		node = self._find(key, self.root)
		if node:
			node.value = value
		else:
			raise KeyError("invalid key")

	def _insert(self, key, value=None):
		if self.root:
			self.__insert(key, value, self.root)
		else:
			self.root = HeapNode(key, value)
		self.size += 1

	def __insert(self, key, value, node):
		if key < node.key:
			if node.has_lchild():
				self.__insert(key, value, node.lchild)
			else:
				node.lchild = HeapNode(key, value, parent=node)
		elif key > node.key:
			if node.has_rchild():
				self.__insert(key, value, node.rchild)
			else:
				node.rchild = HeapNode(key, value, parent=node)
		else:
			raise KeyError("attempted to insert duplicate key")

	def __setitem__(self, key, value):
		self.add(key, value)

	def find(self, key):
		if self.root:
			res = self._find(key, self.root)
			if res:
				return res.value
			else:
				return None
		else:
			raise Exception("no root node")

	def _find(self, key, node):
		if not node:
			return None
		elif node.key == key:
			return node
		elif key < node.key and node.has_lchild():
			return self._find(key, node.lchild)
		elif key > node.key and node.has_rchild():
			return self._find(key, node.rchild)

	def __getitem__(self, key):
		return self.find(key)

	def __contains__(self, key):
		if self._find(key, self.root):
			return True
		return False

	def delete(self, key):
		toremove = self._find(key, self.root)
		if toremove:
			toremove.value = None
		else:
			raise KeyError("key not in tree")

	def __delitem__(self, key):
		self.delete(key)


	# This is a transversal
	def DFS(self, ttype=0):
		self.type = ttype
		if self.root:
			self.nodes = []
			self.values = []
			if self.root.has_children():
				self._depth_recurse(self.root)
			else:
				self.nodes.append(self.root.key)
				self.values.append(self.root.values)
			return self.values
		else:
			return None

	def _depth_recurse(self, node):
		# Preorder
		if self.type == 0:
			self.nodes.append(node.key)
			self.values.append(node.value)
		if node.has_lchild():
			if not node.lchild.key in self.nodes:
				self._depth_recurse(node.lchild)
		# Inorder
		if self.type == 1:
			self.nodes.append(node.key)
			self.values.append(node.value)
		if node.has_rchild():
			if not node.rchild.key in self.nodes:
				self._depth_recurse(node.rchild)
		# Postorder
		if self.type == 2:
			self.nodes.append(node.key)
			self.values.append(node.value)
		return

	def BFS(self):
		q = queue.Queue()
		nodes = []
		q.enqueue(self.root)
		while q.head:
			current = q.dequeue()
			nodes.append(current.value)
			if current.has_lchild():
				q.enqueue(current.lchild)
			if current.has_rchild():
				q.enqueue(current.rchild)
		return nodes

	def max_heapify(self):
		for i in range(self.size // 2, -1, -1):
			self._max_heapify(i)

	def _max_heapify(self, i):
		node = self._find(i, self.root)
		if node:
			if node.has_both_children():
				if node.lchild.value > node.rchild.value and node.lchild.value > node.value:
					node.value, node.lchild.value = node.lchild.value, node.value
				elif node.rchild.value > node.lchild.value and node.rchild.value > node.value:
					node.value, node.rchild.value = node.rchild.value, node.value
			if node.has_lchild():
				if node.lchild.value > node.value:
					node.value, node.lchild.value = node.lchild.value, node.value
			if node.has_rchild():
				if node.rchild.value > node.value:
					node.value, node.rchild.value = node.rchild.value, node.value

	def min_heapify(self):
		for i in range(self.size // 2, -1, -1):
			self._min_heapify(i)

	def _min_heapify(self, i):
		node = self._find(i, self.root)
		if node:
			if node.has_both_children():
				if node.lchild.value < node.rchild.value and node.lchild.value < node.value:
					node.value, node.lchild.value = node.lchild.value, node.value
				elif node.rchild.value < node.lchild.value and node.rchild.value < node.value:
					node.value, node.rchild.value = node.rchild.value, node.value
			if node.has_lchild():
				if node.lchild.value < node.value:
					node.value, node.lchild.value = node.lchild.value, node.value
			if node.has_rchild():
				if node.rchild.value < node.value:
					node.value, node.rchild.value = node.rchild.value, node.value

if __name__ == "__main__":
	SIZE = 100
	heap = Heap(SIZE)
	for i in range(0, SIZE):
		heap[i] = random.randint(0, 150)

	#heap.max_heapify()
	heap.min_heapify()
	print(heap.DFS())
	print(heap.BFS())

# if __name__ == "__main__":
# 	mytree = Heap()
# 	mytree[3]="red"
# 	mytree[4]="blue"
# 	mytree[6]="yellow"
# 	mytree[2]="at"

# 	print(mytree.find(6))
# 	print(mytree[2])
# 	mytree.delete(4)
# 	print(mytree[6])
# 	print(mytree[4])



