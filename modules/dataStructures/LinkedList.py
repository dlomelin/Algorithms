from Algorithms.modules.dataStructures.Node import Node
from Algorithms.modules.dataStructures.NodeTree import NodeTree

class LinkedList(NodeTree):

	##################
	# Public Methods #
	##################

	def insert(self, value):

		# Create new head node whose next node is the current Head
		currentHead = self.root()
		newHead = Node(value, nNode = currentHead)

		# Set the current head to point at the new head
		if not currentHead is None:
			currentHead.setPrev(newHead)

		# Set the new head
		self._setRoot(newHead)
