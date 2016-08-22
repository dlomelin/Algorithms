'''.'''

from algorithms.PriorityQueue import PriorityQueueMin
from algorithms.data_structures.Node import Node


class Huffman(object):
    ''' Implements Huffman coding algorithm '''

    def __init__(self, data_list):
        self.__create_code(data_list)
        self.__create_encode_data()

    ##################
    # Public Methods #
    ##################

    def decode(self, bit_string):
        '''
        Converts a bitstring into a normal string.  Ex: 001011101 -> aabe

        :param bit_string:  String - String of 0s and 1s

        :return:  String - Decoded string
        '''
        decoded_list = []

        # Set the node to the tree's root node
        current_node = self.__code
        for char in bit_string:
            # Grab the left or right node depending on the bit
            if char == '0':
                current_node = current_node.left()
            else:
                current_node = current_node.right()

            # Get the current node value.
            # If the node has a character assigned, then get the char value and
            # reset the current node back to the top of the tree.
            value = current_node.value()
            if 'char' in value:
                decoded_list.append(value['char'])
                # Reset the node to the tree's root node
                current_node = self.__code

        # Concatenate the list and return it
        return ''.join(decoded_list)

    def encode(self, char_string):
        '''
        Converts a bitstring into a normal string.  Ex: aabe -> 001011101

        :param char_string:  String - Decoded string

        :param:  String - String of 0s and 1s
        '''
        encoded_list = []

        # Encode each character
        for char in char_string:
            encoded_list.append(self.__encode_data[char])

        # Concatenate the list and return it
        return ''.join(encoded_list)

    ###################
    # Private Methods #
    ###################

    def __create_code(self, data_list):
        '''
        Creates a tree where going left = 0, right = 1.  The concatenation of these
        bits gives the code for the leaf node's "char".
        '''

        list_length = len(data_list)

        pqm_obj = PriorityQueueMin(array=data_list, key=lambda x: x.value()['freq'])

        # A tree with list_length leaves has list_length-1 nodes
        for _ in xrange(list_length-1):

            # Extract the top 2 nodes with the min values
            left_min = pqm_obj.extract_top_queue()
            right_min = pqm_obj.extract_top_queue()

            # Add the left and right node frequencies as the new frequency
            # and create a new node.
            new_freq = left_min.value()['freq'] + right_min.value()['freq']
            node = Node({'freq': new_freq}, l_node=left_min, r_node=right_min)

            # Add this new node back into the priority queue
            pqm_obj.insert(node)

        # Sets the root of the tree as the code
        self.__code = pqm_obj.extract_top_queue()

    def __create_encode_data(self):
        self.__encode_data = {}

        node = self.__code
        self.__iterate_node(node, '')

    def __iterate_node(self, node, encode_string):
        value = node.value()
        if 'char' in value:
            self.__encode_data[value['char']] = encode_string
        else:
            self.__iterate_node(node.left(), '%s%s' % (encode_string, '0'))
            self.__iterate_node(node.right(), '%s%s' % (encode_string, '1'))
