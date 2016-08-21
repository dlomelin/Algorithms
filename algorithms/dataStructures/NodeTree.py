# IMPORTANT - Child classes that inherit from NodeTree must set up
# their own __iter__ method to iterate over each node in order for
# the rest of the NodeTree methods work correctly

class NodeTree(object):
    def __init__(self, key = lambda x: x):
        # Initialize empty root
        self._setRoot()

        self.__key = key

    ########################
    # Operator Overloading #
    ########################

    # for node in self:
    # Default behavior assumes singly linked list that starts at the root,
    # and then keeps going right until there are no more nodes.
    def __iter__(self):

        node = self.root()

        while not node is None:
            yield node
            node = node.right()

    # if x in self:
    def __contains__(self, value):
        if self.search(value) is None:
            return False
        else:
            return True

    # print self
    def __str__(self):
        return ' -> '.join(str(self._nodeKey(node)) for node in self)

    ##################
    # Public Methods #
    ##################

    # Searches for and returns the node that matches the specified value
    # Works just like __contains__ except it returns the node
    def search(self, value):
        node = None

        # Check each node until it finds the one with the specified value
        for tNode in self:
            if self._nodeKey(tNode) == value:
                node = tNode
                break

        return node

    def root(self):
        return self.__root

    ########################
    # Semi-private Methods #
    ########################

    def _setRoot(self, value = None):
        self.__root = value

    def _nodeKey(self, node):
        return self.__key(node.value())

