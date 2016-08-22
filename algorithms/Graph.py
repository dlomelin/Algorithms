'''.'''

from algorithms.data_structures.Queue import Queue


class Graph(object):
    ''' Implements a Graph for various algorithms '''

    def __init__(self):
        self.__vertices = {}
        self.__clear_dfs_structure()

    ########################
    # Operator Overloading #
    ########################

    def __iter__(self):
        for key in self.__vertices:
            yield self.get_vertex(key)

    def __str__(self):
        string = []
        for vertex in self:
            string.append(str(vertex))
        return '\n'.join(string)

    ##################
    # Public Methods #
    ##################

    def dfs(self):
        '''
        Performs a depth first search across all Vertex objects that are loaded into
        the Graph object.

        :param:  None

        :return:  None
        '''
        # Reset DFS structure (s(r(vv)r)(w(t(u(x(yy)x)u)t)w)s)(zz)
        self.__clear_dfs_structure()

        # Reset all vertices
        for vertex in self:
            vertex.reset_vertex()

        # Iterate through all unvisited nodes in the graph and perform a dfs visit
        for vertex in self:
            if vertex.get_status() == 'unvisited':
                vertex.set_distance(0)
                self.__dfs_visit(vertex)

    def bfs(self, root_vertex_key):
        '''
        Performs a breadth first search across the user specified Vertex object.

        :param root_vertex_key:  String - Vertex key

        :return:  None
        '''
        # Reset all vertices
        for vertex in self:
            vertex.reset_vertex()

        # Mark user specified vertex as the first queued vertex
        self.get_vertex(root_vertex_key).set_status('queued')
        self.get_vertex(root_vertex_key).set_distance(0)

        queue_obj = Queue()
        queue_obj.enqueue(root_vertex_key)

        while not queue_obj.empty():
            # Remove 1 vertex from the queue
            vertex_key = queue_obj.dequeue()
            current_vertex = self.get_vertex(vertex_key)

            # Iterate through each neighboring vertex
            for adj_vertex_key in current_vertex.adjacencies():
                adj_vertex = self.get_vertex(adj_vertex_key)

                # If that node has never been visited, modify it and add it to the queue
                if adj_vertex.get_status() == 'unvisited':
                    adj_vertex.set_status('queued')

                    # Calculates the distance between the 2 vertices and replaces their
                    # distance if it's less than the older value
                    self.__relax(current_vertex, adj_vertex)

                    queue_obj.enqueue(adj_vertex_key)

            # Mark the current vertex as visited
            current_vertex.set_status('visited')

    def get_path(self, vertex_key):
        '''
        Returns a list of vertex keys that show the path from the bfs node to the user specified key

        :param vertex_key:  String - Vertex key

        :return:  List - Vertex keys that go from the root node to vertex_key
        '''
        vertex_keys = []

        # Only perform operation if vertex_key has been found from the starting node
        if not self.get_vertex(vertex_key).get_distance() == float('inf'):

            while not vertex_key is None:
                vertex_keys.insert(0, vertex_key)
                vertex = self.get_vertex(vertex_key)
                vertex_key = vertex.get_predecessor()

        return vertex_keys

    def get_structure(self):
        '''
        Returns a string that shows the search route that was taken during the dfs algorithm.
        self.dfs() must be called first in order to create the string.  Otherwise an emptry string
        is returned.

        :param:  None

        :return:  String - Ex: (s(r(vv)r)(w(t(u(x(yy)x)u)t)w)s)(zz)
        '''
        return ''.join(self.__dfs_structure)

    def get_vertex(self, vertex_key):
        '''
        Returns a Vertex() object stored using vertex_key identifier

        :param vertex_key:  String - Vertex key

        :return:  Vertex - Instance of a Vertex class
        '''

        try:
            return self.__vertices[vertex_key]
        except:
            raise Exception('Invalid vertex key specified: %s' % (vertex_key))

    def add_vertex(self, vertex):
        '''
        Adds a Vertex() object and stores it using vertex_key as its identifier

        :param vertex:  Vertex - Instance of a Vertex class

        :return:  None
        '''
        vertex_key = vertex.get_key()
        self.__vertices[vertex_key] = vertex

    ###################
    # Private Methods #
    ###################

    @staticmethod
    def __relax(start_vertex, end_vertex):
        # Determine the distance between start_vertex and end_vertex
        end_vertex_key = end_vertex.get_key()
        vertex_distance = start_vertex.get_distance() + start_vertex.get_edge_weight(end_vertex_key)

        # If new distance is less than the older distance, then set the new distance
        if end_vertex.get_distance() > vertex_distance:
            end_vertex.set_distance(vertex_distance)
            start_vertex_key = start_vertex.get_key()
            end_vertex.set_predecessor(start_vertex_key)

    def __dfs_visit(self, vertex):
        ''' Recursive method that performs the depth first search '''

        vertex.set_status('queued')
        vertex_key = vertex.get_key()

        # Stores the structural element that marks this node as discovered
        self.__dfs_discover(vertex_key)

        # Iterate through each neighboring vertex
        for adj_vertex_key in vertex.adjacencies():
            adj_vertex = self.get_vertex(adj_vertex_key)

            if adj_vertex.get_status() == 'unvisited':

                # Calculates the distance between the 2 vertices and replaces their
                # distance if it's less than the older value
                self.__relax(vertex, adj_vertex)

                self.__dfs_visit(adj_vertex)

        # Vertex and all its adjacent vertices (and children vertices) have all been
        # searched.  Marks the vertex as completed.
        vertex.set_status('visited')

        # Stores the structural element that marks this node as finished
        self.__dfs_finish(vertex_key)

    def __dfs_discover(self, vertex_key):
        ''' Adds the dfs algorithm's discovery structural element '''
        self.__dfs_structure.append('(%s' % (vertex_key))

    def __dfs_finish(self, vertex_key):
        ''' Adds the dfs algorithm's finishing structural element '''
        self.__dfs_structure.append('%s)' % (vertex_key))

    def __clear_dfs_structure(self):
        ''' Reset the depth first search structure '''
        self.__dfs_structure = []
