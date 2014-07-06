from Algorithms.modules.dataStructures.Node import Node

class LinkedList(object):
	def __init__(self, key = lambda x: x):
		# TODO handle calling LinkedList with a list to initialize it
		self.__head = None

		# TODO handle tail setting
		self.__tail = None

		self.__key = key

	########################
	# Operator Overloading #
	########################

	# for node in self:
	def __iter__(self):

		node = self.head()

		while not node is None:
			yield node
			node = node.next()

	# if x in self:
	def __contains__(self, value):
		for node in self:
			if self.__nodeValue(node) == value:
				return True

		return False

	# print self
	def __str__(self):
		return ' -> '.join(str(self.__nodeValue(node)) for node in self)

	##################
	# Public Methods #
	##################

	def insert(self, value):

		# Create new head node whose next node is the current Head
		currentHead = self.head()
		newHead = Node(value, nNode = currentHead)

		# Set the current head to point at the new head
		if not currentHead is None:
			currentHead.setPrev(newHead)

		# Set the new head
		self.__head = newHead

	def search(self, value):
		node = None

		# Check each node until it finds the one with the specified value
		for tNode in self:
			if self.__nodeValue(tNode) == value:
				node = tNode
				break

		return node

	def head(self):
		return self.__head

	def tail(self):
		return self.__tail

	###################
	# Private Methods #
	###################

	def __nodeValue(self, node):
		return self.__key(node.value())
