'''.'''

from algorithms.data_structures.mixins.EqualityMixin import EqualityMixin


class Node(EqualityMixin):
    '''
    Node objects that will be inserted into NodeTrees
    '''

    def __init__(self, value, p_node=None, l_node=None, r_node=None):
        self.set_value(value)

        self.set_parent(p_node)
        self.set_left(l_node)
        self.set_right(r_node)

    ########################
    # Operator Overloading #
    ########################

    def __repr__(self):
        return '%s(%s)' % (self.__class__.__name__, self.value())

    def __str__(self):
        try:
            l_val = self.left().value()
        except AttributeError:
            l_val = None

        try:
            r_val = self.right().value()
        except AttributeError:
            r_val = None

        try:
            p_val = self.parent().value()
        except AttributeError:
            p_val = None

        return '%s << %s (%s) >> %s' % (l_val, self.value(), p_val, r_val)

    ##################
    # Public Methods #
    ##################

    def value(self):
        '''
        Returns the value of the Node

        :param:  None

        :return:  Various - The value of the Node
        '''
        return self.__value

    def parent(self):
        '''
        Returns the parent Node

        :param:  None

        :return:  Node - Instance of a Node class
        '''
        return self.__parent

    def left(self):
        '''
        Returns the left Node

        :param:  None

        :return:  Node - Instance of a Node class
        '''
        return self.__left

    def right(self):
        '''
        Returns the right Node

        :param:  None

        :return:  Node - Instance of a Node class
        '''
        return self.__right

    def set_value(self, value):
        '''
        Assigns the value of the Node

        :param value:  Various - The value of the Node

        :return:  None
        '''
        self.__value = value

    def set_parent(self, node):
        '''
        Assigns the parent Node

        :param node:  Node - Instance of a Node class

        :return:  None
        '''
        self.__validate_node(node)
        self.__parent = node

    def set_left(self, node):
        '''
        Assigns the right Node

        :param node:  Node - Instance of a Node class

        :return:  None
        '''
        self.__validate_node(node)
        self.__left = node

    def set_right(self, node):
        '''
        Assigns the right Node

        :param node:  Node - Instance of a Node class

        :return:  None
        '''
        self.__validate_node(node)
        self.__right = node

    ###################
    # Private Methods #
    ###################

    def __validate_node(self, node):
        if node is not None and type(self) is not type(node):
            raise Exception(
                'Invalid node type passed as argument: %s.  Must be %s' % (
                    node.__class__.__name__,
                    self.__class__.__name__,
                )
            )
