import unittest
from algorithms.data_structures.LinkedList import LinkedList

class TestLinkedList(unittest.TestCase):
    def setUp(self):
        self.llObj = LinkedList()

    def test_insert(self):
        self.__insertData()

        listData = []
        for node in self.llObj:
            listData.append(node.value())

        self.assertEqual(listData, [1, 2, 3, 4])

    def test_str(self):
        self.__insertData()
        self.assertEqual(str(self.llObj), '1 -> 2 -> 3 -> 4')

    # Make sure in statement works correctly
    def test_inTrue(self):
        self.__insertData()
        self.assertTrue(3 in self.llObj)

    # Make sure in statement works correctly
    def test_inFalse(self):
        self.__insertData()
        self.assertFalse(33 in self.llObj)

    # Search for a node that should be found
    def test_search(self):
        self.__insertData()

        node = self.llObj.search(3)

        self.assertEqual(node.value(), 3)

    # Search for missing node in linked list with data
    def test_searchEmpty1(self):
        self.__insertData()

        node = self.llObj.search(345)

        self.assertEqual(node, None)

    # Search for missing node in an empty linked list
    def test_searchEmpty2(self):
        node = self.llObj.search(345)

        self.assertEqual(node, None)

    ###################
    # Private Methods #
    ###################

    def __insertData(self):
        for i in xrange(4, 0, -1):
            self.llObj.insert(i)
