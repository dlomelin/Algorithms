import unittest
from algorithms.PriorityQueue import PriorityQueue, PriorityQueueMax, PriorityQueueMin


class TestPriorityQueue(unittest.TestCase):
    def setUp(self):
        self.array = [4, 3, 2, 1, 7, 8, 9, 10, 14, 16]

    def test_empty_queue(self):
        max_queue = PriorityQueueMax()
        self.assertEqual(
            len(max_queue),
            0,
        )

        min_queue = PriorityQueueMin()
        self.assertEqual(
            len(min_queue),
            0,
        )

    def test_pqMaxExtractTopQueue(self):
        pqObj = PriorityQueueMax(self.array)
        element = pqObj.extract_top_queue()
        self.assertEqual(
            element,
            16,
        )
        # New max should be next in line
        self.assertEqual(
            pqObj.top_queue(),
            14,
        )

    def test_pqMinExtractTopQueue(self):
        pqObj = PriorityQueueMin(self.array)
        element = pqObj.extract_top_queue()
        self.assertEqual(
            element,
            1,
        )
        # New min should be next in line
        self.assertEqual(
            pqObj.top_queue(),
            2,
        )

    def test_pqMaxTopQueue(self):
        pqObj = PriorityQueueMax(self.array)
        self.assertEqual(
            pqObj.top_queue(),
            16,
        )

    def test_pqMinTopQueue(self):
        pqObj = PriorityQueueMin(self.array)
        self.assertEqual(
            pqObj.top_queue(),
            1,
        )
