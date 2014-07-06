class Node(object):
	def __init__(self, value, pNode = None, nNode = None):
		self.__value = value
		self.setPrev(pNode)
		self.setNext(nNode)

	########################
	# Operator Overloading #
	########################

	def __repr__(self):
		return '%s(%s)' % (self.__class__.__name__, self.value())

	def __str__(self):
		try:
			pVal = self.prev().value()
		except:
			pVal = None

		try:
			nVal = self.next().value()
		except:
			nVal = None

		return '%s << %s >> %s' % (pVal, self.value(), nVal)

	##################
	# Public Methods #
	##################

	def value(self):
		return self.__value

	def prev(self):
		return self.__prev

	def next(self):
		return self.__next

	def setPrev(self, node):
		self.__prev = node

	def setNext(self, node):
		self.__next = node
