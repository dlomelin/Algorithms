import unittest
from Algorithms.modules.Graph import Graph
from Algorithms.modules.dataStructures.Vertex import Vertex

class TestGraph(unittest.TestCase):
	def setUp(self):
		self.graph = Graph()

	def test_dfs(self):
		self.__addVertices1()
		self.graph.dfs()

		# Get vertex 'y'
		vertex = self.graph.getVertex('t')

		# Validate vertex 'y' has the appropriate values set
		self.assertEqual(vertex.getStatus(), 'visited')
		self.assertEqual(vertex.getPredecessor(), 'u')
		self.assertEqual(vertex.getDistance(), 5)

	def test_dfsPrintPath(self):
		self.__addVertices1()
		# Runs depth first search
		self.graph.dfs()

		path = self.graph.getPath('t')
		self.assertEqual(path, ['s', 'w', 'x', 'y', 'u', 't'])

		path = self.graph.getPath('s')
		self.assertEqual(path, ['s'])

		path = self.graph.getPath('z')
		self.assertEqual(path, ['z'])

	def test_dfsPrintStructure(self):
		self.__addVertices1()
		self.graph.dfs()

		self.assertEqual(self.graph.getStructure(), '(s(r(vv)r)(w(x(y(u(tt)u)y)x)w)s)(zz)')

	def test_bfs(self):
		self.__addVertices1()
		# Runs breadth first search using 's' vertex as the root node
		self.graph.bfs('s')

		# Get vertex 'y'
		vertex = self.graph.getVertex('y')

		# Validate vertex 'y' has the appropriate values set
		self.assertEqual(vertex.getStatus(), 'visited')
		self.assertEqual(vertex.getPredecessor(), 'x')
		self.assertEqual(vertex.getDistance(), 3)

	def test_bfsPrintPath(self):
		self.__addVertices1()

		# Runs breadth first search using 's' vertex as the root node
		self.graph.bfs('s')

		path = self.graph.getPath('y')
		self.assertEqual(path, ['s', 'w', 'x', 'y'])

		path = self.graph.getPath('s')
		self.assertEqual(path, ['s'])

		path = self.graph.getPath('z')
		self.assertEqual(path, [])

	def test_bfsShortestPath(self):
		self.__addVertices2()

		# Runs breadth first search using 's' vertex as the root node
		self.graph.bfs('s')

		print self.graph

	###################
	# Private Methods #
	###################

	def __addVertices1(self):
		self.graph.addVertex('r', Vertex('r', {'s': 1, 'v': 1}))
		self.graph.addVertex('s', Vertex('s', {'r': 1, 'w': 1}))
		self.graph.addVertex('t', Vertex('t', {'u': 1, 'w': 1, 'x': 1}))
		self.graph.addVertex('u', Vertex('u', {'t': 1, 'x': 1, 'y': 1}))
		self.graph.addVertex('v', Vertex('v', {'r': 1}))
		self.graph.addVertex('w', Vertex('w', {'s': 1, 't': 1, 'x': 1}))
		self.graph.addVertex('x', Vertex('x', {'t': 1, 'u': 1, 'y': 1}))
		self.graph.addVertex('y', Vertex('y', {'u': 1, 'x': 1}))
		self.graph.addVertex('z', Vertex('z', {}))

	def __addVertices2(self):
		self.graph.addVertex('s', Vertex('s', {'t': 3, 'y': 5}))
		self.graph.addVertex('t', Vertex('t', {'y': 2, 'x': 6}))
		self.graph.addVertex('x', Vertex('x', {'z': 2}))
		self.graph.addVertex('y', Vertex('y', {'t': 1, 'x': 4, 'z': 6}))
		self.graph.addVertex('z', Vertex('z', {'s': 3, 'x': 7}))

if __name__ == '__main__':
	unittest.main()