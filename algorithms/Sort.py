'''.'''

from algorithms.data_structures.Heap import Heap


def merge_sort(array):
    '''
    Executes merge sort algorithm on a list
    Small wrapper around __merge_sort to prevent user from having to specify bounds

    :param array:  List

    :return:  None
    '''
    __merge_sort(array, 0, len(array)-1)


def heap_sort(array):
    '''
    Executes heap sort algorithm on a list

    :param array:  List

    :return:  None
    '''
    heap = Heap(array)
    heap.sort()
    return list(heap)


def insertion_sort(array):
    '''
    Executes insertion sort algorithm on a list

    :param array:  List

    :return:  None
    '''

    # Iterate through each position except the first
    for i in xrange(1, len(array)):
        # Store the current value
        key = array[i]

        # Iterate through all previous values so long as they are greater
        # then the current value.  Swap both values
        j = i - 1
        while j >= 0 and array[j] > key:
            array[j+1] = array[j]
            j -= 1
        array[j+1] = key


def selection_sort(array):
    '''
    Executes selection sort algorithm on a list

    :param array:  List

    :return:  None
    '''
    array_len = len(array)

    # Iterate through each position except the last
    for i in xrange(array_len-1):

        # Look for the index position with the smallest possible value
        min_index = i
        for j in xrange(i+1, array_len):
            if array[j] < array[min_index]:
                min_index = j

        # Swap current element with min element
        array[i], array[min_index] = array[min_index], array[i]


def bubble_sort(array):
    '''
    Executes bubble sort algorithm on a list

    :param array:  List

    :return:  None
    '''
    array_len = len(array)

    # Iterate through each position
    for i in xrange(array_len):

        # Compare each position and swap elements to make the larger values
        # go higher in the index and the lowest value to the beginning
        for j in xrange(array_len-1, i, -1):
            if array[j] < array[j-1]:
                array[j], array[j-1] = array[j-1], array[j]

#####################
# Private Functions #
#####################


def __merge_sort(array, left, right):
    if left < right:
        mid = (left+right) / 2
        __merge_sort(array, left, mid)
        __merge_sort(array, mid+1, right)
        __merge(array, left, mid, right)


def __merge(array, left, mid, right):
    # Create left and right list based on left, mid, right
    l_list = array[left:mid+1]
    r_list = array[mid+1:right+1]

    # Append sentinel
    l_list.append(float('inf'))
    r_list.append(float('inf'))

    l_index = 0
    r_index = 0
    for i in xrange(left, right+1):
        if l_list[l_index] < r_list[r_index]:
            array[i] = l_list[l_index]
            l_index += 1
        else:
            array[i] = r_list[r_index]
            r_index += 1
