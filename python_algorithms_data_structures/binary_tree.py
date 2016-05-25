import queue

class BSTNode(object):
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

class BST(object):
	def __init__(self):
		self.root = None
		self.size = 0

	def __len__(self):
		return self.size

	def insert(self, key, value):
		if self.root:
			self._insert(key, value, self.root)
		else:
			self.root = BSTNode(key, value)
		self.size += 1

	def _insert(self, key, value, node):
		if key < node.key:
			if node.has_lchild():
				self._insert(key, value, node.lchild)
			else:
				node.lchild = BSTNode(key, value, parent=node)
		elif key > node.key:
			if node.has_rchild():
				self._insert(key, value, node.rchild)
			else:
				node.rchild = BSTNode(key, value, parent=node)
		else:
			raise KeyError("attempted to insert duplicate key")

	def __setitem__(self, key, value):
		self.insert(key, value)

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
		if self.size > 1:
			toremove = self._find(key, self.root)
			if toremove:
				self.__remove(toremove)
				self.size -= 1
			else:
				raise KeyError("key not in tree")
		elif self.size == 1 and self.root.key == key:
			self.root = None
			self.size -= 1
		else:
			raise Exception("no root node")

	def __delitem__(self, key):
		self.delete(key)

	def __splice(self, node):
		if node.is_leaf():
			if node.is_lchild():
				node.parent.lchild = None
			else:
				node.parent.rchild = None
		elif node.has_children():
			if node.has_lchild():
				if node.is_lchild():
					node.parent.lchild = node.lchild
				else:
					node.parent.rchild = node.lchild
				node.lchild.parent = node.parent
			else:
				if node.is_lchild():
					node.parent.lchild = node.rchild
				else:
					node.parent.rchild = node.rchild
				node.rchild.parent = node.parent

	def __successor(self, node):
		s = None
		if node.has_rchild():
			s = self.__fmin(node.rchild)
		else:
			if node.parent:
				if node.is_lchild():
					s = node.parent
				else:
					node.parent.rchild = None
					s = self.__successor(node.parent)
					node.parent.rchild = self
		return s

	def __fmin(self, node):
		current = node
		while current.has_lchild():
			current = current.lchild
		return current

	def __remove(self, node):
		if node.is_leaf():
			if node == node.parent.lchild:
				node.parent.lchild = None
			else:
				node.parent.rchild = None
		elif node.has_both_children():
			s = self.__successor(node)
			self.__splice(s)
			node.key = s.key
			node.value = s.value
		else:
			if node.has_lchild():
				if node.is_lchild():
					node.lchild.parent = node.parent
					node.parent.lchild = node.lchild
				elif node.is_rchild():
					node.lchild.parent = node.parent
					node.parent.rchild = node.lchild
				else:
					node.update_node(node.lchild.key,
									node.lchild.value,
									node.lchild.lchild,
									node.lchild.rchild)
			else:
				if node.is_lchild():
					node.rchild.parent = node.parent
					node.parent.lchild = node.rchild
				elif node.is_rchild():
					node.rchild.parent = node.parent
					node.parent.rchild = node.rchild
				else:
					node.update_node(node.rchild.key,
									node.rchild.value,
									node.rchild.lchild,
									node.rchild.rchild)

	# This is a transversal
	def DFS(self, ttype=0):
		self.type = ttype
		if self.root:
			self.nodes = []
			if self.root.has_children():
				self._depth_recurse(self.root)
			else:
				self.nodes.append(self.root.key)
			return self.nodes
		else:
			return None

	def _depth_recurse(self, node):
		# Preorder
		if self.type == 0:
			self.nodes.append(node.key)
		if node.has_lchild():
			if not node.lchild.key in self.nodes:
				self._depth_recurse(node.lchild)
		# Inorder
		if self.type == 1:
			self.nodes.append(node.key)
		if node.has_rchild():
			if not node.rchild.key in self.nodes:
				self._depth_recurse(node.rchild)
		# Postorder
		if self.type == 2:
			self.nodes.append(node.key)
		return

	def BFS(self):
		q = queue.Queue()
		nodes = []
		q.enqueue(self.root)
		while q.head:
			current = q.dequeue()
			nodes.append(current.key)
			if current.has_lchild():
				q.enqueue(current.lchild)
			if current.has_rchild():
				q.enqueue(current.rchild)
		return nodes

if __name__ == "__main__":
	tree = BST()
	for i in ['j','f', 'a', 'd', 'h', 'k', 'z']:
		tree[i] = 0


	tree.delete('j')
	print(tree.DFS())
	print(tree.BFS())

# if __name__ == "__main__":
# 	mytree = BST()
# 	mytree[3]="red"
# 	mytree[4]="blue"
# 	mytree[6]="yellow"
# 	mytree[2]="at"

# 	print(mytree.find(6))
# 	print(mytree[2])
# 	mytree.delete(4)
# 	print(mytree[6])
# 	print(mytree[4])



