import unittest
from Algorithms.modules.PriorityQueue import PriorityQueue, PriorityQueueMax, PriorityQueueMin

class TestPriorityQueue(unittest.TestCase):
	def setUp(self):
		self.array = [4, 3, 2, 1, 7, 8, 9, 10, 14, 16]

	def test_pqMaxExtractTopQueue(self):
		pqObj = PriorityQueueMax(self.array)
		v = pqObj.extractTopQueue()

	def test_pqMaxTopQueue(self):
		pqObj = PriorityQueueMax(self.array)
		self.assertEqual(pqObj.topQueue(), 16)

	def test_pqMinTopQueue(self):
		pqObj = PriorityQueueMin(self.array)
		self.assertEqual(pqObj.topQueue(), 1)

if __name__ == '__main__':
	unittest.main()
