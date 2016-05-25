# CliqueCuts
import itertools as it

def solve(n, a, b, c):
	d = set(zip(zip(a, b), c))
	S = 0
	meaningful_set = set(a + b)
	combs = []
	for i in range(1, len(meaningful_set) + 1):
		combs += it.combinations(meaningful_set, i)
	for comb in combs:
		alice = set([edge if (set(edge[0]).issubset(set(comb))) else None for edge in list(d)])
		alice.discard(None)
		unused = d.difference(alice)
		bob = set([None if (edge[0][0] in comb or edge[0][1] in comb or edge[0] in comb) else edge for edge in list(unused)])
		bob.discard(None)
		if (alice == set()) and (bob == set()):
			S += 0
		elif alice == set():
			S -= sum(x[1] for x in list(bob))
		elif bob == set():
			S += sum(x[1] for x in list(alice))
		else:
			S += sum(x[1] for x in list(alice)) - sum(x[1] for x in list(bob))
	return S % 1000000007

if __name__ == '__main__':
	print(solve( 2, [0], [1], [100] ))
	print(solve( 5, [0,0,0,0,1,1,1,2,2,3], [1,2,3,4,2,3,4,3,4,4], [0,1,2,3,4,5,6,7,8,9] ))
	print(solve( 10, [0,1,2,9,5,3,4,7,3,4,1,5,2,3,0,7,8], [6,7,4,5,6,2,6,3,1,8,2,0,9,9,8,2,5], [10000,10000000,100000000,100,10,1,1000,100,10000,100,10000,1000,100,10,100,100000000,10]))
	print(solve( 5, [0,1,2,3], [1,2,3,4], [9,2,4,3]))
	print(solve( 45, [], [], []))