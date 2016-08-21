import unittest
from algorithms.dataStructures.Heap import Heap

class TestHeap(unittest.TestCase):
    def setUp(self):
        self.sortedArrayAsc = [1, 2, 3, 4, 7, 8, 9, 10, 14, 16]
        self.sortedArrayDesc = self.sortedArrayAsc[::-1]
        self.maxHeapedArray = [16, 14, 9, 10, 7, 8, 3, 1, 4, 2]
        self.sortingArray = [16, 14, 10, 8, 7, 9, 3, 2, 4, 1]
        self.dictList = [
            {'name': 'Carl', 'age': 13},
            {'name': 'Bob', 'age': 6},
            {'name': 'Amy', 'age': 25},
            {'name': 'Frank', 'age': 18},
            {'name': 'David', 'age': 9},
        ]

    def test_keyAge(self):
        myHeap = Heap(self.dictList, key = lambda x: x['age'])
        myHeap.sort()
        self.assertEqual(list(myHeap), [
            {'name': 'Bob', 'age': 6},
            {'name': 'David', 'age': 9},
            {'name': 'Carl', 'age': 13},
            {'name': 'Frank', 'age': 18},
            {'name': 'Amy', 'age': 25},
        ])

    def test_keyName(self):
        myHeap = Heap(self.dictList, key = lambda x: x['name'])
        myHeap.sort()
        self.assertEqual(list(myHeap), [
            {'name': 'Amy', 'age': 25},
            {'name': 'Bob', 'age': 6},
            {'name': 'Carl', 'age': 13},
            {'name': 'David', 'age': 9},
            {'name': 'Frank', 'age': 18},
        ])

    def test_insert(self):
        myHeap = Heap(self.sortingArray)
        myHeap.insert(15)
        self.assertEqual(list(myHeap), [16, 15, 10, 8, 14, 9, 3, 2, 4, 1, 7])

    def test_sortAscending(self):
        myHeap = Heap(self.sortingArray)
        myHeap.sort()
        self.assertEqual(list(myHeap), self.sortedArrayAsc)

    def test_sortDescending(self):
        myHeap = Heap(self.sortingArray, heapType = 'min')
        myHeap.sort()
        self.assertEqual(list(myHeap), self.sortedArrayDesc)

    def test_initHeap(self):
        myHeap = Heap(self.sortedArrayAsc)
        self.assertEqual(list(myHeap), self.maxHeapedArray)

if __name__ == '__main__':
    unittest.main()
