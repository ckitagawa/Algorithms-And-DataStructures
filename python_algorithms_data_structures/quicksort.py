from math import floor

def quicksort(A):
	less = []
	equal = []
	greater = []

	l = len(A)

	if l > 1:
		pivot = A[l // 2]
		for x in A:
			if x > pivot:
				greater.append(x)
			elif x < pivot:
				less.append(x)
			else:
				equal.append(x)
		return quicksort(less) + equal + quicksort(greater)
	else:
		return A

if __name__ == "__main__":
	A = [1,4736,65,24,3,4,23,4,2133,2,3,2,4,23,4,1,6564,132,534,23,5]
	print(quicksort(A))