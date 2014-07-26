from Algorithms.modules.dataStructures.mixins.MixinEquality import MixinEquality

class Vertex(MixinEquality):
	def __init__(self):
		self.setStatus()
		self.setParent()

	########################
	# Operator Overloading #
	########################

	#def __repr__(self):
	#	return '%s(%s)' % (self.__class__.__name__, self.value())

	def __str__(self):
		return ''

	##################
	# Public Methods #
	##################

	def getStatus(self):
		return self.__status

	def setStatus(self, status = None):
		self.__status = status

	def getParent(self):
		return self.__parent

	def setParent(self, vertex = None):
		self.__parent = vertex

	###################
	# Private Methods #
	###################
