"""Linked list with printing to show how it works"""

class LinkedList:
    """Linked list data type"""

    def __init__(self):
        self.head = None

    def append(self, data):
        """Appends node to LinkedList"""
        # create a new Node instance with data
        new_node = Node(data)
        # Empty linked list case, give head the first node instance
        if self.head is None:
            self.head = new_node
            return
        # Start at head node and traverse until next is None (tail)
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
        #  Traverse until next is None (tail)
        while curr_node.next:
            #  if we see a curr_node that matches, update next pointers
            if curr_node == after_node:
                new_node.next = after_node.next
                after_node.next = new_node
                return
            curr_node = curr_node.next
        #  after_node did not match any nodes in linked list
        print('after_node doesn\'t exist in linked list')
        return

    def __str__(self):
        curr_node = self.head
        ll_string = str()
        while curr_node:
            ll_string += " %s " % str(curr_node.data)
            curr_node = curr_node.next
        return "<%s>" % ll_string

class Node():
    """Node for a linked list"""
    def __init__(self, data):
        self.data = data
        self.next = None

if __name__ == "__main__":
    LINKED_LIST = LinkedList()
    LINKED_LIST.append(1)
    LINKED_LIST.append(2)
    LINKED_LIST.append(2)
    LINKED_LIST.append(7)
    LINKED_LIST.append(7)
    LINKED_LIST.prepend('ha3')
    LINKED_LIST.prepend('ha2')
    LINKED_LIST.prepend('ha1')
    NODE_1 = LINKED_LIST.head.next.next.next
    NODE_LONER = Node('lone wolf')
    LINKED_LIST.insert_after(NODE_1, 'lol-inserted-after-node_1')
    LINKED_LIST.insert_after(NODE_LONER, 'lol')
    print(LINKED_LIST)
