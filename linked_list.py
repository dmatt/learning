"""Linked list with printing to show how it works"""

class LinkedList:
    """Linked list data type"""
    empty = ()

    def __init__(self):
        self.head = self.empty

    def append(self, data):
        """Appends node to LinkedList"""
        # create a new Node instance with data
        new_node = Node(data)
        # empty linked list case, give head the first node instance
        if self.head is self.empty:
            self.head = new_node
            return
        # Start at head node and traverse until next is empty (tail)
        curr_node = self.head
        while curr_node.next:
            curr_node = curr_node.next
        # We are at the tail_node, append new_node to next
        tail_node = curr_node
        tail_node.next = new_node

    def prepend(self, data):
        """insert a new node containing data after a node provided"""
        # create a new Node instance with data
        new_node = Node(data)
        # Give new node old head, and reassign head
        new_node.next = self.head
        self.head = new_node

    def insert_after(self, after_node, data):
        """insert a new node containing data after a node provided"""
        # Start at head node
        curr_node = self.head
        # Create a new Node instance with data
        new_node = Node(data)
        #  Traverse until next is empty (tail)
        while curr_node.next:
            #  if we see a curr_node that matches, update next pointers
            if curr_node == after_node:
                new_node.next = after_node.next
                after_node.next = new_node
                return
            curr_node = curr_node.next
        #  after_node did not match any nodes in linked list
        print('after_node containing \"%s\" doesn\'t exist in linked list' % after_node.data)
        return

    def delete_node(self, key):
        """Delete node containing the key provided"""
        curr_node = self.head
        # When head is the matching node to delete
        if curr_node and curr_node.data == key:
            self.head = curr_node.next
            print('deleting %s' % curr_node)
            curr_node = self.empty
            return
        # Traverse through all nodes to delete node with matching key
        while curr_node.next:
            #  if we see that the next node matches, update pointers for deletion
            if curr_node.next.data == key:
                deletion_target = curr_node.next
                curr_node.next = curr_node.next.next
                print('deleting %s' % deletion_target)
                deletion_target = self.empty
                return
            curr_node = curr_node.next
        #  key did not match any nodes in linked list
        print('key \"%s\" doesn\'t exist in linked list' % key)

    def reverse_iterative(self):
        """Revereses linked list and updates pointers"""
        prev_node = self.empty
        curr_node = self.head
        while curr_node:
            nxt = curr_node.next
            curr_node.next = prev_node
            prev_node = curr_node
            curr_node = nxt
        self.head = prev_node
        return self

    def __str__(self):
        curr_node = self.head
        ll_string = str()
        while curr_node:
            ll_string += " %s " % str(curr_node.data)
            curr_node = curr_node.next
        return "<%s>" % ll_string

class Node():
    """Node for a linked list"""
    empty = ()

    def __init__(self, data):
        self.data = data
        self.next = self.empty

if __name__ == "__main__":
    LINKED_LIST = LinkedList()
    LINKED_LIST.append(1)
    LINKED_LIST.append(2)
    LINKED_LIST.append(3)
    LINKED_LIST.prepend('string 3')
    LINKED_LIST.prepend('string 2')
    LINKED_LIST.prepend('string 1')
    NODE_1 = LINKED_LIST.head.next.next.next
    NODE_LONER = Node('lone wolf')
    LINKED_LIST.insert_after(NODE_1, 'should be inserted after int 1')
    LINKED_LIST.insert_after(NODE_LONER, 'should not be inserted')
    LINKED_LIST.delete_node('string 1')
    LINKED_LIST.delete_node(3)
    print(LINKED_LIST)

    LINKED_LIST_TO_REVERSE = LinkedList()
    LINKED_LIST_TO_REVERSE.append(1)
    LINKED_LIST_TO_REVERSE.append(2)
    LINKED_LIST_TO_REVERSE.append(3)
    LINKED_LIST_TO_REVERSE.append(4)
    LINKED_LIST_TO_REVERSE.append(5)
    LINKED_LIST_TO_REVERSE.append(6)
    print(LINKED_LIST_TO_REVERSE.reverse_iterative())
