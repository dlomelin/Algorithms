'''.'''

from algorithms.data_structures.mixins.EqualityMixin import EqualityMixin


class Stack(EqualityMixin):
    '''
    Last-in, First-out (LIFO) data structure
    '''

    def __init__(self, array=None):
        if array is None:
            array = []
        self.__array = array
        self.__set_index(len(self.__array) - 1)

    ########################
    # Operator Overloading #
    ########################

    def __str__(self):
        # Calls __iter__ and converts to a string
        return str(list(self))

    def __len__(self):
        return self.__index() + 1

    def __iter__(self):
        for i in xrange(self.__index() + 1):
            yield self[i]

    def __getitem__(self, index):
        return self.__array[index]

    ##################
    # Public Methods #
    ##################

    def push(self, value):
        '''
        Adds an element to the stack

        :param value:  Various - Adds value to the stack

        :return:  None
        '''
        self.__increase_index()
        try:
            self[self.__index()] = value
        except TypeError:
            self.__array.append(value)

    def pop(self):
        '''
        Returns the element at the top of the stack

        :param:  None

        :return:  Various - An element that the user added to the stack
        '''
        if self.empty():
            return None
        else:
            self.__decrease_index()
            return self[self.__index() + 1]

    def multi_pop(self, count):
        '''
        Iterator that returns up to count elements from the stack

        :param count:  Integer - the number of elements that should be returned

        :yield:  Various - the next element in the stack
        '''
        while not self.empty() and count > 0:
            yield self.pop()
            count -= 1

    def empty(self):
        '''
        Returns a boolean value if the stack is empty

        :param:  None

        :return:  Boolean - If the stack is empty
        '''
        return self.__index() < 0

    ###################
    # Private Methods #
    ###################

    def __index(self):
        return self.__top_index
    def __set_index(self, value):
        self.__top_index = value
    def __increase_index(self):
        self.__top_index += 1
    def __decrease_index(self):
        self.__top_index -= 1
