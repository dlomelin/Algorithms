import unittest
from algorithms.BWT import BWT

class TestBWT(unittest.TestCase):
    def setUp(self):
        self.bwtObj = BWT()

    def test_transformEos(self):
        inputString = 'missi$$ippi'
        self.assertRaises(Exception, self.bwtObj.transform, (inputString))

    def test_transform1(self):
        inputString = 'abaaba'
        transformString = 'abba$aa'
        self.bwtObj.transform(inputString)

        self.assertEqual(self.bwtObj.getTransformString(), transformString)

    def test_transform2(self):
        inputString = 'mississippi'
        transformString = 'ipssm$pissii'
        frontString = '$iiiimppssss'
        self.bwtObj.transform(inputString)

        self.assertEqual(self.bwtObj.getTransformString(), transformString)
        self.assertEqual(self.bwtObj.getFrontString(), frontString)

    def test_inverseTransform(self):
        transformString = 'ipssm$pissii'
        inverseString = self.bwtObj.inverseTransform(transformString)
        self.assertEqual(inverseString, 'mississippi')

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
        (firstIndex, lastIndex) = self.bwtObj.backwardSearch(pattern)
        self.assertEqual(fIndex, firstIndex)
        self.assertEqual(lIndex, lastIndex)

        if not fIndex is None:
            for i in range(firstIndex, lastIndex+1):
                ogIndex = self.bwtObj.getOriginalIndex(i)
                slice1 = ogIndex - 1
                slice2 = ogIndex + len(pattern) - 1
                self.assertEqual(pattern, inputString[slice1:slice2])

if __name__ == '__main__':
    unittest.main()
