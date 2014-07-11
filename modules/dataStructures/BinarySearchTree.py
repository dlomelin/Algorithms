from Algorithms.modules.dataStructures.Node import Node
from Algorithms.modules.dataStructures.NodeTree import NodeTree

class BinarySearchTree(NodeTree):

	########################
	# Operator Overloading #
	########################

	# for node in self:
	def __iter__(self):
		rootNode = self.root()

		for node in self.__treeIter(rootNode):
			yield node

	##################
	# Public Methods #
	##################

	def insert(self, insertNode):

		parentNode = None
		testNode = self.root()

		# Iterate down the tree of nodes until it finds a node that has an
		# empty slot for the current insert node
		while not testNode is None:
			parentNode = testNode
			if self._nodeKey(insertNode) < self._nodeKey(testNode):
				testNode = testNode.left()
			else:
				testNode = testNode.right()

		# Set the insert node's parent to the node that had an empty slot
		insertNode.setParent(parentNode)

		if parentNode is None:
			# Tree was empty, set root node
			self._setRoot(insertNode)
		else:
			# Place the insert node as a child of the parent node in its correct position
			if self._nodeKey(insertNode) < self._nodeKey(parentNode):
				parentNode.setLeft(insertNode)
			else:
				parentNode.setRight(insertNode)

	# TODO def delete()

	# Finds the node with the specified value
	def search(self, value):
		node = self.root()

		while not node is None and value != self._nodeKey(node):
			if value < self._nodeKey(node):
				node = node.left()
			else:
				node = node.right()

		return node

	# Finds the node with the minimum value
	def minimum(self):
		node = self.root()

		while not node is None and not node.left() is None:
			node = node.left()

		return node

	# Finds the node with the maximum value
	def maximum(self):
		node = self.root()

		while not node is None and not node.right() is None:
			node = node.right()

		return node

	###################
	# Private Methods #
	###################

	# Recursive iterator that walks through each node in order
	def __treeIter(self, node):
		if not node is None:
			for lNode in self.__treeIter(node.left()):
				yield lNode
			yield node
			for rNode in self.__treeIter(node.right()):
				yield rNode

