import unittest
from Algorithms.modules.dataStructures.Heap import Heap

class TestHeap(unittest.TestCase):
	def setUp(self):
		#self.array = [1, 2, 3, 4, 7, 8, 9, 10, 14, 16]
		self.array = [16, 4, 10, 14, 7, 9, 3, 2, 8, 1]
		self.heapedArray = [16, 14, 10, 8, 7, 9, 3, 2, 4, 1]

	def test_heapifyMax(self):
		myHeap = Heap(self.array)
		print myHeap
		index = 1
		myHeap.heapifyMax(index)
		print myHeap

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
