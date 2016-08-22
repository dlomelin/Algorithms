import unittest
from algorithms.data_structures.Node import Node
from algorithms.data_structures.NodeBST import NodeBST


class TestNode(unittest.TestCase):
    def setUp(self):
        self.node1 = Node(3)
        self.node2 = Node(3)
        self.node3 = Node(33)

        self.nodeB1 = NodeBST(3)
        self.nodeB2 = NodeBST(3)
        self.nodeB3 = NodeBST(33)

    def test_string(self):
        str(self.node1)

    def test_set_parent_exception1(self):
        # Make sure exception is raised when node types don't match
        with self.assertRaises(Exception):
            self.node1.set_parent(self.nodeB1)

    def test_set_parent_exception2(self):
        # Make sure exception is raised when node types don't match
        with self.assertRaises(Exception):
            self.nodeB1.set_parent(self.node1)

    def test_nodeEquality1(self):
        # Make sure 2 different objects with the same initialization parameters are equal
        self.assertEqual(self.node1, self.node2)

        # Make sure 2 different objects with different initialization parameters are not equal
        self.assertNotEqual(self.node1, self.node3)

    def test_nodeEquality2(self):
        # Make sure both nodes equal to each other
        self.assertEqual(self.node1, self.node2)

        # Modify one node
        self.node2.set_parent(self.node3)

        # Make sure they are no longer equal
        self.assertNotEqual(self.node1, self.node2)

        # Set back to original state
        self.node2.set_parent(None)

        # Make sure both nodes equal to each other
        self.assertEqual(self.node1, self.node2)

    def test_nodeBstEquality1(self):
        # Make sure 2 different objects with the same initialization parameters are equal
        self.assertEqual(self.nodeB1, self.nodeB2)

        # Make sure 2 different objects with different initialization parameters are not equal
        self.assertNotEqual(self.nodeB1, self.nodeB3)

    def test_nodeBstEquality2(self):
        # Make sure both nodes equal to each other
        self.assertEqual(self.nodeB1, self.nodeB2)

        # Modify one node
        self.nodeB2.set_parent(self.nodeB3)

        # Make sure they are no longer equal
        self.assertNotEqual(self.nodeB1, self.nodeB2)

        # Set back to original state
        self.nodeB2.set_parent(None)

        # Make sure both nodes equal to each other
        self.assertEqual(self.nodeB1, self.nodeB2)
