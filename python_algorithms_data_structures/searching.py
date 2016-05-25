import stack

def DFS(graph, start):
	visited, s = [], stack.Stack()
	s.push(start)
	while s:
		node = stack.pop()
		if node.key not in visited:
			visited.add(node.key)



import random
from binary_tree import *

if __name__ == "__main__":
	tree = BST()
	key = 10
	tree[key] = 1
	for i in range(0, 20):
		if i != 10:
			tree[i] = 0

	print(DFS(tree, tree.root))