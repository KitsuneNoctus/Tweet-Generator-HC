#!python

from linkedlist import LinkedList


class HashTable(object):

    def __init__(self, init_size=8):
        """Initialize this hash table with the given initial size."""
        # Create a new list (used as fixed-size array) of empty linked lists
        self.buckets = [LinkedList() for _ in range(init_size)]

    def __str__(self):
        """Return a formatted string representation of this hash table."""
        items = ['{!r}: {!r}'.format(key, val) for key, val in self.items()]
        return '{' + ', '.join(items) + '}'

    def __repr__(self):
        """Return a string representation of this hash table."""
        return 'HashTable({!r})'.format(self.items())

    def _bucket_index(self, key):
        """Return the bucket index where the given key would be stored."""
        # Calculate the given key's hash code and transform into bucket index
        return hash(key) % len(self.buckets)

    def keys(self):
        """Return a list of all keys in this hash table.
        TODO: Running time: O(???) Why and under what conditions?
        - O(n^2), When it runs it will go through two For loops. Loop into a loop"""
        # Collect all keys in each bucket
        all_keys = []
        for bucket in self.buckets:
            for key, value in bucket.items():
                all_keys.append(key)
        return all_keys

    def values(self):
        """Return a list of all values in this hash table.
        TODO: Running time: O(???) Why and under what conditions?
        - O(n^2), when called it goes though all items in the HashTable
        first getting to the index of the bucket, then going through each item in the linked
        list associated with that bucket"""
        # TODO: Loop through all buckets
        # TODO: Collect all values in each bucket
        all_values = []
        for bucket in self.buckets:
            for key, value in bucket.items():
                all_values.append(value)
        return all_values

    def items(self):
        """Return a list of all items (key-value pairs) in this hash table.
        TODO: Running time: O(???) Why and under what conditions?
        - O(n)
        - Goes through each index in the list, and get all items from the bucket"""
        # Collect all pairs of key-value entries in each bucket
        all_items = []
        for bucket in self.buckets:
            all_items.extend(bucket.items())
        return all_items

    def length(self):
        """Return the number of key-value entries by traversing its buckets.
        TODO: Running time: O(???) Why and under what conditions?
        - Run time: O(n)
        - go through each item in the bucket list and it calls the length function of each linked list, only then needed the single for
        loop as a result"""
        # TODO: Loop through all buckets
        # TODO: Count number of key-value entries in each bucket
        count = 0
        for bucket in self.buckets:
            count += bucket.length()
        return count

    def contains(self, key):
        """Return True if this hash table contains the given key, or False.
        TODO: Running time: O(???) Why and under what conditions?
        - O(1) or O(L)
        - Best scenario, the item contained is in the first item of the bucket.
        - Average Case: Full load factor must be run through (n/b) in order to check each of the values
        in each bucket"""
        # TODO: Find bucket where given key belongs
        # TODO: Check if key-value entry exists in bucket
        #reference to https://github.com/BriantOliveira/Computer_Science_2/blob/master/hashtable.py
        index = self._bucket_index(key)
        bucket = self.buckets[index]
        # data = self.buckets[index]
        data = bucket.find(lambda item: item [0] == key)
        return data is not None


    def get(self, key):
        """Return the value associated with the given key, or raise KeyError.
        TODO: Running time: O(???) Why and under what conditions?
        - O(1) or O(L)
        - Best time: Finds the value at the head of the bucket related to the hash/index key
        - Average: Must go through the load in order to find the item.
        """
        # TODO: Find bucket where given key belongs
        index = self._bucket_index(key)
        bucket = self.buckets[index]
        # TODO: Check if key-value entry exists in bucket
        node = bucket.find(lambda item: item [0] == key)
        # TODO: If found, return value associated with given key
        # TODO: Otherwise, raise error to tell user get failed
        # Hint: raise KeyError('Key not found: {}'.format(key))
        if node is not None:
            return node[1]
        else:
            raise KeyError(f'Key Not Found: {key}')

    def set(self, key, value):
        """Insert or update the given key with its associated value.
        TODO: Running time: O(???) Why and under what conditions?
        - O(1) or O(L)
        - Best time: Will get the bucket and a node assciated with it to deposit the info in if its new
        - Average: Will go through the load to find where the data is stored before deleting and refilling the spot"""
        # TODO: Find bucket where given key belongs
        # TODO: Check if key-value entry exists in bucket
        # TODO: If found, update value associated with given key
        # TODO: Otherwise, insert given key-value entry into bucket
        index = self._bucket_index(key)
        bucket = self.buckets[index]
        node = bucket.find(lambda item: item [0] == key)

        if node is not None:
            bucket.delete(node)
        bucket.append((key, value))

    def delete(self, key):
        """Delete the given key from this hash table, or raise KeyError.
        TODO: Running time: O(???) Why and under what conditions?
        - O(1) or O(L)
        - Best time: gets the bucket that hash is related to, and the item is first(at the head)
        - Average: It will need to run through the full load of items in the hashtable,
        can run to the end if the item doesn't exist."""
        # TODO: Find bucket where given key belongs
        index = self._bucket_index(key)
        bucket = self.buckets[index]
        # TODO: Check if key-value entry exists in bucket
        node = bucket.find(lambda item: item [0] == key)
        # TODO: If found, delete entry associated with given key
        if node is not None:
            bucket.delete(node)
        else:
            raise KeyError(f'Key not found: {key}')
        # TODO: Otherwise, raise error to tell user delete failed
        # Hint: raise KeyError('Key not found: {}'.format(key))


def test_hash_table():
    ht = HashTable()
    print('hash table: {}'.format(ht))

    print('\nTesting set:')
    for key, value in [('I', 1), ('V', 5), ('X', 10)]:
        print('set({!r}, {!r})'.format(key, value))
        ht.set(key, value)
        print('hash table: {}'.format(ht))

    print('\nTesting get:')
    for key in ['I', 'V', 'X']:
        value = ht.get(key)
        print('get({!r}): {!r}'.format(key, value))

    print('contains({!r}): {}'.format('X', ht.contains('X')))
    print('length: {}'.format(ht.length()))

    # Enable this after implementing delete method
    delete_implemented = False
    if delete_implemented:
        print('\nTesting delete:')
        for key in ['I', 'V', 'X']:
            print('delete({!r})'.format(key))
            ht.delete(key)
            print('hash table: {}'.format(ht))

        print('contains(X): {}'.format(ht.contains('X')))
        print('length: {}'.format(ht.length()))


if __name__ == '__main__':
    test_hash_table()
