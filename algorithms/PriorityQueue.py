'''.'''

from algorithms.data_structures.Heap import Heap


class PriorityQueue(Heap):
    ''' Implements a priority queue data structure for maximum values '''

    def top_queue(self):
        '''
        Returns the top most element of the queue.
        (max value for max queues, min value for min queues)

        :param:  None

        :return:  Various - The element at the top of the queue
        '''
        return self.top_heap()

    def extract_top_queue(self):
        '''
        Removes and returns the top most element of the queue

        :param:  None

        :return:  Various - The element at the top of the queue
        '''
        return self.extract_top_heap()


class PriorityQueueMax(PriorityQueue):
    ''' Implements a priority queue data structure for maximum values '''

    def __init__(self, array=None, key=lambda x: x):
        if array is None:
            array = []
        super(PriorityQueueMax, self).__init__(array=array, heap_type='max', key=key)


class PriorityQueueMin(PriorityQueue):
    ''' Implements a priority queue data structure for minimum values '''

    def __init__(self, array=None, key=lambda x: x):
        if array is None:
            array = []
        super(PriorityQueueMin, self).__init__(array=array, heap_type='min', key=key)
