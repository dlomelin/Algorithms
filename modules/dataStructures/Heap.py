import sys, operator

class Heap(object):
	def __init__(self, array = [], heapType = 'max'):
		self.__array = array
		self.__setHeapType(heapType)
		self.__resetArrayLength() # Remove if parent, left, and right methods become private
		self.buildHeap()

	def sort(self):
		for i in xrange(self._arrayLength() - 1, 0, -1):
			self._swapArrayPositions(0, i)
			self._reduceArrayLength()
			self._floatDownHeap(0)

	def parent(self, index):
		pIndex = (index - 1) / 2
		if pIndex < 0:
			pIndex = None
		return pIndex

	def left(self, index):
		lIndex = 2*index + 1
		if lIndex >= self._arrayLength():
			lIndex = None
		return lIndex

	def right(self, index):
		rIndex = 2*index + 2
		if rIndex >= self._arrayLength():
			rIndex = None
		return rIndex

	def insert(self, value):
		self._increaseArrayLength()
		try:
			self.__array[self._arrayLength() - 1] = value
		except:
			self.__array.append(value)

		self._floatUpHeap(self._arrayLength() - 1)

	# Create a heap where all nodes below any given node have smaller values
	def buildHeap(self):
		self.__resetArrayLength()

		# Iterate through all non leaf nodes and float down all values.
		# Start with the nodes that are furthest down first.
		for i in xrange(self._arrayLength()/2 - 1, -1, -1):
			self._floatDownHeap(i)

	########################
	# Operator Overloading #
	########################

	def __eq__(self, other):
		return self.__array == other.__array

	def __str__(self):
		return str(self.__array)

	def __len__(self):
		return len(self.__array)

	def __getitem__(self, index):
		return self.__array[index]

	########################
	# Semi-Private Methods #
	########################

	def _arrayLength(self):
		return self.__arrayLen

	def _reduceArrayLength(self):
		self.__arrayLen -= 1

	def _increaseArrayLength(self):
		self.__arrayLen += 1

	def _swapArrayPositions(self, idx1, idx2):
		self.__array[idx1], self.__array[idx2] = self.__array[idx2], self.__array[idx1]

	def _floatDownHeap(self, index):

		leftIndex = self.left(index)
		rightIndex = self.right(index)

		# Between the starting node and its left and right nodes, determine which one
		# has the largest(if max heap) or lowest(if min heap) value and store its
		# index position.
		if not leftIndex is None and self.__floatOperator(self[leftIndex], self[index]):
			switchIndex = leftIndex
		else:
			switchIndex = index

		if not rightIndex is None and self.__floatOperator(self[rightIndex], self[switchIndex]):
			switchIndex = rightIndex

		# If the largest value is not the current index, then swap the switch index
		# value with the current index position and repeat.  Otherwise terminate.
		if switchIndex != index:
			self._swapArrayPositions(switchIndex, index)
			self._floatDownHeap(switchIndex)

	def _floatUpHeap(self, index):

		parentIndex = self.parent(index)

		while index > 0 and self.__floatOperator(self.__array[index], self.__array[parentIndex]):
			self._swapArrayPositions(parentIndex, index)
			index = parentIndex
			parentIndex = self.parent(index)

	###################
	# Private Methods #
	###################

	def __setHeapType(self, heapType):
		self.__heapType = heapType
		if self.__heapType == 'max':
			self.__floatOperator = operator.gt
		elif self.__heapType == 'min':
			self.__floatOperator = operator.lt
		else:
			raise Exception('Invalid heapType specified: %s' % (self.__heapType))

	def __resetArrayLength(self):
		self.__arrayLen = len(self)

