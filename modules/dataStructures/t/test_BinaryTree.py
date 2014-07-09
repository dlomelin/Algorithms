import unittest
from Algorithms.modules.dataStructures.BinaryTree import BinaryTree

class TestBinaryTree(unittest.TestCase):
	def setUp(self):
		self.array = [16, 14, 9, 10, 7, 8, 3, 1, 4, 2]
		self.btObj = BinaryTree(self.array)

	def test_nodes1(self):
		index = 3

		parent = self.btObj._parent(index)
		left = self.btObj._left(index)
		right = self.btObj._right(index)

		self.assertEqual(parent, 1)
		self.assertEqual(left, 7)
		self.assertEqual(right, 8)

	def test_nodes2(self):
		index = 4

		parent = self.btObj._parent(index)
		left = self.btObj._left(index)
		right = self.btObj._right(index)

		self.assertEqual(parent, 1)
		self.assertEqual(left, 9)
		self.assertEqual(right, None)

	def test_nodes3(self):
		index = 5

		parent = self.btObj._parent(index)
		left = self.btObj._left(index)
		right = self.btObj._right(index)

		self.assertEqual(parent, 2)
		self.assertEqual(left, None)
		self.assertEqual(right, None)

	def test_nodes4(self):
		index = 0

		parent = self.btObj._parent(index)
		left = self.btObj._left(index)
		right = self.btObj._right(index)

		self.assertEqual(parent, None)
		self.assertEqual(left, 1)
		self.assertEqual(right, 2)

if __name__ == '__main__':
	unittest.main()
