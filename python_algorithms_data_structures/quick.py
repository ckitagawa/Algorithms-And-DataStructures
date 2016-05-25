import numpy as np

def reverse_string(string):
	li = list(string)
	li.reverse()
	return "".join(li)

def rotate_matrix(arr):
	A = np.array(arr)
	A.transpose()
	return list(np.fliplr(A))


if __name__ == "__main__":
	print(reverse_string("Hello"))
	print(rotate_matrix([[1,2,3],[4,5,6],[7,8,9]]))