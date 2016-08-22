'''.'''

from algorithms.data_structures.NodeTree import NodeTree


class BinarySearchTree(NodeTree):
    ''' BinarySearchTree data structure '''

    ########################
    # Operator Overloading #
    ########################

    # for node in self:
    def __iter__(self):
        root_node = self.root()

        for node in self.__tree_iter(root_node):
            yield node

    ##################
    # Public Methods #
    ##################

    def insert(self, insert_node):
        '''
        Inserts a node into the BinarySearchTree

        :param insert_node:  Node - Instance of a Node class

        :return:  None
        '''
        parent_node = None
        test_node = self.root()

        # Iterate down the tree of nodes until it finds a node that has an
        # empty slot for the current insert node
        while test_node is not None:
            parent_node = test_node
            if self._node_key(insert_node) < self._node_key(test_node):
                test_node = test_node.left()
            else:
                test_node = test_node.right()

        # Set the insert node's parent to the node that had an empty slot
        insert_node.set_parent(parent_node)

        if parent_node is None:
            # Tree was empty, set root node
            self._set_root(insert_node)
        else:
            # Place the insert node as a child of the parent node in its correct position
            if self._node_key(insert_node) < self._node_key(parent_node):
                parent_node.set_left(insert_node)
            else:
                parent_node.set_right(insert_node)

    def delete(self, node):
        '''
        Delete the node that was passed in from the tree
        1) If node has no children, just remove it
        2) If node has 1 child, just make that child replace the location of the node
        3) If node has 2 children, find the successor node and place its data into that
           of the node.  Also reattach the successor node's children to its parent node.

        :param node:  Node - Instance of a Node class

        :return:  None
        '''

        # Determine the node to splice out.  If the current node has 2 children then
        # use the sucessor node.  Otherwise use the current node.
        if node.left() is None or node.right() is None:
            splice_node = node
        else:
            splice_node = node.successor()

        # Find a child node of the splice node that is not empty.  This node will be empty
        # only for a node without children.
        if not splice_node.left() is None:
            splice_child = splice_node.left()
        else:
            splice_child = splice_node.right()

        # Change the child's parent to the parent of the splice_node
        if splice_child is not None:
            splice_child.set_parent(splice_node.parent())

        splice_node_parent = splice_node.parent()
        if splice_node_parent is None:
            # If splice_node was the root, then set the root to the splice_child
            self._set_root(splice_child)
        else:
            # Move the splice_node's child node to connect to the splice_node's parent node
            if splice_node == splice_node_parent.left():
                splice_node_parent.set_left(splice_child)
            else:
                splice_node_parent.set_right(splice_child)

        # Copy the contents of the splice_node into the original node
        # This will only occur for nodes with 2 children
        if splice_node != node:
            node.set_value(splice_node.value())

    def search(self, value):
        '''
        Finds the node with the specified value in the entire tree

        :param value:  Various - The value of a node

        :return:  Node - Instance of a Node class
        '''
        node = self.root()

        while node is not None and value != self._node_key(node):
            if value < self._node_key(node):
                node = node.left()
            else:
                node = node.right()

        return node

    def minimum(self):
        '''
        Finds the node with the minimum value in the entire tree

        :param:  None

        :return:  Node - Instance of a Node class
        '''
        node = self.root()

        if node is not None:
            return node.minimum()
        else:
            return node

    def maximum(self):
        '''
        Finds the node with the maximum value in the entire tree

        :param:  None

        :return:  Node - Instance of a Node class
        '''
        node = self.root()

        if node is not None:
            return node.maximum()
        else:
            return node

    ###################
    # Private Methods #
    ###################

    # Recursive iterator that walks through each node in order
    def __tree_iter(self, node):
        if node is not None:
            for l_node in self.__tree_iter(node.left()):
                yield l_node
            yield node
            for r_node in self.__tree_iter(node.right()):
                yield r_node
