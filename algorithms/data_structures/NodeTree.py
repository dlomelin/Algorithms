'''
IMPORTANT - Child classes that inherit from NodeTree must set up
their own __iter__ method to iterate over each node in order for
the rest of the NodeTree methods to work correctly.
'''


class NodeTree(object):
    '''
    Creates a tree of Node objects
    '''

    def __init__(self, key=lambda x: x):
        # Initialize empty root
        self._set_root()

        # Function that returns the value of a node
        # Default key assumes the value is a standard python object (int, str, etc)
        self.__key = key

    ########################
    # Operator Overloading #
    ########################

    def __iter__(self):
        '''
        for node in self:

        Default behavior assumes singly linked list that starts at the root,
        and then keeps going right until there are no more nodes.
        '''

        node = self.root()

        while node is not None:
            yield node
            node = node.right()

    def __contains__(self, value):
        '''
        if x in self:
        '''
        return self.search(value) is not None

    def __str__(self):
        '''
        print self
        '''
        return ' -> '.join(str(self._node_key(node)) for node in self)

    ##################
    # Public Methods #
    ##################

    def search(self, value):
        '''
        Searches for and returns the node that matches the specified value
        Works just like __contains__ except it returns the node

        :param value:  Various - The value of a Node

        :return:  Node - Instance of a Node class
        '''
        node = None

        # Check each node until it finds the one with the specified value
        for tnode in self:
            if self._node_key(tnode) == value:
                node = tnode
                break

        return node

    def root(self):
        '''
        Returns the node of the root of the tree

        :param:  None

        :return:  Node - Instance of a Node class
        '''
        return self.__root

    ########################
    # Semi-private Methods #
    ########################

    def _set_root(self, value=None):
        '''
        Assigns the root node.

        :param value:  Node - Instance of a Node class

        :return:  None
        '''
        self.__root = value

    def _node_key(self, node):
        '''
        Returns the value of the node.  Set key in the constructor to modify return value
        if the default node value is complex, eg, an object

        :param node:  Node - Instance of a Node class

        :return:  Various - The value of the node
        '''
        return self.__key(node.value())
