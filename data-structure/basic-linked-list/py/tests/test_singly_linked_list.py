'''
Unitest module for Singly Linked List
'''

import unittest
from singly_linked_list import LinkedList

class TestSinglyLinkedList(unittest.TestCase):
    '''
    Singly Linked List unit test class
    '''
    def test_insert_nodes(self):
        '''
        Test Singly Linked List insert operation
        '''
        linked_list = LinkedList()
        self.assertEqual('', repr(linked_list))
        linked_list.insert(1)
        self.assertEqual('1', repr(linked_list))
        linked_list.insert(2)
        self.assertEqual('2->1', repr(linked_list))
        linked_list.insert(3)
        self.assertEqual('3->2->1', repr(linked_list))

    def test_delete_nodes(self):
        '''
        Test Singly Linked List delete operation
        '''
        linked_list = LinkedList()
        self.assertEqual('', repr(linked_list))
        linked_list.insert(1)
        self.assertEqual('1', repr(linked_list))
        linked_list.delete()
        self.assertEqual('', repr(linked_list))
        linked_list.insert(0)
        linked_list.insert(1)
        self.assertEqual('1->0', repr(linked_list))
        linked_list.delete()
        self.assertEqual('0', repr(linked_list))
        linked_list.delete()
        self.assertEqual('', repr(linked_list))
        with self.assertRaises(ValueError) as ctx_mgm:
            linked_list.delete()
        self.assertEqual('List is empty', str(ctx_mgm.exception))

    def test_search_node_data(self):
        '''
        Test Singly Linked List search node operation
        '''
        linked_list = LinkedList()
        self.assertIsNone(linked_list.search(0))
        linked_list.insert(0)
        linked_list.insert(1)
        linked_list.insert(2)
        self.assertEqual(0, linked_list.search(2))
        self.assertEqual(1, linked_list.search(1))
        self.assertEqual(2, linked_list.search(0))

    def test_delete_node_at_index(self):
        '''
        Test Singly Linked List delete at index node operation
        '''
        linked_list = LinkedList()
        with self.assertRaises(ValueError) as ctx_mgm:
            linked_list.delete_at_index(1)
        self.assertEqual('List is empty', str(ctx_mgm.exception))
        linked_list.insert(0)
        linked_list.insert(1)
        linked_list.insert(2)
        self.assertEqual('2->1->0', repr(linked_list))
        with self.assertRaises(ValueError) as ctx_mgm:
            linked_list.delete_at_index(3)
        self.assertEqual("Couldn't find node at index 3", str(ctx_mgm.exception))
        linked_list.delete_at_index(2)
        self.assertEqual('2->1', repr(linked_list))
        linked_list.delete_at_index(0)
        self.assertEqual('1', repr(linked_list))

if __name__ == '__main__': # pragma: no cover
    unittest.main()
