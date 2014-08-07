from Algorithms.modules.dataStructures.Queue import Queue

class Graph(object):

	def __init__(self):
		self.__vertices = {}
		self.__clearDfsStructure()

	########################
	# Operator Overloading #
	########################

	def __iter__(self):
		for key in self.__vertices.keys():
			yield self.getVertex(key)

	def __str__(self):
		string = []
		for vertex in self:
			string.append(str(vertex))
		return '\n'.join(string)

	##################
	# Public Methods #
	##################

	# Performs a depth first search across all Vertex objects that are loaded into
	# the Graph object.
	def dfs(self):
		# Reset DFS structure (s(r(vv)r)(w(t(u(x(yy)x)u)t)w)s)(zz)
		self.__clearDfsStructure()

		# Reset all vertices
		for vertex in self:
			vertex.resetVertex()

		# Iterate through all unvisited nodes in the graph and perform a dfs visit
		for vertex in self:
			if vertex.getStatus() == 'unvisited':
				vertex.setDistance(0)
				self.__dfsVisit(vertex)

	# Performs a breadth first search across the user specified Vertex object.
	def bfs(self, rootVertexKey):

		# Reset all vertices
		for vertex in self:
			vertex.resetVertex()

		# Mark user specified vertex as the first queued vertex
		self.getVertex(rootVertexKey).setStatus('queued')
		self.getVertex(rootVertexKey).setDistance(0)

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

					# Calculates the distance between the 2 vertices and replaces their
					# distance if it's less than the older value
					self.__relax(currentVertex, adjVertex)

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

	# Returns a string that shows the search route that was taken during the dfs algorithm.
	# Ex: (s(r(vv)r)(w(t(u(x(yy)x)u)t)w)s)(zz)
	# self.dfs() must be called first in order to create the string.  Otherwise an emptry string
	# is returned.
	def getStructure(self):
		return ''.join(self.__dfsStructure)

	# Returns a Vertex() object stored using vertexKey identifier
	def getVertex(self, vertexKey):
		try:
			return self.__vertices[vertexKey]
		except:
			raise Exception('Invalid vertex key specified: %s' % (vertexKey))

	# Adds a Vertex() object and stores it using vertexKey as its identifier
	def addVertex(self, vertexKey, vertex):
		self.__vertices[vertexKey] = vertex

	###################
	# Private Methods #
	###################

	def __relax(self, startVertex, endVertex):
		# Determine the distance between startVertex and endVertex
		endVertexKey = endVertex.getKey()
		vertexDistance = startVertex.getDistance() + startVertex.getEdgeWeight(endVertexKey)

		# If new distance is less than the older distance, then set the new distance
		if endVertex.getDistance() > vertexDistance:
			endVertex.setDistance(vertexDistance)
			startVertexKey = startVertex.getKey()
			endVertex.setPredecessor(startVertexKey)

	# Recursive method that performs the depth first search
	def __dfsVisit(self, vertex):
		vertex.setStatus('queued')
		vertexKey = vertex.getKey()

		# Stores the structural element that marks this node as discovered
		self.__dfsDiscover(vertexKey)

		# Iterate through each neighboring vertex
		for adjVertexKey in vertex.adjacencies():
			adjVertex = self.getVertex(adjVertexKey)

			if adjVertex.getStatus() == 'unvisited':

				# Calculates the distance between the 2 vertices and replaces their
				# distance if it's less than the older value
				self.__relax(vertex, adjVertex)

				self.__dfsVisit(adjVertex)

		# Vertex and all its adjacent vertices (and children vertices) have all been
		# searched.  Marks the vertex as completed.
		vertex.setStatus('visited')

		# Stores the structural element that marks this node as finished
		self.__dfsFinish(vertexKey)

	# Adds the dfs algorithm's discovery structural element
	def __dfsDiscover(self, vertexKey):
		self.__dfsStructure.append('(%s' % (vertexKey))

	# Adds the dfs algorithm's finishing structural element
	def __dfsFinish(self, vertexKey):
		self.__dfsStructure.append('%s)' % (vertexKey))

	# Reset the depth first search structure.
	def __clearDfsStructure(self):
		self.__dfsStructure = []

