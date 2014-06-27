import sys

class Heap(object):
	def __init__(self, array = []):
		self.__array = array
		self.__arrayLen = len(self.__array)

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

	def heapifyMax(self, index):
		leftIndex = self.left(index)
		rightIndex = self.right(index)

		if not leftIndex is None and self.__array[leftIndex] > self.__array[index]:
			largestIndex = leftIndex
		else:
			largestIndex = index

		if not rightIndex is None and self.__array[rightIndex] > self.__array[largestIndex]:
			largestIndex = rightIndex

		if largestIndex != index:
			self.__array[largestIndex], self.__array[index] = self.__array[index], self.__array[largestIndex]
			self.heapifyMax(largestIndex)

	########################
	# Operator Overloading #
	########################

	def __str__(self):
		return str(self.__array)

	def __len__(self):
		return len(self.__array)

	def __getitem__(self, index):
		return self.__array[index]
