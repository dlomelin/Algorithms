from Algorithms.modules.dataStructures.mixins.MixinEquality import MixinEquality

class Vertex(MixinEquality):
	def __init__(self, key, adjacencyList):
		self.__key = key
		self.__adjacencyList = adjacencyList

		self.setStatus()
		self.setPredecessor()
		self.setDistance()

	########################
	# Operator Overloading #
	########################

	def __str__(self):
		return 'Vertex: %s  Neighbors: %s  Distance: %s  Predecessor: %s' % (
			self.__key,
			self.__adjacencyList,
			self.getDistance(),
			self.getPredecessor(),
		)

	##################
	# Public Methods #
	##################

	def adjacencies(self):
		for vertexKey in self.__adjacencyList:
			yield vertexKey

	def getStatus(self):
		return self.__status

	def setStatus(self, status = None):
		self.__status = status

	def getPredecessor(self):
		return self.__predecessor

	def setPredecessor(self, vertex = None):
		self.__predecessor = vertex

	def getDistance(self):
		return self.__distance

	def setDistance(self, distance = 0):
		self.__distance = distance

	###################
	# Private Methods #
	###################
