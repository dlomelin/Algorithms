from algorithms.PriorityQueue import PriorityQueueMin
from algorithms.dataStructures.Node import Node

class Huffman(object):
    def __init__(self, dataList):
        self.__createCode(dataList)
        self.__createEncodeData()

    ##################
    # Public Methods #
    ##################

    # Converts a bitstring into a normal string.
    # Ex: 001011101 -> aabe
    def decode(self, bitString):
        decodedList = []

        # Set the node to the tree's root node
        currentNode = self.__code
        for char in bitString:
            # Grab the left or right node depending on the bit
            if char == '0':
                currentNode = currentNode.left()
            else:
                currentNode = currentNode.right()

            # Get the current node value.
            # If the node has a character assigned, then get the char value and
            # reset the current node back to the top of the tree.
            value = currentNode.value()
            if 'char' in value:
                decodedList.append(value['char'])
                # Reset the node to the tree's root node
                currentNode = self.__code

        # Concatenate the list and return it
        return ''.join(decodedList)

    def encode(self, charString):
        encodedList = []

        # Encode each character
        for char in charString:
            encodedList.append(self.__encodeData[char])

        # Concatenate the list and return it
        return ''.join(encodedList)

    ###################
    # Private Methods #
    ###################

    # Creates a tree where going left = 0, right = 1.  The concatenation of these
    # bits gives the code for the leaf node's "char".
    def __createCode(self, dataList):

        listLength = len(dataList)

        pqmObj = PriorityQueueMin(array=dataList, key=lambda x: x.value()['freq'])

        # A tree with listLength leaves has listLength-1 nodes
        for i in range(listLength-1):

            # Extract the top 2 nodes with the min values
            leftMin = pqmObj.extractTopQueue()
            rightMin = pqmObj.extractTopQueue()

            # Add the left and right node frequencies as the new frequency
            # and create a new node.
            newFreq = leftMin.value()['freq'] + rightMin.value()['freq']
            node = Node({'freq': newFreq}, lNode=leftMin, rNode=rightMin)

            # Add this new node back into the priority queue
            pqmObj.insert(node)

        # Sets the root of the tree as the code
        self.__code = pqmObj.extractTopQueue()

    def __createEncodeData(self):
        self.__encodeData = {}

        node = self.__code
        self.__iterateNode(node, '')

    def __iterateNode(self, node, encodeString):
        value = node.value()
        if 'char' in value:
            self.__encodeData[value['char']] = encodeString
        else:
            self.__iterateNode(node.left(), '%s%s' % (encodeString, '0'))
            self.__iterateNode(node.right(), '%s%s' % (encodeString, '1'))
