'''
Singly Linked List module
'''

class Node:
    '''
    Node or Link Class
    '''
    def __init__(self, data, next_node=None):
        '''
        Function to initialize the Node object
        It has the node data  and a link for the next node
        '''
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        '''
        Getter method for the node data
        '''
        return self._data

    @data.setter
    def data(self, data):
        '''
        Setter method for the node data
        '''
        self._data = data

    @property
    def next_node(self):
        '''
        Getter method for next node
        '''
        return self._next_node

    @next_node.setter
    def next_node(self, next_node):
        '''
        Setter method for next node
        '''
        self._next_node = next_node

class LinkedList:
    '''
    Singly Linked List class
    '''
    def __init__(self):
        '''
        Singly Linked List constructor that has only the head as member
        '''
        self._head = None

    def __repr__(self):
        '''
        Singly Linked List representation
        e.g. '2->1->0'
        '''
        str_repr = ''
        current = self._head
        while current is not None:
            if current != self._head:
                str_repr = str_repr + '->'
            str_repr = str_repr + str(current.data)
            current = current.next_node
        return str_repr

    def insert(self, data):
        '''
        Linked List operation that inserts a node at the begging for the list
        '''
        if self._head is None:
            self._head = Node(data)
        else:
            tmp_node = Node(data, self._head)
            self._head = tmp_node

    def delete(self):
        '''
        Linked List operation that deletes a node from the begging of the list
        '''
        if self._head is None:
            raise ValueError('List is empty')
        self._head = self._head.next_node

    def search(self, data):
        '''
        Linked List operation that searches for the first node that has the given
        data on the list
        '''
        current = self._head
        index = 0

        while current is not None:
            if current.data == data:
                return index
            index += 1
            current = current.next_node

        return None

    def delete_at_index(self, index):
        '''
        Linked List operation that deletes a node at a specific index on the list
        '''
        if self._head is None:
            raise ValueError('List is empty')

        if index == 0:
            self._head = self._head.next_node
            return

        current = self._head
        cur_index = 0
        wanted_index = index - 1 # We want the previous node to delete right one
        while current is not None:
            if cur_index == wanted_index and current.next_node is not None:
                to_be_deleted = current.next_node
                current.next_node = to_be_deleted.next_node
                return
            cur_index += 1
            current = current.next_node

        raise ValueError(f"Couldn't find node at index {index}")
