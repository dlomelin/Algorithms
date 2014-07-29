import unittest
from Algorithms.modules.Graph import Graph
from Algorithms.modules.dataStructures.Vertex import Vertex

class TestGraph(unittest.TestCase):
	def setUp(self):
		self.graph = Graph()
		self.__addVertices()

	def test_bfs(self):
		self.graph.bfs('s')

	def __addVertices(self):
		self.graph.addVertex('r', Vertex('r', ['s', 'v']))
		self.graph.addVertex('s', Vertex('s', ['r', 'w']))
		self.graph.addVertex('t', Vertex('t', ['u', 'w', 'x']))
		self.graph.addVertex('u', Vertex('u', ['t', 'x', 'y']))
		self.graph.addVertex('v', Vertex('v', ['r']))
		self.graph.addVertex('w', Vertex('w', ['s', 't', 'x']))
		self.graph.addVertex('x', Vertex('x', ['t', 'u', 'y']))
		self.graph.addVertex('y', Vertex('y', ['u', 'x']))

if __name__ == '__main__':
	unittest.main()
