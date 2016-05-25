import string
import queue
import sys
import math

def max_price(arr):
	if len(arr) < 2:
		raise Exception("minimum two prices needed")
	min_price = arr[0]
	max_profit = arr[1] - arr[0]
	for i, stock in enumerate(arr):
		if i == 0:
			continue
		potential = stock - min_price
		max_profit = max(max_profit, potential)
		min_price = min(stock, min_price)

	return max_profit

class Acronyms:
	def __init__(self):
		return

	def acronize(self, document):
		for j, line in enumerate(document):
			UC = []
			gap = 0
			start = True
			first = None
			last = None
			line = line.split(" ")
			for i, word in enumerate(line):
				if word.title() == word and start != True:
					UC.append(word)
					if not first:
						first = i
					else:
						last = i
					gap = 0
				else:
					gap += 1
					start = None
				if gap > 1:
					if len(UC) > 1:
						line = self._replace(UC, line, first, last)
					UC = []
					first = None
					last = None
				if word.find(".") != -1 or word.find("\n") != -1 or line[-1] == line[i]:
					if len(UC) > 1:
						line = self._replace(UC, line, first, last)
					UC = []
					first = None
					last = None
			document[j] = " ".join(line)
		return document

	def _replace(self, UC, line, first, last):
		acc = ""
		for i, word in enumerate(UC):
			acc += "".join(list(filter(lambda x: x.isupper(), word)))
			if i == len(UC) - 1:
				if word[-1] in string.punctuation and word[-1] != ',':
					acc += word[-1]
		return line[:first] + [acc] + line[last + 1:]

class AdaptiveRouting:
	def deliveryTime(self, layout, failed, A, B):
		V = []
		E = {}
		for i, link in enumerate(layout):
			L = link.split(" ")
			for j in [0, 1]:
				if L[j] not in V:
					V.append(L[j])
			if i not in failed:
				if int(L[0]) > int(L[1]):
					E[" ".join([L[1], L[0]])] = int(L[2])
				else:
					E[" ".join(L[:2])] = int(L[2])
		G = [V, E]
		return self._dijkstra(G, A, B)


	# Shortest path algorithm using a priority queue
	def _dijkstra(self, G, A, B):
		dist = {}
		dist[str(A)] = 0
		inQ = []
		Q = queue.PriorityQueue()
		for i, v in enumerate(G[0]):
			if int(v) != A:
				dist[v] = sys.maxsize
				inQ.append(v)
			Q.put((dist[v], v))

		print(G[1])
		while not Q.empty():
			u = Q.get()
			if int(u[1]) == B:
				if dist[str(B)] != sys.maxsize:
					return dist[str(B)]
			for v in inQ:
				if int(u[1]) < int(v):
					s = u[1] + " " + v
				else:
					s = v + " " + u[1]
				if s in G[1]:
					alt = dist[u[1]] + G[1][s]

					if alt < dist[v]:
						dist[v] = alt
						Q.put((alt, v))
		if str(B) in dist:
			if dist[str(B)] == sys.maxsize:
				return -1
			return dist[str(B)]
		return -1

class BatchSystem:
	def schedule(self, durations, names):
		out = []
		for i in zip(zip(durations, names), range(0, len(names))):
			out.append(i)
		out = sorted(out)
		return [out[i] for i in range(0, len(out))]

class ABCPath:
	def length(self, grid):
		i = 0
		max_length = 0
		length = 0
		s = "".join(grid)
		i = s.find('A', 0)
		while i >= 0:
			self.col = i % len(grid[0])
			self.row = math.floor(i // len(grid[0]))
			for L in string.ascii_uppercase:
				l = self._search(grid, L)
				if l == 0:
					break
				else:
					length += l
			if length > max_length:
				max_length = length
			length = 0
			i = s.find('A', i + 1)
		return max_length

	def _search(self, grid, L):
		for j in range(self.row - 1, self.row + 2):
			for k in range(self.col -1, self.col +2 ):
				if j >= 0 and k >= 0 and j <= len(grid) - 1 and k <= len(grid[0]) - 1:
					if grid[j][k] == L:
						self.row = j
						self.col = k
						return 1
		return 0

def rotate(matrix):
	return fliplr(transpose(matrix, len(matrix[0])))

def transpose(matrix, n):
	return [[row[i] for row in matrix] for i in range(n)]

def fliplr(matrix):
	return [row[::-1] for row in matrix]

if __name__ == "__main__":
	s = [10, 7, 5, 8, 11, 9]
	print(max_price(s))
	a = Acronyms()
	print(a.acronize(["We the people of the United States of America.", "Don't worry. Be Happy!"]))
	A = AdaptiveRouting()
	l = ["4 3 100", "2 4 3", "3 2 1", "2 5 1", "4 1 2", "5 4 1"]
	f = [2, 5]
	a = 1
	b = 3
	print(A.deliveryTime(l, f, a, b))
	b = BatchSystem()
	print(b.schedule([400, 100, 100, 100], ["Danny Messer", "Stella Bonasera", "Stella Bonasera", "Mac Taylor"]))
	abc = ABCPath()
	print(abc.length(["KCBVNRXSPVEGUEUFCODMOAXZYWEEWNYAAXRBKGACSLKYRVRKIO", "DIMCZDMFLAKUUEPMPGRKXSUUDFYETKYQGQHNFFEXFPXNYEFYEX", "DMFRPZCBOWGGHYAPRMXKZPYCSLMWVGMINAVRYUHJKBBRONQEXX", "ORGCBHXWMTIKYNLFHYBVHLZFYRPOLLAMBOPMNODWZUBLSQSDZQ", "QQXUAIPSCEXZTTINEOFTJDAOBVLXZJLYOQREADUWWSRSSJXDBV", "PEDHBZOVMFQQDUCOWVXZELSEBAMBRIKBTJSVMLCAABHAQGBWRP", "FUSMGCSCDLYQNIXTSTPJGZKDIAZGHXIOVGAZHYTMIWAIKPMHTJ", "QMUEDLXSREWNSMEWWRAUBFANSTOOJGFECBIROYCQTVEYGWPMTU", "FFATSKGRQJRIQXGAPLTSXELIHXOPUXIDWZHWNYUMXQEOJIAJDH", "LPUTCFHYQIWIYCVOEYHGQGAYRBTRZINKBOJULGYCULRMEOAOFP", "YOBMTVIKVJOSGRLKTBHEJPKVYNLJQEWNWARPRMZLDPTAVFIDTE", "OOBFZFOXIOZFWNIMLKOTFHGKQAXFCRZHPMPKGZIDFNBGMEAXIJ", "VQQFYCNJDQGJPYBVGESDIAJOBOLFPAOVXKPOVODGPFIYGEWITS", "AGVBSRLBUYOULWGFOFFYAAONJTLUWRGTYWDIXDXTMDTUYESDPK", "AAJOYGCBYTMXQSYSPTBWCSVUMNPRGPOEAVVBGMNHBXCVIQQINJ", "SPEDOAHYIDYUJXGLWGVEBGQSNKCURWYDPNXBZCDKVNRVEMRRXC", "DVESXKXPJBPSJFSZTGTWGAGCXINUXTICUCWLIBCVYDYUPBUKTS", "LPOWAPFNDRJLBUZTHYVFHVUIPOMMPUZFYTVUVDQREFKVWBPQFS", "QEASCLDOHJFTWMUODRKVCOTMUJUNNUYXZEPRHYOPUIKNGXYGBF", "XQUPBSNYOXBPTLOYUJIHFUICVQNAWFMZAQZLTXKBPIAKXGBHXX"]))
	mat = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]
	print(rotate(mat))