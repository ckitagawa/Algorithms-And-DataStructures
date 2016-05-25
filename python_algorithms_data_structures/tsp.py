from math import sqrt, inf
from random import randint

def distance(vertex1, vertex2):
	a = 0
	for i, j in zip(vertex1[1], vertex2[1]):
		a += (i - j) ** 2
	return sqrt(a)

def tsp_solve(verticies):
	v = verticies
	length = 0
	v.remove(verticies[-1])
	for i in range(len(verticies)-1, 0, -1):
		min_v = None
		min_d = inf
		for j in range(0, len(v)):
			if not (verticies[i] == v[j]):
				d = distance(verticies[i], v[j])
				if d < min_d:
					min_d = d
					min_v = v[j]
		v.remove(min_v)
		length += min_d
	return min_d

if __name__ == "__main__":
	MAX = 400

	v = []
	for i in range(0, 700):
		v.append((i, [randint(0, MAX), randint(0, MAX), randint(0, MAX)]))
	print(tsp_solve(v))
