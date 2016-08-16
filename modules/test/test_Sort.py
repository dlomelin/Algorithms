import unittest
import Algorithms.modules.Sort as Sort

class TestSort(unittest.TestCase):
	def setUp(self):
		self.unsortedList = [5, 2, 4, 7, 1, 3, 2, 6]
		self.pythonSorted = sorted(self.unsortedList)

	def test_mergeSort(self):
		# Function sorts list in place
		Sort.mergeSort(self.unsortedList)
		self.assertEqual(self.unsortedList, self.pythonSorted)

	def test_heapSort(self):
		# Function returns a sorted list
		self.assertEqual(Sort.heapSort(self.unsortedList), self.pythonSorted)

	def test_insertionSort(self):
		# Function sorts list in place
		Sort.insertionSort(self.unsortedList)
		self.assertEqual(self.unsortedList, self.pythonSorted)

	def test_selectionSort(self):
		# Function sorts list in place
		Sort.selectionSort(self.unsortedList)
		self.assertEqual(self.unsortedList, self.pythonSorted)

	def test_bubbleSort(self):
		# Function sorts list in place
		Sort.bubbleSort(self.unsortedList)
		self.assertEqual(self.unsortedList, self.pythonSorted)

if __name__ == '__main__':
	unittest.main()
