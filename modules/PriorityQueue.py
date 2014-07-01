from Algorithms.modules.dataStructures.Heap import Heap

class PriorityQueue(Heap):

	def topQueue(self):
		return self[0]

	def extractTopQueue(self):
		arrayLen = self._arrayLength()
		if arrayLen == 0:
			return None

		# Get the element at the top of the queue
		tq = self.topQueue()

		self._swapArrayPositions(0, self._arrayLength()-1)
		self._reduceArrayLength()
		self._floatDownHeap(0)

		return tq

class PriorityQueueMax(PriorityQueue):
	def __init__(self, array = []):
		super(PriorityQueueMax, self).__init__(array = array, heapType = 'max')

class PriorityQueueMin(PriorityQueue):
	def __init__(self, array = []):
		super(PriorityQueueMin, self).__init__(array = array, heapType = 'min')
