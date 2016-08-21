import sys, operator
from algorithms.dataStructures.mixins.EqualityMixin import EqualityMixin

class BinaryTree(EqualityMixin):
    def __init__(self, array=[], key=lambda x: x):
        self.__array = array
        self.__key = key

        self._setArrayLength(len(self))

    ########################
    # Operator Overloading #
    ########################

    def __iter__(self):
        for i in range(self._arrayLength()):
            yield self[i]

    def __str__(self):
        return str(self.__array)

    def __len__(self):
        return len(self.__array)

    def __getitem__(self, index):
        return self.__array[index]

    ########################
    # Semi-Private Methods #
    ########################
    # These methods provide functionality for the binary tree but should
    # not be exposed to the user.

    def _parent(self, index):
        pIndex = (index - 1) / 2
        if pIndex < 0:
            pIndex = None
        return pIndex

    def _left(self, index):
        lIndex = 2*index + 1
        if lIndex >= self._arrayLength():
            lIndex = None
        return lIndex

    def _right(self, index):
        rIndex = 2*index + 2
        if rIndex >= self._arrayLength():
            rIndex = None
        return rIndex

    def _root(self):
        try:
            return self[0]
        except:
            return None

    def _cmpValue(self, index):
        return self.__key(self[index])

    # Array modification methods
    def _swapArrayPositions(self, idx1, idx2):
        self.__array[idx1], self.__array[idx2] = self.__array[idx2], self.__array[idx1]
    def _arraySet(self, index, value):
        self.__array[index] = value

    def _arrayAppend(self, value):
        self.__array.append(value)

    # Array length modification methods
    def _arrayLength(self):
        return self.__arrayLen
    def _decreaseArrayLength(self):
        self.__arrayLen -= 1
    def _increaseArrayLength(self):
        self.__arrayLen += 1
    def _setArrayLength(self, value):
        self.__arrayLen = value
