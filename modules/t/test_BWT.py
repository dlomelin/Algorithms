import unittest
from Algorithms.modules.BWT import BWT

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

	def test_backwardSearch(self):
		inputString = 'mississippi'
		self.bwtObj.transform(inputString)

		self.__validateBackwardSearch('iss', 3, 4)
		self.__validateBackwardSearch('ippi', 2, 2)
		self.__validateBackwardSearch('ispi', None, None)
		self.__validateBackwardSearch('iggi', None, None)

	###################
	# Private Methods #
	###################

	def __validateBackwardSearch(self, pattern, fIndex, lIndex):
		(firstIndex, lastIndex) = self.bwtObj.backwardSearch(pattern)
		self.assertEqual(fIndex, firstIndex)
		self.assertEqual(lIndex, lastIndex)

if __name__ == '__main__':
	unittest.main()
