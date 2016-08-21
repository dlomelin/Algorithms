from algorithms.dataStructures.Heap import Heap

class PriorityQueue(Heap):

    def topQueue(self):
        return self.topHeap()

    def extractTopQueue(self):
        return self.extractTopHeap()

class PriorityQueueMax(PriorityQueue):
    def __init__(self, array=[], key=lambda x: x):
        super(PriorityQueueMax, self).__init__(array=array, heapType='max', key=key)

class PriorityQueueMin(PriorityQueue):
    def __init__(self, array=[], key=lambda x: x):
        super(PriorityQueueMin, self).__init__(array=array, heapType='min', key=key)
