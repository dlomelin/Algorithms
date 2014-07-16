from Algorithms.modules.dataStructures.mixins.MixinEquality import MixinEquality

class Node(MixinEquality):
	def __init__(self, value, pNode = None, lNode = None, rNode = None):
		self.setValue(value)

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

		try:
			pVal = self.parent().value()
		except:
			pVal = None

		return '%s << %s (%s) >> %s' % (lVal, self.value(), pVal, rVal)

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

	def setValue(self, value):
		self.__value = value

	def setParent(self, node):
		self.__validateNode(node)
		self.__parent = node

	def setLeft(self, node):
		self.__validateNode(node)
		self.__left = node

	def setRight(self, node):
		self.__validateNode(node)
		self.__right = node

	###################
	# Private Methods #
	###################

	def __validateNode(self, node):
		if not node is None and not type(self) is type(node):
			raise Exception('Invalid node type passed as argument: %s.  Must be %s' % (
					node.__class__.__name__,
					self.__class__.__name__,
				)
			)
