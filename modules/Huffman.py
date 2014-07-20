from Algorithms.modules.PriorityQueue import PriorityQueueMin
from Algorithms.modules.dataStructures.Node import Node

def huffman(dataList):

	listLength = len(dataList)

	pqmObj = PriorityQueueMin(array = dataList, key = lambda x: x.value()['freq'])

	print 'Starting tree:'
	for node in pqmObj:
		print node
	print 'Done'
	print '=========='

	for i in range(listLength-1):
		leftMin = pqmObj.extractTopQueue()
		rightMin = pqmObj.extractTopQueue()

		print 'Topleft: %s' % (leftMin)
		print 'Topright: %s' % (rightMin)

		# Add the left and right node frequencies as the new frequency
		# and create a new node
		newFreq = leftMin.value()['freq'] + rightMin.value()['freq']
		node = Node({'freq': newFreq}, lNode = leftMin, rNode = rightMin)

		print 'Inserting node: ',
		print node

		pqmObj.insert(node)

		print 'Updated tree:'
		for node in pqmObj:
			print node
		print 'Done'
		print '=========='
