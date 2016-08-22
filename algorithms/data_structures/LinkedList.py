'''.'''

from algorithms.data_structures.Node import Node
from algorithms.data_structures.NodeTree import NodeTree


class LinkedList(NodeTree):
    '''
    LinkedList data structure
    '''

    def insert(self, value):
        '''
        Inserts the value as a Node object in the LinkedList

        :param value:  Various - The value of the node (int, float, string, etc)

        :return:  None
        '''

        # Create new head node whose next node is the current Head
        current_head = self.root()
        new_head = Node(value, r_node=current_head)

        # Set the current head to point at the new head
        if current_head is not None:
            current_head.set_left(new_head)

        # Set the new head
        self._set_root(new_head)
