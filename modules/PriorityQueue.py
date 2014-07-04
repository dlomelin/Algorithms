from Algorithms.modules.dataStructures.Heap import Heap

class PriorityQueue(Heap):

	def topQueue(self):
		return self.topHeap()

	def extractTopQueue(self):
		return self.extractTopHeap()

class PriorityQueueMax(PriorityQueue):
	def __init__(self, array = []):
		super(PriorityQueueMax, self).__init__(array = array, heapType = 'max')

class PriorityQueueMin(PriorityQueue):
	def __init__(self, array = []):
		super(PriorityQueueMin, self).__init__(array = array, heapType = 'min')
