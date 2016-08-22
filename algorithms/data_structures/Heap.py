'''.'''

import operator
from algorithms.data_structures.BinaryTree import BinaryTree


class Heap(BinaryTree):
    ''' Heap data structure '''

    def __init__(self, array=None, heap_type='max', key=lambda x: x):
        if array is None:
            array = []
        super(Heap, self).__init__(array=array, key=key)

        self.__set_heap_type(heap_type)
        self.__build_heap()

    def sort(self):
        '''
        Unheaps the internal array and sorts it in ascending or descending
        order depending on the heap_type

        :param:  None

        :return:  None
        '''
        start_length = self._array_length()
        for i in xrange(start_length - 1, 0, -1):
            self._swap_array_positions(0, i)
            self._decrease_array_length()
            self.__float_down_heap(0)
        # Sets the array length back to its original size so that the
        # object can be iterated over.  This is to compensate for all the
        # _decrease_array_length() calls.
        self._set_array_length(start_length)

    def insert(self, value):
        '''
        Adds a new element to the heap

        :param value:  Various - Any python object (string, int, float, object, etc)

        :return:  None
        '''
        self._increase_array_length()
        try:
            self._array_set(self._array_length() - 1, value)
        except IndexError:
            self._array_append(value)

        self.__float_up_heap(self._array_length() - 1)

    def top_heap(self):
        '''
        Returns the top most element of the heap.
        (max value for max heaps, min value for min heaps)

        :param:  None

        :return:  Various - The element at the top of the heap
        '''
        return self._root()

    def extract_top_heap(self):
        '''
        Removes and returns the top most element of the heap

        :param:  None

        :return:  Various - The element at the top of the heap
        '''
        array_len = self._array_length()
        if array_len == 0:
            return None

        # Get the element at the top of the queue
        top_element = self.top_heap()

        self._swap_array_positions(0, self._array_length()-1)
        self._decrease_array_length()
        self.__float_down_heap(0)

        return top_element

    ###################
    # Private Methods #
    ###################

    def __float_down_heap(self, index):

        left_index = self._left(index)
        right_index = self._right(index)

        # Between the starting node and its left and right nodes, determine which one
        # has the largest(if max heap) or lowest(if min heap) value and store its
        # index position.
        if not left_index is None and \
            self.__float_operator(self._cmp_value(left_index), self._cmp_value(index)):
            switch_index = left_index
        else:
            switch_index = index

        if not right_index is None and \
            self.__float_operator(self._cmp_value(right_index), self._cmp_value(switch_index)):
            switch_index = right_index

        # If the largest value is not the current index, then swap the switch index
        # value with the current index position and repeat.  Otherwise terminate.
        if switch_index != index:
            self._swap_array_positions(switch_index, index)
            self.__float_down_heap(switch_index)

    def __float_up_heap(self, index):

        parent_index = self._parent(index)

        while index > 0 and \
            self.__float_operator(self._cmp_value(index), self._cmp_value(parent_index)):
            self._swap_array_positions(parent_index, index)
            index = parent_index
            parent_index = self._parent(index)

    # Create a heap where all nodes below any given node have smaller values
    def __build_heap(self):
        # Iterate through all non leaf nodes and float down all values.
        # Start with the nodes that are furthest down first.
        for i in xrange(self._array_length()/2 - 1, -1, -1):
            self.__float_down_heap(i)

    def __set_heap_type(self, heap_type):
        self.__heap_type = heap_type
        if self.__heap_type == 'max':
            self.__float_operator = operator.gt
        elif self.__heap_type == 'min':
            self.__float_operator = operator.lt
        else:
            raise Exception('Invalid heap_type specified: %s' % (self.__heap_type))
