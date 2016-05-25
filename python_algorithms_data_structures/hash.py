#This is a linear probing variant of a Hash table. It fills up faster than a chain version when a collision occurs
#It is easier to implement and requires less recursion.

class HashTable:
	def __init__(self, size):
		self.keys = [None] * size
		self.values = [None] * size
		self.size = size

	def __hash_fn(self, value):
		return hash(value) % self.size

	def is_full(self):
		if None in self.keys:
			return False
		return True

	def is_empty(self):
		if set(self.keys) == {None}:
			return True
		return False

	def insert(self, key, value):
		if key in set(self.keys):
			return False
		index = self.__hash_fn(key)
		if self.keys[index] == None:
			self.keys[index] = key
			self.values[index] = value
		else:
			if self.is_full() == False:
				i = 1
				while i <= self.size:
					if i + index >= self.size:
						i = -index
					if self.keys[index + i] == None:
						self.keys[index + i] = key
						self.values[index + i] = value
						break
					i += 1
			else:
				return False
		return None

	def remove(self, key):
		index = self.__hash_fn(key)
		if self.keys[index] == key:
			self.keys[index] = None
			self.values[index] = None
		else:
			i = 1
			while i <= self.size:
				if i + index >= self.size:
					i = -index
				elif i == 0:
					return False
				if self.keys[index + i] == None:
					return False
				elif self.keys[index + i] == key:
					self.keys[index + i] == None
					self.values[index + i] == None
					return True
				i += 1


	def retrieve(self, key):
		index = self.__hash_fn(key)
		if self.keys[index] == key:
			return self.values[index]
		elif self.keys[index] == None:
			return None
		else:
			i = 1
			while i <= self.size:
				if i + index >= self.size:
					i = -index
				elif i == 0:
					return None
				if self.keys[index + i] == None:
					return None
				elif self.keys[index + i] == key:
					return self.values[index + i]
				i += 1

	def clear(self):
		self.keys = [None] * self.size
		self.values = [None] * self.size


if __name__ == "__main__":
	ht = HashTable(2)
	print("Is Full? {}".format(ht.is_full()))
	print("Is Empty? {}".format(ht.is_empty()))
	ht.insert("Hello", "World")
	ht.insert("Test", "ing")
	ht.insert("Delta", 1000)
	print("Look for Value corresponding to Hello {}".format(ht.retrieve("Hello")))
	print("Try an invalid insert {}".format(ht.insert("Hello", 9)))
	ht.remove("Hello")
	print("Look for Value corresponding to Hello {}".format(ht.retrieve("Hello")))
	print("Look for Value corresponding to Test {}".format(ht.retrieve("Test")))
	print("Look for Value corresponding to Delta {}".format(ht.retrieve("Delta")))
	ht.clear()
	print("Is Empty? {}".format(ht.is_empty()))
