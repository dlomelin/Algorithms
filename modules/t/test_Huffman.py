import unittest
from Algorithms.modules.Huffman import Huffman
from Algorithms.modules.dataStructures.Node import Node

class TestHuffman(unittest.TestCase):
	def setUp(self):
		dataList = [
			Node({'char': 'a', 'freq': 45}),
			Node({'char': 'b', 'freq': 13}),
			Node({'char': 'c', 'freq': 12}),
			Node({'char': 'd', 'freq': 16}),
			Node({'char': 'e', 'freq': 9}),
			Node({'char': 'f', 'freq': 5}),
		]
		self.huffmanObj = Huffman(dataList)

	def test_decode(self):
		bitString = '001011101'
		decString = self.huffmanObj.decode(bitString)
		self.assertEqual(decString, 'aabe')

if __name__ == '__main__':
	unittest.main()
