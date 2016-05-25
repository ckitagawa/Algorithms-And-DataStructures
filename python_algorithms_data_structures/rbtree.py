import queue

global RED, BLACK
RED = 0
BLACK = 1

class RBNode(object):
	def __init__(self, key, value, left=None, right=None, parent=None, color=RED):
		self.key = key
		self.value = value
		self.lchild = left
		self.rchild = right
		self.parent = parent
		self.grandparent = None
		self.uncle = None
		self.sibling = None
		if self.parent:
			if self.parent.parent:
				self.grandparent = self.parent.parent
			if self.grandparent:
				if self.parent == self.grandparent.lchild:
					self.uncle = self.grandparent.rchild
				else:
					self.uncle = self.grandparent.lchild
			if self == self.parent.lchild:
				self.sibling = self.parent.rchild
			else:
				self.sibling = self.parent.lchild
		self.color = color

	def __str__(self):
		return str(self.key)

	def toggle_color(self):
		if self.color == RED:
			self.color = BLACK
		else:
			self.color = RED

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

	def update_node(self, key, value, left, right):
		self.key = key
		self.value = value
		self.lchild = left
		self.rchild = right
		if self.has_lchild():
			self.lchild.parent = self
		if self.has_rchild():
			self.rchild.parent = self

	def update_parentage(self, parent):
		self.parent = parent
		self.grandparent = None
		self.uncle = None
		self.sibling = None
		if self.parent:
			if self.parent.parent:
				self.grandparent = self.parent.parent
			if self.grandparent:
				if self.parent == self.grandparent.lchild:
					self.uncle = self.grandparent.rchild
				else:
					self.uncle = self.grandparent.lchild
			if self == self.parent.lchild:
				self.sibling = self.parent.rchild
			else:
				self.sibling = self.parent.lchild

