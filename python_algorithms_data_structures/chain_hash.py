#This is a chaining variant of a Hash table.
#It is generally a better implementation than linear probing except when memory might be an issue.

class Chainlink(object):
	def __init__(self, key, value, next_link=None):
		self.key = key
		self.value = value
		self.next_link = next_link

class HashTable(object):
	def __init__(self, size):
		self.table = [None] * size
		self.size = size

	def __hash_fn(self, value):
		return hash(value) % self.size

	def is_full(self):
		if None in self.table:
			return False
		return True

	def is_empty(self):
		if set(self.table) == {None}:
			return True
		return False

	def insert(self, key, value):
		index = self.__hash_fn(key)
		if self.table[index] == None:
			self.table[index] = Chainlink(key, value)
			return True
		else:
			return self.__recurse_insert(key, value, self.table[index])

	def remove(self, key):
		index = self.__hash_fn(key)
		if self.table[index] == None:
			return False
		else:
			self.table[index] = self.__recurse_delete(key, self.table[index])
			return

	def retrieve(self, key):
		index = self.__hash_fn(key)
		if self.table[index] == None:
			return None
		else:
			return self.__recurse_get(key, self.table[index])

	def clear(self):
		self.table = [None] * self.size

	def __recurse_insert(self, key, value, link):
		if link.key == key:
			return False
		if link.next_link == None:
			link.next_link = Chainlink(key, value)
			return True
		else:
			return self.__recurse_insert(key, value, link.next_link)

	def __recurse_delete(self, key, link):
		if link.key == key:
			return link.next_link
		elif link.next_link == None:
			return None
		else:
			link.next_link = self.__recurse_delete(key, link.next_link)

	def __recurse_get(self, key, link):
		if link.key == key:
			return link.value
		elif link.next_link == None:
			return None
		else:
			return self.__recurse_get(key, link.next_link)


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
	print("Is Empty? {}".format(ht.is_empty()))
	print(ht.__name__)
	ht.clear()
	print("Is Empty? {}".format(ht.is_empty()))
