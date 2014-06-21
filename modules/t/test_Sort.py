import unittest
from Algorithms.modules.Sort import Sort

class TestSort(unittest.TestCase):
	def setUp(self):
		self.unsortedList = [5, 3, 11, 7, 11, 1, 18]
		self.pythonSorted = sorted(self.unsortedList)

	def test_insertion(self):
		# Function sorts list in place
		Sort.insertion(self.unsortedList)
		self.assertEqual(self.unsortedList, self.pythonSorted)

	def test_selection(self):
		# Function sorts list in place
		Sort.selection(self.unsortedList)
		self.assertEqual(self.unsortedList, self.pythonSorted)

if __name__ == '__main__':
	unittest.main()
