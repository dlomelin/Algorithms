from Algorithms.modules.dataStructures.mixins.MixinEquality import MixinEquality

class Stack(MixinEquality):
	def __init__(self, array = []):
		self.__array = array
		self.__setIndex(len(self.__array) - 1)

	########################
	# Operator Overloading #
	########################

	def __str__(self):
		# Calls __iter__ and converts to a string
		return str(list(self))

	def __len__(self):
		return self.__index() + 1

	def __iter__(self):
		for i in xrange(self.__index() + 1):
			yield self[i]

	def __getitem__(self, index):
		return self.__array[index]

	##################
	# Public Methods #
	##################

	def push(self, value):
		self.__increaseIndex()
		try:
			self[self.__index()] = value
		except:
			self.__array.append(value)

	def pop(self):
		if self.empty():
			# TODO change to return None instead?
			raise Exception('No items left to pop in stack')
		else:
			self.__decreaseIndex()
			return self[self.__index() + 1]

	# Returns True or False if the Stack is empty
	def empty(self):
		if self.__index() < 0:
			return True
		else:
			return False

	###################
	# Private Methods #
	###################

	def __index(self):
		return self.__topIndex
	def __setIndex(self, value):
		self.__topIndex = value
	def __increaseIndex(self):
		self.__topIndex += 1
	def __decreaseIndex(self):
		self.__topIndex -= 1
