import unittest
from algorithms.Huffman import Huffman
from algorithms.dataStructures.Node import Node

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

        self.stringDecoded = 'aabe'
        self.stringEncoded = '001011101'

    def test_decode(self):
        decString = self.huffmanObj.decode(self.stringEncoded)
        self.assertEqual(decString, self.stringDecoded)

    def test_encode(self):
        encString = self.huffmanObj.encode(self.stringDecoded)
        self.assertEqual(encString, self.stringEncoded)

    def test_encodeDecode(self):
        decString = self.huffmanObj.decode(
            self.huffmanObj.encode(self.stringDecoded)
        )
        self.assertEqual(decString, self.stringDecoded)

if __name__ == '__main__':
    unittest.main()
