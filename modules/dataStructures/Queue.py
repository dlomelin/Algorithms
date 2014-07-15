from Algorithms.modules.dataStructures.MixinEquality import MixinEquality

class Queue(MixinEquality):
	def __init__(self, array = []):
		self.__array = array
		self.__setIndices()


	########################
	# Operator Overloading #
	########################

	def __str__(self):
		# Calls __iter__ and converts to a string
		return str(list(self))

	def __len__(self):
		return self.__tail() - self.__head()

	def __iter__(self):
		for i in xrange(self.__head(), self.__tail()):
			yield self[i]

	def __getitem__(self, index):
		return self.__array[index]

	##################
	# Public Methods #
	##################

	def enqueue(self, value):
		try:
			self[self.__tail()] = value
		except:
			self.__array.append(value)
		self.__increaseTail()

	def dequeue(self):
		if self.empty():
			# TODO change to return None instead?
			raise Exception('No items left to dequeue in queue')
		else:
			self.__increaseHead()
			return self[self.__head() - 1]

	# Returns True or False if the Queue is empty
	def empty(self):
		if self.__head() == self.__tail():
			return True
		else:
			return False

	###################
	# Private Methods #
	###################

	def __setIndices(self):
		self.__setHead(0)
		self.__setTail(len(self.__array))

	def __head(self):
		return self.__headIndex
	def __setHead(self, value):
		self.__headIndex = value
	def __increaseHead(self):
		self.__headIndex += 1

	def __tail(self):
		return self.__tailIndex
	def __setTail(self, value):
		self.__tailIndex = value
	def __increaseTail(self):
		self.__tailIndex += 1
