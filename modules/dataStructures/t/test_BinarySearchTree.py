import unittest
from Algorithms.modules.dataStructures.BinarySearchTree import BinarySearchTree
from Algorithms.modules.dataStructures.Node import Node

class TestBinarySearchTree(unittest.TestCase):
	def setUp(self):
		self.bstObj = BinarySearchTree()

	def test_min(self):
		# Load standard data
		self.__loadData()

		tMin = self.bstObj.minimum()
		self.assertEqual(tMin.value(), 2)

	def test_minNone(self):
		tMin = self.bstObj.minimum()
		self.assertTrue(tMin is None)

	def test_max(self):
		# Load standard data
		self.__loadData()

		tMax = self.bstObj.maximum()
		self.assertEqual(tMax.value(), 20)

	def test_maxNone(self):
		tMax = self.bstObj.maximum()
		self.assertTrue(tMax is None)

	def test_search1(self):
		# Load standard data
		self.__loadData()

		searchValue = 13

		node = self.bstObj.search(searchValue)
		self.assertEqual(node.value(), searchValue)

	def test_search2(self):
		# Load standard data
		self.__loadData()

		searchValue = 66
		node = self.bstObj.search(searchValue)
		self.assertTrue(node is None)

	###################
	# Private Methods #
	###################

	def __loadData(self):
		for i in [15, 6, 18, 3, 7, 17, 20, 2, 4, 13, 9]:
			self.bstObj.insert(Node(i))

if __name__ == '__main__':
	unittest.main()
