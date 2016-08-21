import unittest
from algorithms.Graph import Graph
from algorithms.dataStructures.Vertex import Vertex

class TestGraph(unittest.TestCase):
    def setUp(self):
        self.graph = Graph()

    def test_dfs(self):
        self.__addVertices1()
        self.graph.dfs()

        # Get vertex 't'
        vertex = self.graph.getVertex('t')
        #path = self.graph.getPath('t')
        #self.graph.getStructure()

        # Validate vertex 't' has the appropriate values set
        self.assertEqual(vertex.getStatus(), 'visited')

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

    ###################
    # Private Methods #
    ###################

    def __addVertices1(self):
        '''
        v<->r<->s<->w<->t<->u<->y   z
                    |   ^   ^   ^
                    |  /   /   /
                    | /   /   /
                    vv   /   /
                    x<--/---/
        '''
        self.graph.addVertex(Vertex('r', {'s': 1, 'v': 1}))
        self.graph.addVertex(Vertex('s', {'r': 1, 'w': 1}))
        self.graph.addVertex(Vertex('t', {'u': 1, 'w': 1, 'x': 1}))
        self.graph.addVertex(Vertex('u', {'t': 1, 'x': 1, 'y': 1}))
        self.graph.addVertex(Vertex('v', {'r': 1}))
        self.graph.addVertex(Vertex('w', {'s': 1, 't': 1, 'x': 1}))
        # 'w' can connect to 'x' but 'x' cannot get back to 'w'
        self.graph.addVertex(Vertex('x', {'t': 1, 'u': 1, 'y': 1}))
        self.graph.addVertex(Vertex('y', {'u': 1, 'x': 1}))
        self.graph.addVertex(Vertex('z', {}))

    def __addVertices2(self):
        self.graph.addVertex(Vertex('s', {'t': 3, 'y': 5}))
        self.graph.addVertex(Vertex('t', {'y': 2, 'x': 6}))
        self.graph.addVertex(Vertex('x', {'z': 2}))
        self.graph.addVertex(Vertex('y', {'t': 1, 'x': 4, 'z': 6}))
        self.graph.addVertex(Vertex('z', {'s': 3, 'x': 7}))

if __name__ == '__main__':
    unittest.main()
