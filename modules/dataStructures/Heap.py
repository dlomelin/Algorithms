import sys, operator

class Heap(object):
	def __init__(self, array = [], heapType = 'max', key = lambda x: x):
		self.__array = array
		self.__setHeapType(heapType)
		self.__key = key

		self.__buildHeap()

	# Unheaps the internal array and sorts it in ascending or descending
	# order depending on the heapType
	def sort(self):
		for i in xrange(self.__arrayLength() - 1, 0, -1):
			self.__swapArrayPositions(0, i)
			self.__reduceArrayLength()
			self.__floatDownHeap(0)

	# Adds a new element to the heap
	def insert(self, value):
		self.__increaseArrayLength()
		try:
			self[self.__arrayLength() - 1] = value
		except:
			self.__array.append(value)

		self.__floatUpHeap(self.__arrayLength() - 1)

	# Returns the top most element of the heap (max value for max heaps, min value for min heaps)
	def topHeap(self):
		return self[0]

	# Removes and returns the top most element of the heap
	def extractTopHeap(self):
		arrayLen = self.__arrayLength()
		if arrayLen == 0:
			return None

		# Get the element at the top of the queue
		tq = self.topHeap()

		self.__swapArrayPositions(0, self.__arrayLength()-1)
		self.__reduceArrayLength()
		self.__floatDownHeap(0)

		return tq

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

	def _parent(self, index):
		pIndex = (index - 1) / 2
		if pIndex < 0:
			pIndex = None
		return pIndex

	def _left(self, index):
		lIndex = 2*index + 1
		if lIndex >= self.__arrayLength():
			lIndex = None
		return lIndex

	def _right(self, index):
		rIndex = 2*index + 2
		if rIndex >= self.__arrayLength():
			rIndex = None
		return rIndex

	###################
	# Private Methods #
	###################

	def __arrayLength(self):
		return self.__arrayLen

	def __reduceArrayLength(self):
		self.__arrayLen -= 1

	def __increaseArrayLength(self):
		self.__arrayLen += 1

	def __resetArrayLength(self):
		self.__arrayLen = len(self)

	def __swapArrayPositions(self, idx1, idx2):
		self.__array[idx1], self.__array[idx2] = self.__array[idx2], self.__array[idx1]

	def __floatDownHeap(self, index):

		leftIndex = self._left(index)
		rightIndex = self._right(index)

		# Between the starting node and its left and right nodes, determine which one
		# has the largest(if max heap) or lowest(if min heap) value and store its
		# index position.
		if not leftIndex is None and self.__floatOperator(self.__cmpValue(leftIndex), self.__cmpValue(index)):
			switchIndex = leftIndex
		else:
			switchIndex = index

		if not rightIndex is None and self.__floatOperator(self.__cmpValue(rightIndex), self.__cmpValue(switchIndex)):
			switchIndex = rightIndex

		# If the largest value is not the current index, then swap the switch index
		# value with the current index position and repeat.  Otherwise terminate.
		if switchIndex != index:
			self.__swapArrayPositions(switchIndex, index)
			self.__floatDownHeap(switchIndex)

	def __floatUpHeap(self, index):

		parentIndex = self._parent(index)

		while index > 0 and self.__floatOperator(self.__cmpValue(index), self.__cmpValue(parentIndex)):
			self.__swapArrayPositions(parentIndex, index)
			index = parentIndex
			parentIndex = self._parent(index)

	# Create a heap where all nodes below any given node have smaller values
	def __buildHeap(self):
		self.__resetArrayLength()

		# Iterate through all non leaf nodes and float down all values.
		# Start with the nodes that are furthest down first.
		for i in xrange(self.__arrayLength()/2 - 1, -1, -1):
			self.__floatDownHeap(i)

	def __cmpValue(self, index):
		return self.__key(self[index])

	def __setHeapType(self, heapType):
		self.__heapType = heapType
		if self.__heapType == 'max':
			self.__floatOperator = operator.gt
		elif self.__heapType == 'min':
			self.__floatOperator = operator.lt
		else:
			raise Exception('Invalid heapType specified: %s' % (self.__heapType))

