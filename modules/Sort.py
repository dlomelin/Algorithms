class Sort(object):

	# Small wrapper around __mergeSort to prevent user from
	# having to specify bounds
	@staticmethod
	def mergeSort(array):
		Sort.__mergeSort(array, 0, len(array)-1)

	@staticmethod
	def insertionSort(array):

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
	def selectionSort(array):
		arrayLen = len(array)

		# Iterate through each position except the last
		for i in range(arrayLen-1):

			# Look for the index position with the smallest possible value
			minIndex = i
			for j in range(i+1, arrayLen):
				if array[j] < array[minIndex]:
					minIndex = j
			
			# Swap current element with min element
			array[i], array[minIndex] = array[minIndex], array[i]

	@staticmethod
	def bubbleSort(array):
		arrayLen = len(array)

		# Iterate through each position
		for i in range(arrayLen):

			# Compare each position and swap elements to make the larger values
			# go higher in the index and the lowest value to the beginning
			for j in range(arrayLen-1, i, -1):
				if array[j] < array[j-1]:
					array[j], array[j-1] = array[j-1], array[j]

	###################
	# Private Methods #
	###################

	@staticmethod
	def __mergeSort(array, p, r):
		if p < r:
			q = (p+r) / 2
			Sort.__mergeSort(array, p, q)
			Sort.__mergeSort(array, q+1, r)
			Sort.__merge(array, p, q, r)

	@staticmethod
	def __merge(array, p, q, r):
		# Create left and right list based on p, q, r
		lList = array[p:q+1]
		rList = array[q+1:r+1]

		# Append sentinel
		lList.append(float('inf'))
		rList.append(float('inf'))

		lIndex = 0
		rIndex = 0
		for i in range(p, r+1):
			if lList[lIndex] < rList[rIndex]:
				array[i] = lList[lIndex]
				lIndex += 1
			else:
				array[i] = rList[rIndex]
				rIndex += 1

