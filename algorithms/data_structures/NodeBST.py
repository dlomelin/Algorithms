'''.'''

from algorithms.data_structures.Node import Node


class NodeBST(Node):
    '''
    This node class should be used with the BinarySearchTree class
    '''

    def minimum(self):
        '''
        Finds the node with the minimum value relative to the current node

        :param:  None

        :return:  Node - Instance of a Node class
        '''
        min_node = self
        while min_node is not None and min_node.left() is not None:
            min_node = min_node.left()

        return min_node

    def maximum(self):
        '''
        Finds the node with the maximum value relative to the current node

        :param:  None

        :return:  Node - Instance of a Node class
        '''
        max_node = self
        while max_node is not None and max_node.right() is not None:
            max_node = max_node.right()

        return max_node

    def successor(self):
        '''
        Finds the node with the smallest value greater than the current node

        :param:  None

        :return:  Node - Instance of a Node class
        '''

        # Simplest case scenario when the right tree is non empty
        if not self.right() is None:
            return self.right().minimum()

        parent_node = self.parent()
        right_child = self

        # Keep iteratively finding the current node's parent until the
        # parent's right child is not the previous parent.
        while parent_node is not None and right_child == parent_node.right():
            right_child = parent_node
            parent_node = parent_node.parent()

        return parent_node
