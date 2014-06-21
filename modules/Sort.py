class Sort(object):

	@staticmethod
	def insertion(array):

		# Iterate through each position except the first
		for i in range(1, len(array)):
			# Store the current value
			key = array[i]

			# Iterate through all previous values so long as they are greater
			# then the current value.  Swap both values
			j = i - 1
			while j >= 0 and array[j] > key:
				array[j+1] = array[j]
				j -= 1
			array[j+1] = key

	@staticmethod
	def selection(array):
		arrayLen = len(array)

		# Iterate through each position except the last
		for i in range(arrayLen-1):

			# Look for the index position with the smallest possible value
			minIndex = i
			for j in range(i+i, arrayLen):
				if array[j] < array[minIndex]:
					minIndex = j

			# Swap current element with min element
			array[i], array[minIndex] = array[minIndex], array[i]
