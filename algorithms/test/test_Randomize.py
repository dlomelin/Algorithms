import unittest
import algorithms.Randomize as Randomize


class TestRandomize(unittest.TestCase):
    def setUp(self):
        self.sortedList = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        self.randomList = list(self.sortedList)

    def test_randomizeBySorting(self):
        Randomize.randomize(self.randomList)
        self.assertItemsEqual(
            self.sortedList,
            self.randomList,
        )
        self.assertNotEqual(
            self.sortedList,
            self.randomList,
        )
