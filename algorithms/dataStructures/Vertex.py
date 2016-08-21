from algorithms.dataStructures.mixins.MixinEquality import MixinEquality

class Vertex(MixinEquality):
    def __init__(self, key, adjacencyDict):
        self.__key = key
        self.__adjacencyDict = adjacencyDict

        self.resetVertex()

    ########################
    # Operator Overloading #
    ########################

    def __str__(self):
        return 'Vertex: %s  Neighbors: %s  Distance: %s  Predecessor: %s' % (
            self.__key,
            self.__adjacencyDict,
            self.getDistance(),
            self.getPredecessor(),
        )

    ##################
    # Public Methods #
    ##################

    # Calls several methods to reset publicly available attributes
    def resetVertex(self):
        self.setStatus()
        self.setDistance()
        self.setPredecessor()

    def adjacencies(self):
        for vertexKey in self.__adjacencyDict.keys():
            yield vertexKey

    # Returns the edge weight between this vertex and its adjacent neighbor
    def getEdgeWeight(self, vertexKey):
        return self.__adjacencyDict[vertexKey]

    def getKey(self):
        return self.__key

    def getStatus(self):
        return self.__status

    def setStatus(self, status = 'unvisited'):
        self.__status = status

    def getPredecessor(self):
        return self.__predecessor

    def setPredecessor(self, vertex = None):
        self.__predecessor = vertex

    def getDistance(self):
        return self.__distance

    def setDistance(self, distance = float('inf')):
        self.__distance = distance

    ###################
    # Private Methods #
    ###################
