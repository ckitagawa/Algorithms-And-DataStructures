# Sorting in general
# Most systems use Heap, Insertion, or Quicksort all of which are on average (n log n) algorithms
# In embedded or memory restricted applications Heap or an optimially gapped Shell sort might be preferred
# Radix sort is useful in the event n is large and word size (length of integers) is relatively small ie w < log n

# Use Cases:
# Low memory: Heap/Shell
# Almost Sorted ie insertions are approximate but generally the list is kept sorted by default: Insertion/Shell
# Sorted: Insertion/Shell
# Reversed: Heap/Merge/Quick
# Random: Quick/Heap/Merge
# len(int) is small and n is large: Radix


# Quicksort:
# Best case O(n log(n)) or n , Average case O(n log(n)), Worst case O(n^2) <- bad for sorted or almost sorted data
# Memory usage is between O(log n) average and O(n) worst
# Unstable
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

# Mergesort:
# Always O(n log n) <- generally useful
# Memory usage is O(n)
# Stable ie items will be in order they are inserted if equal
def mergesort(A):
	l = len(A)
	if l > 1:
		mid = l // 2
		left = mergesort(A[0:mid])
		right = mergesort(A[mid:])

		li = []
		i = 0
		j = 0
		while i < len(left) and j < len(right):
			if left[i] > right[j]:
				li.append(right[j])
				j += 1
			else:
				li.append(left[i])
				i += 1
		if j < len(right):
			li += right[j:]
		elif i < len(left):
			li += left[i:]
		return li
	return A

# Heapsort:
# Always O(n log n) <- generally useful better in low memory applications
# In place sort memory usage is O(1)
# Generally unstable requires two methods
def siftdown(A, first, last):
	largest = 2 * first + 1
	while largest <= last:
		if (largest < last) and (A[largest] < A[largest + 1]):
			largest += 1
		if A[largest] > A[first]:
			A[largest], A[first] = A[first], A[largest]
			first = largest
			largest = 2 * first + 1
		else:
			return

def heapsort(A):
	l = len(A) - 1
	iParent = l // 2
	for i in range(iParent, -1, -1):
		siftdown(A, i, l)

	for i in range(l, 0, -1):
		if A[0] > A[i]:
			A[0], A[i] = A[i], A[0]
			siftdown(A, 0, i - 1)

	return A

# Radix Sort (integer sorting): (Stable Variant)
# n * k/d where k = key size and d = digit size (10) typically proportional to O(n log n)
# requires n + 2^d memory
# Stable
def radixsort(A):
	RADIX = 10
	ml = False
	tmp, placement = -1, 1

	while not ml:
		ml = True
		buckets = [list() for _ in range(RADIX)]

		for i in A:
			tmp = i / placement
			buckets[int(tmp % RADIX)].append(i)
			if ml and tmp > 0:
				ml = False

		a = 0
		for b in range(RADIX):
			buck = buckets[b]
			for i in buck:
				A[a] = i
				a += 1

		placement *= RADIX

	return A

if __name__ == "__main__":
	A = [1,4736,65,24,3,4,23,4,2133,2,3,2,4,23,4,1,6564,132,534,23,5]
	print(quicksort(A))
	print(mergesort(A))
	print(heapsort(A))
	print(radixsort(A))