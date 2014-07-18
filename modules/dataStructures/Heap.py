import sys, operator
from Algorithms.modules.dataStructures.BinaryTree import BinaryTree

class Heap(BinaryTree):
	def __init__(self, array = [], heapType = 'max', key = lambda x: x):
		super(Heap, self).__init__(array = array, key = key)

		self.__setHeapType(heapType)
		self.__buildHeap()

	# Unheaps the internal array and sorts it in ascending or descending
	# order depending on the heapType
	def sort(self):
		for i in xrange(self._arrayLength() - 1, 0, -1):
			self._swapArrayPositions(0, i)
			self._decreaseArrayLength()
			self.__floatDownHeap(0)

	# Adds a new element to the heap
	def insert(self, value):
		self._increaseArrayLength()
		try:
			self[self._arrayLength() - 1] = value
		except:
			self._arrayAppend(value)

		self.__floatUpHeap(self._arrayLength() - 1)

	# Returns the top most element of the heap.
	# (max value for max heaps, min value for min heaps)
	def topHeap(self):
		return self._root()

	# Removes and returns the top most element of the heap
	def extractTopHeap(self):
		arrayLen = self._arrayLength()
		if arrayLen == 0:
			return None

		# Get the element at the top of the queue
		tq = self.topHeap()

		self._swapArrayPositions(0, self._arrayLength()-1)
		self._decreaseArrayLength()
		self.__floatDownHeap(0)

		return tq

	###################
	# Private Methods #
	###################

	def __floatDownHeap(self, index):

		leftIndex = self._left(index)
		rightIndex = self._right(index)

		# Between the starting node and its left and right nodes, determine which one
		# has the largest(if max heap) or lowest(if min heap) value and store its
		# index position.
		if not leftIndex is None and self.__floatOperator(self._cmpValue(leftIndex), self._cmpValue(index)):
			switchIndex = leftIndex
		else:
			switchIndex = index

		if not rightIndex is None and self.__floatOperator(self._cmpValue(rightIndex), self._cmpValue(switchIndex)):
			switchIndex = rightIndex

		# If the largest value is not the current index, then swap the switch index
		# value with the current index position and repeat.  Otherwise terminate.
		if switchIndex != index:
			self._swapArrayPositions(switchIndex, index)
			self.__floatDownHeap(switchIndex)

	def __floatUpHeap(self, index):

		parentIndex = self._parent(index)

		while index > 0 and self.__floatOperator(self._cmpValue(index), self._cmpValue(parentIndex)):
			self._swapArrayPositions(parentIndex, index)
			index = parentIndex
			parentIndex = self._parent(index)

	# Create a heap where all nodes below any given node have smaller values
	def __buildHeap(self):
		# Iterate through all non leaf nodes and float down all values.
		# Start with the nodes that are furthest down first.
		for i in xrange(self._arrayLength()/2 - 1, -1, -1):
			self.__floatDownHeap(i)

	def __setHeapType(self, heapType):
		self.__heapType = heapType
		if self.__heapType == 'max':
			self.__floatOperator = operator.gt
		elif self.__heapType == 'min':
			self.__floatOperator = operator.lt
		else:
			raise Exception('Invalid heapType specified: %s' % (self.__heapType))

