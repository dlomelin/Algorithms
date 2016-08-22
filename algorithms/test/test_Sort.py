import unittest
import algorithms.Sort as Sort


class TestSort(unittest.TestCase):
    def setUp(self):
        self.unsortedList = [5, 2, 4, 7, 1, 3, 2, 6]
        self.pythonSorted = sorted(self.unsortedList)

    def test_merge_sort(self):
        # Function sorts list in place
        Sort.merge_sort(self.unsortedList)
        self.assertEqual(self.unsortedList, self.pythonSorted)

    def test_heap_sort(self):
        # Function returns a sorted list
        self.assertEqual(Sort.heap_sort(self.unsortedList), self.pythonSorted)

    def test_insertion_sort(self):
        # Function sorts list in place
        Sort.insertion_sort(self.unsortedList)
        self.assertEqual(self.unsortedList, self.pythonSorted)

    def test_selection_sort(self):
        # Function sorts list in place
        Sort.selection_sort(self.unsortedList)
        self.assertEqual(self.unsortedList, self.pythonSorted)

    def test_bubble_sort(self):
        # Function sorts list in place
        Sort.bubble_sort(self.unsortedList)
        self.assertEqual(self.unsortedList, self.pythonSorted)
