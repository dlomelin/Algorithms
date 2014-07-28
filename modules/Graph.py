from Algorithms.modules.dataStructures.Queue import Queue

class Graph(object):

	def __init__(self):
		self.__vertices = {}

	# Breadth first search
	def bfs(self, rootVertexKey):

		# Reset all vertices
		for key in self.__vertices.keys():
			self.__vertices[key].setStatus('unvisited')
			self.__vertices[key].setDistance(float('inf'))
			self.__vertices[key].setPredecessor(None)

		# Mark user specified vertex as the first queued vertex
		self.__vertices[rootVertexKey].setStatus('queued')
		self.__vertices[rootVertexKey].setDistance(0)
		self.__vertices[rootVertexKey].setPredecessor(None)

		queueObj = Queue()
		queueObj.enqueue(rootVertexKey)

		while not queueObj.empty():
			# Remove 1 vertex from the queue
			vertexKey = queueObj.dequeue()
			currentVertex = self.__vertices[vertexKey]

			print currentVertex

			# Iterate through each neighboring vertex
			for adjVertexKey in currentVertex.adjacencies():
				adjVertex = self.__vertices[adjVertexKey]

				# If that node has never been visited, modify it and add it to the queue
				if adjVertex.getStatus() == 'unvisited':
					adjVertex.setStatus('queued')
					adjVertex.setDistance(currentVertex.getDistance() + 1)
					adjVertex.setPredecessor(vertexKey)

					queueObj.enqueue(adjVertexKey)

			# Mark the current vertex as visited
			currentVertex.setStatus('visited')


	def addVertex(self, vertexKey, vertex):
		self.__vertices[vertexKey] = vertex
