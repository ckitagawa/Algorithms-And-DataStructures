def knapsack(items, W):
	if W < 1:
		raise Exception("weight must be > 0")

	M = [[0 for _ in range(W + 1)] for _ in range(len(items))]
	for i, item in enumerate(items):
		for j in range(0, W + 1):
			if item[0] <= j:
				if i == 0:
					M[i][j] = item[1]
				else:
					v = M[i - 1][j - item[0]]
					x = M[i - 1][j]
					M[i][j] = max(item[1] + v, x)
			elif i > 0:
				M[i][j] = M[i - 1][j]
	out = []
	j = W
	i = len(items) - 1
	print(M)
	while j > 0:
		if M[i][j] == M[i - 1][j]:
			i -= 1
		else:
			out.append(items[i])
			j -= items[i][0]

	return out

if __name__ == "__main__":
	items = [(1, 1), (3, 4), (4, 5), (5, 7)]
	print(knapsack(items, 7))