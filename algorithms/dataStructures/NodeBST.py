from algorithms.dataStructures.Node import Node

# This node class should be used with the BinarySearchTree class
class NodeBST(Node):

    # Finds the node with the minimum value relative to the current node
    def minimum(self):
        minNode = self
        while not minNode is None and not minNode.left() is None:
            minNode = minNode.left()

        return minNode

    # Finds the node with the maximum value relative to the current node
    def maximum(self):
        maxNode = self
        while not maxNode is None and not maxNode.right() is None:
            maxNode = maxNode.right()

        return maxNode

    # Finds the node with the smallest value greater than the current node
    def successor(self):

        # Simplest case scenario when the right tree is non empty
        if not self.right() is None:
            return self.right().minimum()

        parentNode = self.parent()
        rightChild = self

        # Keep iteratively finding the current node's parent until the
        # parent's right child is not the previous parent.
        while not parentNode is None and rightChild == parentNode.right():
            rightChild = parentNode
            parentNode = parentNode.parent()

        return parentNode
