import unittest
import Algorithms.modules.Huffman as Huffman

class TestHuffman(unittest.TestCase):
	def setUp(self):
		pass

	def test_huffman(self):
		Huffman.huffman()

if __name__ == '__main__':
	unittest.main()
