from algorithms.dataStructures.NodeTree import NodeTree

class BinarySearchTree(NodeTree):

    ########################
    # Operator Overloading #
    ########################

    # for node in self:
    def __iter__(self):
        rootNode = self.root()

        for node in self.__treeIter(rootNode):
            yield node

    ##################
    # Public Methods #
    ##################

    def insert(self, insertNode):

        parentNode = None
        testNode = self.root()

        # Iterate down the tree of nodes until it finds a node that has an
        # empty slot for the current insert node
        while not testNode is None:
            parentNode = testNode
            if self._nodeKey(insertNode) < self._nodeKey(testNode):
                testNode = testNode.left()
            else:
                testNode = testNode.right()

        # Set the insert node's parent to the node that had an empty slot
        insertNode.setParent(parentNode)

        if parentNode is None:
            # Tree was empty, set root node
            self._setRoot(insertNode)
        else:
            # Place the insert node as a child of the parent node in its correct position
            if self._nodeKey(insertNode) < self._nodeKey(parentNode):
                parentNode.setLeft(insertNode)
            else:
                parentNode.setRight(insertNode)

    # Delete the node that was passed in from the tree
    # 1) If node has no children, just remove it
    # 2) If node has 1 child, just make that child replace the location of the node
    # 3) If node has 2 children, find the successor node and place its data into that
    #    of the node.  Also reattach the successor node's children to its parent node.
    def delete(self, node):

        # Determine the node to splice out.  If the current node has 2 children then
        # use the sucessor node.  Otherwise use the current node.
        if node.left() is None or node.right() is None:
            spliceNode = node
        else:
            spliceNode = node.successor()

        # Find a child node of the splice node that is not empty.  This node will be empty
        # only for a node without children.
        if not spliceNode.left() is None:
            spliceChild = spliceNode.left()
        else:
            spliceChild = spliceNode.right()

        # Change the child's parent to the parent of the spliceNode
        if not spliceChild is None:
            spliceChild.setParent(spliceNode.parent())

        spliceNodeParent = spliceNode.parent()
        if spliceNodeParent is None:
            # If spliceNode was the root, then set the root to the spliceChild
            self._setRoot(spliceChild)
        else:
            # Move the spliceNode's child node to connect to the spliceNode's parent node
            if spliceNode == spliceNodeParent.left():
                spliceNodeParent.setLeft(spliceChild)
            else:
                spliceNodeParent.setRight(spliceChild)

        # Copy the contents of the spliceNode into the original node
        # This will only occur for nodes with 2 children
        if spliceNode != node:
            node.setValue(spliceNode.value())

    # Finds the node with the specified value in the entire tree
    def search(self, value):
        node = self.root()

        while not node is None and value != self._nodeKey(node):
            if value < self._nodeKey(node):
                node = node.left()
            else:
                node = node.right()

        return node

    # Finds the node with the minimum value in the entire tree
    def minimum(self):
        node = self.root()

        if not node is None:
            return node.minimum()
        else:
            return node

    # Finds the node with the maximum value in the entire tree
    def maximum(self):
        node = self.root()

        if not node is None:
            return node.maximum()
        else:
            return node

    ###################
    # Private Methods #
    ###################

    # Recursive iterator that walks through each node in order
    def __treeIter(self, node):
        if not node is None:
            for lNode in self.__treeIter(node.left()):
                yield lNode
            yield node
            for rNode in self.__treeIter(node.right()):
                yield rNode

