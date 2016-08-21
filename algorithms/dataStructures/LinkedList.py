from algorithms.dataStructures.Node import Node
from algorithms.dataStructures.NodeTree import NodeTree

class LinkedList(NodeTree):

    ##################
    # Public Methods #
    ##################

    def insert(self, value):

        # Create new head node whose next node is the current Head
        currentHead = self.root()
        newHead = Node(value, rNode = currentHead)

        # Set the current head to point at the new head
        if not currentHead is None:
            currentHead.setLeft(newHead)

        # Set the new head
        self._setRoot(newHead)
