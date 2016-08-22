'''.'''

from algorithms.data_structures.mixins.EqualityMixin import EqualityMixin


class BinaryTree(EqualityMixin):  # pylint: disable=too-few-public-methods
    ''' BinaryTree data structure '''

    def __init__(self, array=None, key=lambda x: x):
        if array is None:
            array = []
        self.__array = array
        self.__key = key

        self._set_array_length(len(self))

    ########################
    # Operator Overloading #
    ########################

    def __iter__(self):
        for i in range(self._array_length()):
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

    @staticmethod
    def _parent(index):
        p_index = (index - 1) / 2
        if p_index < 0:
            p_index = None
        return p_index

    def _left(self, index):
        l_index = 2*index + 1
        if l_index >= self._array_length():
            l_index = None
        return l_index

    def _right(self, index):
        r_index = 2*index + 2
        if r_index >= self._array_length():
            r_index = None
        return r_index

    def _root(self):
        return self[0]

    def _cmp_value(self, index):
        return self.__key(self[index])

    # Array modification methods
    def _swap_array_positions(self, idx1, idx2):
        self.__array[idx1], self.__array[idx2] = self.__array[idx2], self.__array[idx1]
    def _array_set(self, index, value):
        self.__array[index] = value

    def _array_append(self, value):
        self.__array.append(value)

    # Array length modification methods
    def _array_length(self):
        return self.__array_len
    def _decrease_array_length(self):
        self.__array_len -= 1
    def _increase_array_length(self):
        self.__array_len += 1
    def _set_array_length(self, value):
        self.__array_len = value
