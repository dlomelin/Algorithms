import unittest
from algorithms.BWT import BWT


class TestBWT(unittest.TestCase):
    def setUp(self):
        self.bwtObj = BWT()

    def test_transformEos(self):
        inputString = 'missi$$ippi'
        with self.assertRaises(ValueError):
            self.bwtObj.transform(inputString)

    def test_transform1(self):
        inputString = 'abaaba'
        transformString = 'abba$aa'
        self.bwtObj.transform(inputString)

        self.assertEqual(self.bwtObj.get_transform_string(), transformString)

    def test_transform2(self):
        inputString = 'mississippi'
        transformString = 'ipssm$pissii'
        frontString = '$iiiimppssss'
        self.bwtObj.transform(inputString)

        self.assertEqual(self.bwtObj.get_transform_string(), transformString)
        self.assertEqual(self.bwtObj.get_front_string(), frontString)

    def test_inverseTransform(self):
        transformString = 'ipssm$pissii'
        inverse_string = self.bwtObj.inverse_transform(transformString)
        self.assertEqual(inverse_string, 'mississippi')

    def test_inverseTransform_ValueError(self):
        transformString = 'ipssmpissii'
        with self.assertRaises(ValueError):
            self.bwtObj.inverse_transform(transformString)

    def test_backwardSearchAndgetOriginalIndex(self):
        inputString = 'mississippi'
        self.bwtObj.transform(inputString)

        self.__validateBackwardSearch(inputString, 'iss', 3, 4)
        self.__validateBackwardSearch(inputString, 'ippi', 2, 2)
        self.__validateBackwardSearch(inputString, 'ispi', None, None)
        self.__validateBackwardSearch(inputString, 'iggi', None, None)

    ###################
    # Private Methods #
    ###################

    def __validateBackwardSearch(self, inputString, pattern, fIndex, lIndex):
        (firstIndex, lastIndex) = self.bwtObj.backward_search(pattern)
        self.assertEqual(fIndex, firstIndex)
        self.assertEqual(lIndex, lastIndex)

        if fIndex is not None:
            for i in range(firstIndex, lastIndex+1):
                ogIndex = self.bwtObj.get_original_index(i)
                slice1 = ogIndex - 1
                slice2 = ogIndex + len(pattern) - 1
                self.assertEqual(pattern, inputString[slice1:slice2])
