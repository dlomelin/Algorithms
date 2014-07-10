class Node(object):
	def __init__(self, value, pNode = None, lNode = None, rNode = None):
		self.__value = value

		self.setParent(pNode)
		self.setLeft(lNode)
		self.setRight(rNode)

	########################
	# Operator Overloading #
	########################

	def __repr__(self):
		return '%s(%s)' % (self.__class__.__name__, self.value())

	def __str__(self):
		try:
			lVal = self.left().value()
		except:
			lVal = None

		try:
			rVal = self.right().value()
		except:
			rVal = None

		return '%s << %s (%s) >> %s' % (lVal, self.value(), self.parent(), rVal)

	##################
	# Public Methods #
	##################

	def value(self):
		return self.__value

	def parent(self):
		return self.__parent

	def left(self):
		return self.__left

	def right(self):
		return self.__right

	def setParent(self, node):
		self.__parent = node

	def setLeft(self, node):
		self.__left = node

	def setRight(self, node):
		self.__right = node