class RBT(object):
	def __init__(self):
		self.root = None
		self.size = 0

	def __len__(self):
		return self.size

	def insert(self, key, value):
		if self.root:
			self._insert(key, value, self.root)
		else:
			self.root = RBNode(key, value)
			self._insert_case1(self.root)
		self.size += 1

	def _insert(self, key, value, node):
		if key < node.key:
			if node.has_lchild():
				self._insert(key, value, node.lchild)
			else:
				node.lchild = RBNode(key, value, parent=node)
				self._insert_case1(node.lchild)
		elif key > node.key:
			if node.has_rchild():
				self._insert(key, value, node.rchild)
			else:
				node.rchild = RBNode(key, value, parent=node)
				self._insert_case1(node.rchild)
		else:
			raise KeyError("attempted to insert duplicate key")

	def _insert_case1(self, node):
		if not node.parent:
			node.toggle_color()
		else:
			self._insert_case2(node)

	def _insert_case2(self, node):
		if node.parent.color == BLACK:
			return
		else:
			self._insert_case3(node)

	def _insert_case3(self, node):
		if node.uncle != None and node.uncle.color == RED:
			node.uncle.toggle_color()
			node.parent.toggle_color()
			node.grandparent.toggle_color()
			self._insert_case1(node.grandparent)
		else:
			self._insert_case4(node)

	def _insert_case4(self, node):
		if node == node.parent.rchild and node.parent == node.grandparent.lchild:
			self._rotate_left(node.parent)
			node = node.lchild
		elif node == node.parent.lchild and node.parent == node.grandparent.rchild:
			self._rotate_right(node.parent)
			node = node.rchild
		self._insert_case5(node)

	def _insert_case5(self, node):
		print(node)
		node.parent.color = BLACK
		node.grandparent.color = RED
		if node == node.parent.lchild:
			self._rotate_right(node.grandparent)
		else:
			self._rotate_left(node.grandparent)

	def _rotate_left(self, node):
		pivot = node.rchild
		tmp = pivot.lchild
		pivot.lchild = node
		node.rchild = tmp
		pivot.update_parentage(node.parent)
		if pivot.has_rchild():
			pivot.rchild.update_parentage(pivot)
			if pivot.rchild.has_lchild():
				pivot.rchild.lchild.update_parentage(pivot.rchild)
			if pivot.rchild.has_rchild():
				pivot.rchild.rchild.update_parentage(pivot.rchild)
		node.update_parentage(pivot)
		if node.has_lchild():
			node.lchild.update_parentage(node)
			if node.lchild.has_lchild():
				node.lchild.lchild.update_parentage(node.lchild)
			if node.lchild.has_rchild():
				node.lchild.rchild.update_parentage(node.lchild)
		if node.has_rchild():
			node.rchild.update_parentage(node)
			if node.rchild.has_lchild():
				node.rchild.lchild.update_parentage(node.lchild)
			if node.rchild.has_rchild():
				node.rchild.rchild.update_parentage(node.lchild)
		if pivot.parent == None:
			self.root = pivot

	def _rotate_right(self, node):
		pivot = node.lchild
		tmp = pivot.rchild
		pivot.rchild = node
		node.lchild = tmp
		pivot.update_parentage(node.parent)
		if pivot.has_lchild():
			pivot.lchild.update_parentage(pivot)
			if pivot.lchild.has_lchild():
				pivot.lchild.lchild.update_parentage(pivot.lchild)
			if pivot.lchild.has_rchild():
				pivot.lchild.rchild.update_parentage(pivot.lchild)
		node.update_parentage(pivot)
		if node.has_lchild():
			node.lchild.update_parentage(node)
			if node.lchild.has_lchild():
				node.lchild.lchild.update_parentage(node.lchild)
			if node.lchild.has_rchild():
				node.lchild.rchild.update_parentage(node.lchild)
		if node.has_rchild():
			node.rchild.update_parentage(node)
			if node.rchild.has_lchild():
				node.rchild.lchild.update_parentage(node.lchild)
			if node.rchild.has_rchild():
				node.rchild.rchild.update_parentage(node.lchild)
		if pivot.parent == None:
			self.root = pivot

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
				if toremove.has_both_children():
					toremove = self.__relocate(toremove)
				if toremove.has_children():
					self._delete_one_child(toremove)
				else:
					if toremove == toremove.parent.rchild:
						if toremove.parent.has_lchild():
							toremove.parent.lchild.sibling = None
						toremove.parent.rchild = None
					else:
						if toremove.parent.has_rchild():
							toremove.parent.rchild.sibling = None
						toremove.parent.lchild = None
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

	def __relocate(self, node):
		s = self.__successor(node)
		s.key, s.value, node.key, node.value = node.key, node.value, s.key, s.value
		return s

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

	def _delete_one_child(self, node):
		if node.has_lchild():
			child = node.lchild
			r = False
		else:
			child = node.rchild
			r = True
		child.value, child.key, child.color, node.key, node.value, node.color = node.key, node.value, node.color, child.value, child.key, child.color
		if child.color == BLACK:
			if node.color == RED:
				node.color = BLACK
			else:
				self._delete_case1(node)
		if r:
			node.rchild = None
			if node.has_lchild():
				node.lchild.sibling = None
		else:
			node.lchild = None
			if node.has_rchild():
				node.rchild.sibling = None

	def _delete_case1(self, node):
		if node.parent != None:
			self._delete_case2(node)

	def _delete_case2(self, node):
		if node.sibling:
			if node.sibling.color == RED:
				node.parent.color = RED
				node.sibling.color = BLACK
				if node == node.parent.lchild:
					self._rotate_left(node.parent)
				else:
					self._rotate_right(node.parent)
		self._delete_case3(node)

	def _delete_case3(self, node):
		if node.sibling:
			if node.sibling.has_both_children():
				if node.parent.color == BLACK and node.sibling.color == BLACK and node.sibling.lchild.color == BLACK and node.sibling.rchild.color == BLACK:
					node.sibling.color = RED
					_delete_case1(node.parent)
				else:
					self._delete_case4(node)

	def _delete_case4(self, node):
		if node.parent.color == RED and node.sibling.color == BLACK and node.sibling.lchild.color == BLACK and node.sibling.rchild.color == BLACK:
			node.sibling.color = RED
			node.parent.color = BLACK
		else:
			self._delete_case5(node)

	def _delete_case5(self, node):
		if node == node.parent.lchild and node.sibling.rchild == BLACK:
			node.sibling.color = RED
			node.sibling.lchild = BLACK
			self._rotate_right(node.sibling)
		elif node == node.parent.rchild and node.sibling.lchild == BLACK:
			node.sibling.color = RED
			node.sibling.rchild = BLACK
			self._rotate_left(node.sibling)
		self._delete_case6(node)

	def _delete_case6(self, node):
		node.sibling.color = node.parent.color
		node.parent.color = BLACK
		if node == node.parent.lchild:
			node.sibling.rchild.color = BLACK
			self._rotate_left(node.parent)
		else:
			node.sibling.lchild.color = BLACK
			self._rotate_right(node.parent)

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
	tree = RBT()
	for i in ['j','f', 'a', 'd', 'w', 'h', 'n', 'o', 'k' ]:
		tree[i] = 0

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



