'''.'''

from algorithms.data_structures.mixins.EqualityMixin import EqualityMixin


class Vertex(EqualityMixin):
    '''
    Defines a Vertex, which is used for various different graph algorithms.
    '''
    def __init__(self, key, adj_dict):
        self.__key = key
        self.__adjacency_dict = adj_dict

        self.reset_vertex()

    ########################
    # Operator Overloading #
    ########################

    def __str__(self):
        return 'Vertex: %s  Neighbors: %s  Distance: %s  Predecessor: %s' % (
            self.get_key(),
            self.__adjacency_dict,
            self.get_distance(),
            self.get_predecessor(),
        )

    ##################
    # Public Methods #
    ##################

    def reset_vertex(self):
        '''
        Resets several attributes to their default values

        :param:  None

        :return:  None
        '''
        self.set_status()
        self.set_distance()
        self.set_predecessor()

    def adjacencies(self):
        '''
        Iterator that returns the names of adjacent vertices

        :param:  None

        :yield:  String - Name of an adjacent vertex
        '''
        for vertex_key in self.__adjacency_dict.keys():
            yield vertex_key

    def get_edge_weight(self, vertex_key):
        '''
        Returns the edge weight between this vertex and its adjacent neighbor

        :param vertex_key:  The name of the adjacent vertex

        :return:  Integer - The weight of the edge between this vertex and its neighbor
        '''
        return self.__adjacency_dict[vertex_key]

    def get_key(self):
        '''
        Returns the key assigned to this vertex
        :param:  None
        :return:  String - The identifier/name of this vertex
        '''
        return self.__key

    def get_status(self):
        '''
        Gets the status attribute
        :param:  None
        :return:  The status of this vertex (used for graph algorithms)
        '''
        return self.__status

    def set_status(self, status='unvisited'):
        '''
        Sets the status attribute
        :param status:
        :return:  None
        '''
        self.__status = status  # pylint: disable=attribute-defined-outside-init

    def get_predecessor(self):
        '''
        Gets the predecessor attribute
        :param:  None
        :return:  The predecessor of this vertex (used for graph algorithms)
        '''
        return self.__predecessor

    def set_predecessor(self, vertex=None):
        '''
        Sets the predecessor attribute
        :param vertex:
        :return:  None
        '''
        self.__predecessor = vertex  # pylint: disable=attribute-defined-outside-init

    def get_distance(self):
        '''
        Gets the distance attribute
        :param:  None
        :return:  The distance of this vertex (used for graph algorithms)
        '''
        return self.__distance

    def set_distance(self, distance=float('inf')):
        '''
        Sets the distance attribute
        :param distance:
        :return:  None
        '''
        self.__distance = distance  # pylint: disable=attribute-defined-outside-init
