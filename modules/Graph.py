from Algorithms.modules.dataStructures.Queue import Queue

class Graph(object):

	def __init__(self):
		self.__vertices = {}

	########################
	# Operator Overloading #
	########################

	def __iter__(self):
		for key in self.__vertices.keys():
			yield self.getVertex(key)

	##################
	# Public Methods #
	##################

	# Breadth first search
	def bfs(self, rootVertexKey):

		# Reset all vertices
		for vertex in self:
			vertex.setStatus('unvisited')
			vertex.setDistance(float('inf'))
			vertex.setPredecessor(None)

		# Mark user specified vertex as the first queued vertex
		self.getVertex(rootVertexKey).setStatus('queued')
		self.getVertex(rootVertexKey).setDistance(0)
		self.getVertex(rootVertexKey).setPredecessor(None)

		queueObj = Queue()
		queueObj.enqueue(rootVertexKey)

		while not queueObj.empty():
			# Remove 1 vertex from the queue
			vertexKey = queueObj.dequeue()
			currentVertex = self.getVertex(vertexKey)

			# Iterate through each neighboring vertex
			for adjVertexKey in currentVertex.adjacencies():
				adjVertex = self.getVertex(adjVertexKey)

				# If that node has never been visited, modify it and add it to the queue
				if adjVertex.getStatus() == 'unvisited':
					adjVertex.setStatus('queued')
					adjVertex.setDistance(currentVertex.getDistance() + 1)
					adjVertex.setPredecessor(vertexKey)

					queueObj.enqueue(adjVertexKey)

			# Mark the current vertex as visited
			currentVertex.setStatus('visited')

	# Returns a list of vertexKeys that show the path from the bfs node to the user specified key
	def getPath(self, vertexKey):
		vertexKeys = []

		# Only perform operation if vertexKey has been found from the starting node
		if not self.getVertex(vertexKey).getDistance() == float('inf'):

			while not vertexKey is None:
				vertexKeys.insert(0, vertexKey)
				vertex = self.getVertex(vertexKey)
				vertexKey = vertex.getPredecessor()

		return vertexKeys

	# Returns a Vertex() object stored using vertexKey identifier
	def getVertex(self, vertexKey):
		try:
			return self.__vertices[vertexKey]
		except:
			raise Exception('Invalid vertex key specified: %s' % (vertexKey))

	# Adds a Vertex() object and stores it using vertexKey as its identifier
	def addVertex(self, vertexKey, vertex):
		self.__vertices[vertexKey] = vertex
