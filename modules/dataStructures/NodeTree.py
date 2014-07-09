class NodeTree(object):
	def __init__(self, key = lambda x: x):
		# TODO handle calling NodeTree with a list to initialize it

		# Initialize empty root
		self._setRoot()

		self.__key = key

	########################
	# Operator Overloading #
	########################

	# for node in self:
	def __iter__(self):

		node = self.root()

		while not node is None:
			yield node
			node = node.next()

	# if x in self:
	def __contains__(self, value):
		for node in self:
			if self._nodeValue(node) == value:
				return True

		return False

	# print self
	def __str__(self):
		return ' -> '.join(str(self._nodeValue(node)) for node in self)

	##################
	# Public Methods #
	##################

	def search(self, value):
		node = None

		# Check each node until it finds the one with the specified value
		for tNode in self:
			if self._nodeValue(tNode) == value:
				node = tNode
				break

		return node

	def root(self):
		return self.__root

	########################
	# Semi-private Methods #
	########################

	def _setRoot(self, value = None):
		self.__root = value

	def _nodeValue(self, node):
		return self.__key(node.value())
