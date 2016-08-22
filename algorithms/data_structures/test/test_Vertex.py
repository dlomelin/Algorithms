import unittest
from algorithms.data_structures.Vertex import Vertex


class TestVertex(unittest.TestCase):
    def setUp(self):
        self.key = 'a'
        self.neighbor_dict = {'x': 1, 'y': 2, 'z': 3}
        self.vertex = Vertex(self.key, self.neighbor_dict)

    def test_string(self):
        self.assertRegexpMatches(
            str(self.vertex),
            'Vertex: a  Neighbors: {\'[x-z]\': [1-3], \'[x-z]\': [1-3], \'[x-z]\': [1-3]}  Distance: inf  Predecessor: None',
        )

    def test_adjacencies(self):
        self.assertItemsEqual(
            list(self.vertex.adjacencies()),
            list(self.neighbor_dict.keys()),
        )

    def test_get_key(self):
        self.assertEqual(
            self.vertex.get_key(),
            self.key,
        )

    def test_get_edge_weight(self):
        self.assertEqual(
            self.vertex.get_edge_weight('y'),
            2,
        )

    def test_reset_vertex_setters_getters(self):
        new_status = 'visited'
        self.vertex.set_status(new_status)

        new_distance = 76
        self.vertex.set_distance(new_distance)

        new_predecessor = 'xyz'
        self.vertex.set_predecessor(new_predecessor)

        self.__check_vertex_attributes(new_status, new_distance, new_predecessor)

        # Now reset it and check again
        self.vertex.reset_vertex()

        self.__check_vertex_attributes('unvisited', float('inf'), None)

    def __check_vertex_attributes(self, status, distance, predecessor):
        self.assertEqual(
            self.vertex.get_status(),
            status,
        )

        self.assertEqual(
            self.vertex.get_distance(),
            distance,
        )

        self.assertEqual(
            self.vertex.get_predecessor(),
            predecessor,
        )
