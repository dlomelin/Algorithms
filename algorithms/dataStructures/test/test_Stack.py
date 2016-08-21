import unittest
from algorithms.dataStructures.Stack import Stack

class TestStack(unittest.TestCase):
    def setUp(self):
        pass

    def test_push(self):
        stackObj = Stack([1, 2, 3])
        stackObj.push(5)
        self.assertEqual(list(stackObj), [1, 2, 3, 5])

    def test_pop(self):
        stackObj = Stack([1, 2, 3])
        val = stackObj.pop()
        self.assertEqual(val, 3)
        self.assertEqual(list(stackObj), [1, 2])

    def test_multiPop(self):
        stackObj = Stack([1, 2, 3, 4, 5])
        for val in stackObj.multiPop(3):
            pass
        self.assertEqual(list(stackObj), [1, 2])

    def test_pushPop(self):
        stackObj = Stack([1, 2, 3])
        stackObj.push(5)
        stackObj.push(12)
        stackObj.push(7)
        val = stackObj.pop()
        self.assertEqual(val, 7)
        val = stackObj.pop()
        self.assertEqual(val, 12)
        self.assertEqual(list(stackObj), [1, 2, 3, 5])

    def test_emptyTrue(self):
        stackObj = Stack()
        self.assertTrue(stackObj.empty())

    def test_emptyFalse(self):
        stackObj = Stack([2, 5, 13])
        self.assertFalse(stackObj.empty())

if __name__ == '__main__':
    unittest.main()
