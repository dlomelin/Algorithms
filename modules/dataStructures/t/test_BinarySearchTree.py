import unittest
from Algorithms.modules.dataStructures.BinarySearchTree import BinarySearchTree
from Algorithms.modules.dataStructures.NodeBST import NodeBST

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

	def test_successor1(self):
		# Load standard data
		self.__loadData()

		searchValue = 15
		node = self.bstObj.search(searchValue)

		successorNode = node.successor()
		self.assertEqual(successorNode.value(), 17)

	def test_successor2(self):
		# Load standard data
		self.__loadData()

		searchValue = 13
		node = self.bstObj.search(searchValue)

		successorNode = node.successor()
		self.assertEqual(successorNode.value(), 15)

	def test_delete1(self):
		# Load standard data
		self.__loadDeleteData()

		# Delete and validate the tree is correct after deletion
		self.__deleteNode(13)

	def test_delete2(self):
		# Load standard data
		self.__loadDeleteData()

		# Delete and validate the tree is correct after deletion
		self.__deleteNode(16)

	def test_delete3(self):
		# Load standard data
		self.__loadDeleteData()

		# Delete and validate the tree is correct after deletion
		self.__deleteNode(5)

	def test_deleteAll(self):
		# Load standard data
		self.__loadDeleteData()

		# Delete and validate the tree is correct after deletion of each node
		for i in self.__deleteIter():
			self.__deleteNode(i)

	###################
	# Private Methods #
	###################

	def __loadData(self):
		for i in [15, 6, 18, 3, 7, 17, 20, 2, 4, 13, 9]:
			self.bstObj.insert(NodeBST(i))

	def __deleteIter(self):
		for i in [15, 5, 16, 3, 12, 20, 10, 13, 18, 23, 6, 7]:
			yield i

	def __loadDeleteData(self):
		for i in self.__deleteIter():
			self.bstObj.insert(NodeBST(i))

	def __deleteNode(self, value):
		delNode = self.bstObj.search(value)

		self.assertTrue(value in self.bstObj)
		self.bstObj.delete(delNode)
		self.assertTrue(not value in self.bstObj)

if __name__ == '__main__':
	unittest.main()
