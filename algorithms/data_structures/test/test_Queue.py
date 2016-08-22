import unittest
from algorithms.data_structures.Queue import Queue


class TestQueue(unittest.TestCase):
    def setUp(self):
        pass

    def test_endequeue(self):
        qObj = Queue([1, 2, 3])
        qObj.enqueue(5)
        qObj.enqueue(12)
        qObj.dequeue()
        qObj.dequeue()

        self.assertListEqual(
            list(qObj),
            [3, 5, 12],
        )

    def test_str(self):
        qObj = Queue([3, 5, 12])

        self.assertEqual(
            str(qObj),
            '[3, 5, 12]',
        )

    def test_dequeue_empty(self):
        qObj = Queue()
        self.assertIsNone(qObj.dequeue())

    def test_enqueue(self):
        qObj = Queue([1, 2, 3])
        qObj.enqueue(5)

        self.assertListEqual(
            list(qObj),
            [1, 2, 3, 5],
        )

    def test_dequeue(self):
        qObj = Queue([1, 2, 3])
        val = qObj.dequeue()
        self.assertEqual(val, 1)
        self.assertListEqual(
            list(qObj),
            [2, 3],
        )

    def test_emptyTrue(self):
        qObj = Queue()
        self.assertTrue(qObj.empty())

    def test_emptyFalse(self):
        qObj = Queue([1])
        self.assertFalse(qObj.empty())
