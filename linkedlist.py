#!python


class Node(object):

    def __init__(self, data):
        """Initialize this node with the given data."""
        self.data = data
        self.next = None

    def __repr__(self):
        """Return a string representation of this node."""
        return 'Node({!r})'.format(self.data)


class LinkedList(object):

    def __init__(self, items=None):
        """Initialize this linked list and append the given items, if any."""
        self.head = None  # First node
        self.tail = None  # Last node
        # Append given items
        if items is not None:
            for item in items:
                self.append(item)

    def __str__(self):
        """Return a formatted string representation of this linked list."""
        items = ['({!r})'.format(item) for item in self.items()]
        return '[{}]'.format(' -> '.join(items))

    def __repr__(self):
        """Return a string representation of this linked list."""
        return 'LinkedList({!r})'.format(self.items())

    def items(self):
        """Return a list (dynamic array) of all items in this linked list.
        Best and worst case running time: O(n) for n items in the list (length)
        because we always need to loop through all n nodes to get each item."""
        items = []  # O(1) time to create empty list
        # Start at head node
        node = self.head  # O(1) time to assign new variable
        # Loop until node is None, which is one node too far past tail
        while node is not None:  # Always n iterations because no early return
            items.append(node.data)  # O(1) time (on average) to append to list
            # Skip to next node to advance forward in linked list
            node = node.next  # O(1) time to reassign variable
        # Now list contains items from all nodes
        return items  # O(1) time to return list

    def is_empty(self):
        """Return a boolean indicating whether this linked list is empty."""
        return self.head is None

    def length(self):
        """Return the length of this linked list by traversing its nodes.
        TODO: Running time: O(???) Why and under what conditions?
        - O(n) Due to looping though code by for loop to check each node"""
        # TODO: Loop through all nodes and count one for each
        count = 0
        node = self.head
        while node is not None:
            count += 1
            # Skip to next node to advance forward in linked list
            node = node.next
        return count

    def append(self, item):
        """Insert the given item at the tail of this linked list.
        TODO: Running time: O(???) Why and under what conditions?
        - O(1) runs single moment when one item"""
        # TODO: Create new node to hold given item
        new_node = Node(item)
        # TODO: Append node after tail, if it exists
        if self.is_empty() is True:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        # self.append(new_node)

    def prepend(self, item):
        """Insert the given item at the head of this linked list.
        TODO: Running time: O(???) Why and under what conditions?
        - O(1) because its not looping and checks code once"""
        # TODO: Create new node to hold given item
        new_node = Node(item)
        # TODO: Prepend node before head, if it exists
        if self.head is not None:
            new_node.next = self.head
            self.head = new_node
        else:
            self.head = new_node
            self.tail = new_node

    def find(self, quality):
        """Return an item from this linked list satisfying the given quality.
        TODO: Best case running time: O(???) Why and under what conditions?
        - O(n)
        TODO: Worst case running time: O(???) Why and under what conditions?
        - O(n)"""

        # TODO: Loop through all nodes to find item where quality(item) is True
        # TODO: Check if node's data satisfies given quality function
        node = self.head
        while node is not None:
            if quality(node.data) == True:
                return node.data
            else:
                node = node.next
        else:
            return None


    def delete(self, item):
        """Delete the given item from this linked list, or raise ValueError.
        TODO: Best case running time: O(???) Why and under what conditions?
        - O(n) To check through each item in the list and get each node to test
        TODO: Worst case running time: O(???) Why and under what conditions?
        - O(n)"""
        # TODO: Loop through all nodes to find one whose data matches given item
        # TODO: Update previous node to skip around node with matching data
        # TODO: Otherwise raise error to tell user that delete has failed
        # Hint: raise ValueError('Item not found: {}'.format(item))

        node = self.head
        previous_node = None

        while node is not None:
            if node.data == item:
                #Used Diyar Kudrat reference. This erases the head.
                if previous_node == None:
                    self.head = node.next
                    if node.next == None:
                        self.tail = None
                #Gets rid of tail. Also with help from Diyar
                elif node.next == None:
                    previous_node.next = None
                    self.tail = previous_node
                else:
                    ''' Gets rid of the current node by switching the previous nodes
                    next reference to the current nodes next reference, thus removing any
                    reference of the node the was just in between.'''
                    previous_node.next = node.next

        #------------My own attempts before reference\ing or help------------------------
                # if node.next == None:
                #     '''If there is only the single item.'''
                #     self.head = None
                #     self.tail = None
                #
                # elif previous_node == None:
                #     pass
                    # if node.next == None:
                    #     self.head = None
                    #     self.tail = None
                    # else:
                    #     self.head = node.next
            #---------------------------------------
                # # if self.length() == 1:
                # #     self.head = None
                # #     self.tail = None
                # if node == self.head:
                #     self.head = node.next
                # elif node == self.tail:
                #     self.tail = previous_node
                # else:
                #     previous_node.next = current_node.next
                return
            else:
                previous_node = node
                node = node.next

        raise ValueError(f'Item not found: {item}')




def test_linked_list():
    ll = LinkedList()
    print('list: {}'.format(ll))

    print('\nTesting append:')
    for item in ['A', 'B', 'C']:
        print('append({!r})'.format(item))
        ll.append(item)
        print('list: {}'.format(ll))

    print('head: {}'.format(ll.head))
    print('tail: {}'.format(ll.tail))
    print('length: {}'.format(ll.length()))

    # Enable this after implementing delete method
    delete_implemented = False
    if delete_implemented:
        print('\nTesting delete:')
        for item in ['B', 'C', 'A']:
            print('delete({!r})'.format(item))
            ll.delete(item)
            print('list: {}'.format(ll))

        print('head: {}'.format(ll.head))
        print('tail: {}'.format(ll.tail))
        print('length: {}'.format(ll.length()))


if __name__ == '__main__':
    test_linked_list()
