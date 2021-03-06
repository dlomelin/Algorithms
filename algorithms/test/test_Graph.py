import unittest
from algorithms.Graph import Graph
from algorithms.data_structures.Vertex import Vertex


class TestGraph(unittest.TestCase):
    def setUp(self):
        self.graph = Graph()

    def test_dfs_string(self):
        self.__addVertices2()
        self.graph.dfs()
        self.assertEqual(
            str(self.graph),
            "Vertex: y  Neighbors: {'x': 4, 'z': 6, 't': 1}  Distance: 0  Predecessor: None\n"
            "Vertex: x  Neighbors: {'z': 2}  Distance: 4  Predecessor: y\n"
            "Vertex: s  Neighbors: {'y': 5, 't': 3}  Distance: 9  Predecessor: z\n"
            "Vertex: z  Neighbors: {'x': 7, 's': 3}  Distance: 6  Predecessor: x\n"
            "Vertex: t  Neighbors: {'y': 2, 'x': 6}  Distance: 12  Predecessor: s",
        )

    def test_missing_vertex(self):
        with self.assertRaises(KeyError):
            self.graph.get_vertex('invalid_key')

    def test_dfs_get_structure(self):
        self.__addVertices1()
        self.graph.dfs()

        struct = self.graph.get_structure()
        self.assertEqual(
            struct,
            '(s(r(vv)r)(w(x(y(u(tt)u)y)x)w)s)(zz)',
        )

    def test_dfs_get_path(self):
        self.__addVertices1()
        self.graph.dfs()

        path = self.graph.get_path('t')
        self.assertListEqual(
            path,
            ['s', 'w', 'x', 'y', 'u', 't'],
        )

    def test_dfs_get_vertex(self):
        self.__addVertices1()
        self.graph.dfs()

        # Get vertex 't'
        vertex = self.graph.get_vertex('t')
        # Validate vertex 't' has the appropriate values set
        self.assertEqual(vertex.get_status(), 'visited')

    def test_bfs(self):
        self.__addVertices1()
        # Runs breadth first search using 's' vertex as the root node
        self.graph.bfs('s')

        # Get vertex 'y'
        vertex = self.graph.get_vertex('y')

        # Validate vertex 'y' has the appropriate values set
        self.assertEqual(vertex.get_status(), 'visited')
        self.assertEqual(vertex.get_predecessor(), 'x')
        self.assertEqual(vertex.get_distance(), 3)

    def test_bfsPrintPath(self):
        self.__addVertices1()

        # Runs breadth first search using 's' vertex as the root node
        self.graph.bfs('s')

        path = self.graph.get_path('y')
        self.assertEqual(path, ['s', 'w', 'x', 'y'])

        path = self.graph.get_path('s')
        self.assertEqual(path, ['s'])

        path = self.graph.get_path('z')
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
        self.graph.add_vertex(Vertex('r', {'s': 1, 'v': 1}))
        self.graph.add_vertex(Vertex('s', {'r': 1, 'w': 1}))
        self.graph.add_vertex(Vertex('t', {'u': 1, 'w': 1, 'x': 1}))
        self.graph.add_vertex(Vertex('u', {'t': 1, 'x': 1, 'y': 1}))
        self.graph.add_vertex(Vertex('v', {'r': 1}))
        self.graph.add_vertex(Vertex('w', {'s': 1, 't': 1, 'x': 1}))
        # 'w' can connect to 'x' but 'x' cannot get back to 'w'
        self.graph.add_vertex(Vertex('x', {'t': 1, 'u': 1, 'y': 1}))
        self.graph.add_vertex(Vertex('y', {'u': 1, 'x': 1}))
        self.graph.add_vertex(Vertex('z', {}))

    def __addVertices2(self):
        self.graph.add_vertex(Vertex('s', {'t': 3, 'y': 5}))
        self.graph.add_vertex(Vertex('t', {'y': 2, 'x': 6}))
        self.graph.add_vertex(Vertex('x', {'z': 2}))
        self.graph.add_vertex(Vertex('y', {'t': 1, 'x': 4, 'z': 6}))
        self.graph.add_vertex(Vertex('z', {'s': 3, 'x': 7}))
