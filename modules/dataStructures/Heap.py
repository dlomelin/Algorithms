import sys

class Heap(object):
	def __init__(self, array = []):
		self.__array = array
		self.__resetArrayLength()

	def sort(self):
		self.buildHeapMax()
		for i in xrange(self.__arrayLen - 1, 0, -1):
			self.__array[0], self.__array[i] = self.__array[i], self.__array[0]
			self.__reduceArrayLength()
			self.__floatDownHeap(0)

	def parent(self, index):
		pIndex = (index - 1) / 2
		if pIndex < 0:
			pIndex = None
		return pIndex

	def left(self, index):
		lIndex = 2*index + 1
		if lIndex >= self.__arrayLen:
			lIndex = None
		return lIndex

	def right(self, index):
		rIndex = 2*index + 2
		if rIndex >= self.__arrayLen:
			rIndex = None
		return rIndex

	# Create a heap where all nodes below any given node have smaller values
	def buildHeapMax(self):
		self.__resetArrayLength()

		# Iterate through all non leaf nodes and float down all values.
		# Start with the nodes that are furthest down first.
		for i in xrange(self.__arrayLen/2 - 1, -1, -1):
			self.__floatDownHeap(i)

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

	###################
	# Private Methods #
	###################

	def __floatDownHeap(self, index):

		leftIndex = self.left(index)
		rightIndex = self.right(index)

		# Between the starting node and its left and right nodes, determine which one
		# has the largest value and store its index position.
		if not leftIndex is None and self.__array[leftIndex] > self.__array[index]:
			largestIndex = leftIndex
		else:
			largestIndex = index

		if not rightIndex is None and self.__array[rightIndex] > self.__array[largestIndex]:
			largestIndex = rightIndex

		# If the largest value is not the current index, then swap the largest index
		# value with the current index position and repeat.  Otherwise terminate.
		if largestIndex != index:
			self.__array[largestIndex], self.__array[index] = self.__array[index], self.__array[largestIndex]
			self.__floatDownHeap(largestIndex)

	def __resetArrayLength(self):
		self.__arrayLen = len(self.__array)

	def __reduceArrayLength(self):
		self.__arrayLen -= 1
