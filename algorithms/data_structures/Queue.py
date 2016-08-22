'''.'''

from algorithms.data_structures.mixins.EqualityMixin import EqualityMixin


class Queue(EqualityMixin):
    '''
    First-in, First-out (FIFO)
    '''

    def __init__(self, array=None):
        # Allows default empty lists without keeping track of older initializations
        if array is None:
            array = []
        self.__array = array
        self.__set_indices()

    ########################
    # Operator Overloading #
    ########################

    def __str__(self):
        # Calls __iter__ and converts to a string
        return str(list(self))

    def __len__(self):
        return self.__tail() - self.__head()

    def __iter__(self):
        for i in xrange(self.__head(), self.__tail()):
            yield self[i]

    def __getitem__(self, index):
        return self.__array[index]

    ##################
    # Public Methods #
    ##################

    def enqueue(self, value):
        '''
        Adds an element to the queue

        :param value:  Various - Adds value to the queue

        :return:  None
        '''
        try:
            self[self.__tail()] = value
        except TypeError:
            self.__array.append(value)
        self.__increase_tail()

    def dequeue(self):
        '''
        Returns the element at the bottom of the queue

        :param:  None

        :return:  Various - An element that the user added to the queue
        '''
        if self.empty():
            return None
        else:
            self.__increase_head()
            return self[self.__head() - 1]

    def empty(self):
        '''
        Returns a boolean value if the queue is empty

        :param:  None

        :return:  Boolean - If the queue is empty
        '''
        return self.__head() == self.__tail()

    ###################
    # Private Methods #
    ###################

    def __set_indices(self):
        self.__set_head(0)
        self.__set_tail(len(self.__array))

    def __head(self):
        return self.__head_index

    def __set_head(self, value):
        self.__head_index = value  # pylint: disable=attribute-defined-outside-init

    def __increase_head(self):
        self.__head_index += 1

    def __tail(self):
        return self.__tail_index

    def __set_tail(self, value):
        self.__tail_index = value  # pylint: disable=attribute-defined-outside-init

    def __increase_tail(self):
        self.__tail_index += 1
