import unittest
import Algorithms.modules.Huffman as Huffman
from Algorithms.modules.dataStructures.Node import Node

class TestHuffman(unittest.TestCase):
	def setUp(self):
		pass

	def test_huffman(self):
		dataList = [
			Node({'char': 'a', 'freq': 45}),
			Node({'char': 'b', 'freq': 13}),
			Node({'char': 'c', 'freq': 12}),
			Node({'char': 'd', 'freq': 16}),
			Node({'char': 'e', 'freq': 9}),
			Node({'char': 'f', 'freq': 5}),
		]
		Huffman.huffman(dataList)

if __name__ == '__main__':
	unittest.main()
