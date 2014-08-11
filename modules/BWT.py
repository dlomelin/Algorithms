class BWT(object):
	def __init__(self, eos = '$'):
		self.__eos = eos

		self.__resetTransformData()

	##################
	# Public Methods #
	##################

	# Creates transform data needed for backwardSearch method
	def transform(self, inputString):
		self.__resetTransformData()

		# Make sure end of string character is not already present and then
		# append eos to string
		if self.__eos in inputString:
			raise Exception('Invalid end of string character specified.  "%s" found in input.' % (self.__eos))
		inputString = '%s%s' % (inputString, self.__eos)

		# Create the table necessary for the transform
		transformTable = []

		# Generate a list of cyclically shifted strings, then sort them
		for i in xrange(len(inputString)):
			transformTable.append('%s%s' % (inputString[i:], inputString[:i]))
		transformTable = sorted(transformTable)

		print 'Transform Table'
		for i in xrange(len(transformTable)):
			print transformTable[i]
		print '---'

		# Return a string compsed of the characters from the final column
		for i in xrange(len(transformTable)):
			firstChar = transformTable[i][0]
			lastChar = transformTable[i][-1]

			self.__charIndexObj.add(firstChar, i)
			self.__occurrenceTableObj.add(lastChar, i)
			self.__frontColumn.append(firstChar)
			self.__transformColumn.append(lastChar)

		print 'Char Index'
		print self.__charIndexObj
		print '---'

	def backwardSearch(self, pattern):

		patternIndex = len(pattern) - 1
		currentChar = pattern[patternIndex]

		firstIndex = self.__charIndexObj.getFirstIndex(currentChar)
		lastIndex = self.__charIndexObj.getLastIndex(currentChar)

		while firstIndex <= lastIndex and patternIndex >= 1 and not(firstIndex is None or lastIndex is None):
			currentChar = pattern[patternIndex - 1]

			firstIndex = self.__lastToFront(currentChar, firstIndex - 1)
			# Handling to add 1 when return value is None
			try:
				firstIndex += 1
			except:
				pass
			lastIndex = self.__lastToFront(currentChar, lastIndex)

			patternIndex -= 1

		# Convert index values to None when pattern was not found
		if firstIndex > lastIndex:
			(firstIndex, lastIndex) = (None, None)

		return (firstIndex, lastIndex)

	def getTransformString(self):
		return ''.join(self.__transformColumn)

	def getFrontString(self):
		return ''.join(self.__frontColumn)

	###################
	# Private Methods #
	###################

	def __resetTransformData(self):
		self.__frontColumn = []
		self.__transformColumn = []
		self.__charIndexObj = CharacterIndex()
		self.__occurrenceTableObj = OccurrenceTable()

	# Finds the index corresponding to the prior character in the original string
	def __lastToFront(self, char, index):
		try:
			return self.__charIndexObj.getFirstIndex(char) + self.__occurrenceTableObj.getValue(char, index) - 1
		except:
			return None


class CharacterIndex(object):
	def __init__(self):
		self.__data = {}

	########################
	# Operator Overloading #
	########################

	def __str__(self):
		stringData = []
		for key in self.__data.keys():
			stringData.append('%s: [%s, %s]' % (key, self.getFirstIndex(key), self.getLastIndex(key)))
		return '\n'.join(stringData)

	##################
	# Public Methods #
	##################

	def add(self, char, index):
		if not char in self.__data:
			self.__data[char] = {'first': index, 'last': index}
		else:
			self.__data[char]['last'] = index

	def getFirstIndex(self, char):
		try:
			return self.__data[char]['first']
		except:
			return None

	def getLastIndex(self, char):
		try:
			return self.__data[char]['last']
		except:
			return None


class OccurrenceTable(object):
	def __init__(self):
		self.__data = []

	########################
	# Operator Overloading #
	########################

	def __iter__(self):
		for i in range(len(self.__data)):
			yield self.__data[i]

	def __str__(self):
		stringData = []

		for data in self:
			stringData.append(str(data))

		return '\n'.join(stringData)

	##################
	# Public Methods #
	##################

	def add(self, char, index):
		# Copy the previous index's dictionary.
		# Should only fail when index == 0
		try:
			newDict = self.__data[index-1].copy()
		except:
			newDict = {char: 0}

		# Increase the counter for the current character.
		# If it's this character's first occurrence, backtrace
		# through the previous entries to fill in zero values.
		try:
			newDict[char] += 1
		except:
			newDict[char] = 1
			for i in range(index):
				self.__data[i][char] = 0

		self.__data.append(newDict)

	def getValue(self, char, index):
		try:
			return self.__data[index][char]
		except:
			return None

