import unittest
import Algorithms.modules.Randomize as Randomize

class TestRandomize(unittest.TestCase):
	def setUp(self):
		self.sortedList = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

	def test_randomizeBySorting(self):
		Randomize.randomize(self.sortedList)

if __name__ == '__main__':
	unittest.main()
