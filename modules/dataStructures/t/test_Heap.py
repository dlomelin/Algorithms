import unittest
from Algorithms.modules.dataStructures.Heap import Heap

class TestHeap(unittest.TestCase):
	def setUp(self):
		self.sortedArray = [1, 2, 3, 4, 7, 8, 9, 10, 14, 16]
		self.heapedArray = [16, 14, 9, 10, 7, 8, 3, 1, 4, 2]
		self.sortingArray = [16, 14, 10, 8, 7, 9, 3, 2, 4, 1]

	def test_sort(self):
		myHeap = Heap(self.sortingArray)
		myHeap.sort()
		self.assertEqual(list(myHeap), self.sortedArray)

	def test_buildHeapMax(self):
		myHeap = Heap(self.sortedArray)
		myHeap.buildHeapMax()
		self.assertEqual(list(myHeap), self.heapedArray)

	def test_nodes1(self):
		myHeap = Heap(self.heapedArray)
		index = 3

		parent = myHeap.parent(index)
		left = myHeap.left(index)
		right = myHeap.right(index)

		self.assertEqual(parent, 1)
		self.assertEqual(left, 7)
		self.assertEqual(right, 8)

	def test_nodes2(self):
		myHeap = Heap(self.heapedArray)
		index = 4

		parent = myHeap.parent(index)
		left = myHeap.left(index)
		right = myHeap.right(index)

		self.assertEqual(parent, 1)
		self.assertEqual(left, 9)
		self.assertEqual(right, None)

	def test_nodes3(self):
		myHeap = Heap(self.heapedArray)
		index = 5

		parent = myHeap.parent(index)
		left = myHeap.left(index)
		right = myHeap.right(index)

		self.assertEqual(parent, 2)
		self.assertEqual(left, None)
		self.assertEqual(right, None)

	def test_nodes4(self):
		myHeap = Heap(self.heapedArray)
		index = 0

		parent = myHeap.parent(index)
		left = myHeap.left(index)
		right = myHeap.right(index)

		self.assertEqual(parent, None)
		self.assertEqual(left, 1)
		self.assertEqual(right, 2)

if __name__ == '__main__':
	unittest.main()
