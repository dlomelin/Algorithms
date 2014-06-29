# Small wrapper around __mergeSort to prevent user from
# having to specify bounds
def mergeSort(array):
	__mergeSort(array, 0, len(array)-1)

def insertionSort(array):

	# Iterate through each position except the first
	for i in xrange(1, len(array)):
		# Store the current value
		key = array[i]

		# Iterate through all previous values so long as they are greater
		# then the current value.  Swap both values
		j = i - 1
		while j >= 0 and array[j] > key:
			array[j+1] = array[j]
			j -= 1
		array[j+1] = key

def selectionSort(array):
	arrayLen = len(array)

	# Iterate through each position except the last
	for i in xrange(arrayLen-1):

		# Look for the index position with the smallest possible value
		minIndex = i
		for j in xrange(i+1, arrayLen):
			if array[j] < array[minIndex]:
				minIndex = j

		# Swap current element with min element
		array[i], array[minIndex] = array[minIndex], array[i]

def bubbleSort(array):
	arrayLen = len(array)

	# Iterate through each position
	for i in xrange(arrayLen):

		# Compare each position and swap elements to make the larger values
		# go higher in the index and the lowest value to the beginning
		for j in xrange(arrayLen-1, i, -1):
			if array[j] < array[j-1]:
				array[j], array[j-1] = array[j-1], array[j]

#####################
# Private Functions #
#####################

def __mergeSort(array, p, r):
	if p < r:
		q = (p+r) / 2
		__mergeSort(array, p, q)
		__mergeSort(array, q+1, r)
		__merge(array, p, q, r)

def __merge(array, p, q, r):
	# Create left and right list based on p, q, r
	lList = array[p:q+1]
	rList = array[q+1:r+1]

	# Append sentinel
	lList.append(float('inf'))
	rList.append(float('inf'))

	lIndex = 0
	rIndex = 0
	for i in xrange(p, r+1):
		if lList[lIndex] < rList[rIndex]:
			array[i] = lList[lIndex]
			lIndex += 1
		else:
			array[i] = rList[rIndex]
			rIndex += 1

