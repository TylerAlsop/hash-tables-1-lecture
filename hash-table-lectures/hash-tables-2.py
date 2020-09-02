class HashTableEntry:
    """
    Hash Table entry, as a linked list node.
    """

    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None


class HashTable:
    """
    A hash table that with `capacity` buckets
    that accepts string keys
    Implement this.
    """

    def __init__(self, capacity):
        self.capacity = capacity  # Number of buckets in the hash table
        self.hash_table = [None] * capacity
        self.initial_capacity = capacity
        self.number_of_items = 0

    def fnv1(self, key):
        """
        FNV-1 64-bit hash function
        For 64-bit:
            FNV_prime = 2^40 + 2^8 + 0xb3
            offset_basis = 14695981039346656037
        XOR operator ^
        hash = offset_basis
        for each octet_of_data to be hashed
            hash = hash * FNV_prime
            hash = hash xor octet_of_data
        return hash
        Implement this, and/or DJB2.
        """
        FNV_prime = 2**40 + 2**8 + 0xb3
        hash = 14695981039346656037
        for x in key:
            hash = hash * FNV_prime
            hash = hash ^ ord(x)
        return hash & 0xFFFFFFFFFFFFFFFF

    def djb2(self, key):
        """
        DJB2 32-bit hash function
        Implement this, and/or FNV-1.
        """
        hash = 5381
        for x in key:
            hash = ((hash << 5) + hash) + ord(x)
        return hash & 0xFFFFFFFF

    def _hash_index(self, key):
        """
        Take an arbitrary key and return a valid integer index
        between within the hash_table capacity of the hash table.
        """
        # return self.fnv1(key) % self.capacity
        return self.djb2(key) % self.capacity

    def put(self, key, value):
        """
        Store the value with the given key.
        Hash collisions should be handled with Linked List Chaining.
        Implement this.
        """
        self.size_check()

        index = self._hash_index(key)
        new_entry = HashTableEntry(key, value)

        node = self.hash_table[index]
        if node is None:
            self.hash_table[index] = new_entry
            self.number_of_items += 1
            return

        while node is not None and node.key != key:
            prev = node
            node = node.next

        if node is None:
            prev.next = new_entry
            self.number_of_items += 1

        else:
            # The key was found, so update the value
            node.value = value

    def delete(self, key):
        """
        Remove the value stored with the given key.
        Print a warning if the key is not found.
        Implement this.
        """
        # Get the index.
        index = self._hash_index(key)

        # Get the value stored in hash_table at that index.
        node = self.hash_table[index]

        # If that node is the desired one, point the hash_table[index] to its next.
        if node.key == key:
            self.hash_table[index] = node.next
            self.number_of_items -= 1
            self.size_check()
            return

        # Traverse the LL until the key is found or the end of the LL is reached.

        while node is not None and node.key != key:
            prev = node
            node = node.next

        if node is None:
            print(f'{key} was not found')
            return None
        # Remove the LinkedPair node from the chain by assigning
        # the .next pointer of the previous node to be the node that its .next pointer was pointing to.
        prev.next = node.next
        self.number_of_items -= 1
        self.size_check()

    def get(self, key):
        """
        Retrieve the value stored with the given key.
        Returns None if the key is not found.
        Implement this.
        """
        # Compute hash
        index = self._hash_index(key)

        # Get the first node in LL in hash_table
        node = self.hash_table[index]

        # Traverse the linked list at this node until the key is found or the end is reached
        while node is not None and node.key != key:
            node = node.next

        if node is None:
            return None
        else:
            return node.value

    def make_new_hash_table(self):
        new_hash_table = [None] * self.capacity

        for i in range(len(self.hash_table)):
            # print(f'at index {i} in self.hash_table')
            node = self.hash_table[i]

            while node is not None:
                # traverse the LL to rehash each key/value pair
                # print("At key: " + str(node.key))
                index = self._hash_index(node.key)
                new_hash_table[index] = node
                node = node.next
        self.hash_table = new_hash_table

    def resize(self):
        """
        Doubles the capacity of the hash table and
        rehash all key/value pairs.
        """
        self.capacity = self.capacity * 2
        self.make_new_hash_table()

    def shrink(self):
        '''
        Halves the capacity of the hash table and
        rehashes all key/value pairs.
        '''
        self.capacity = self.capacity // 2
        self.make_new_hash_table()

    def size_check(self):
        '''
        Update your HashTable to automatically double in size when it grows past a load factor of 0.7
        and half in size when it shrinks past a load factor of 0.2.
        This (I assume the halving) should only occur 
        if the HashTable has been resized past the initial size.
        '''
        # num_entries = sum(x is not None for x in self.hash_table)
        # print('num_entries: ' + str(num_entries))
        # load_factor = num_entries/self.capacity
        load_factor = self.number_of_items/self.capacity
        # print('load factor: ' + str(load_factor))

        if load_factor > 0.7:
            # print('Time to increase the capacity; load factor is ' + str(load_factor))
            self.resize()

        if self.capacity > self.initial_capacity:
            if load_factor < 0.2 and self.capacity // 2 >= 8:  # 128
                # print('time to shrink the hashtable in half')
                self.shrink()


if __name__ == "__main__":
    ht = HashTable(2)

    ht.put("line_1", "Tiny hash table")
    ht.put("line_2", "Filled beyond capacity")
    ht.put("line_3", "Linked list saves the day!")

    print("")

    # Test storing beyond capacity
    print(ht.get("line_1"))
    print(ht.get("line_2"))
    print(ht.get("line_3"))

    # Test resizing
    old_capacity = len(ht.hash_table)
    ht.resize()
    new_capacity = len(ht.hash_table)

    print(f"\nResized from {old_capacity} to {new_capacity}.\n")

    # Test if data intact after resizing
    print(ht.get("line_1"))
    print(ht.get("line_2"))
    print(ht.get("line_3"))

    print("")

    print(ht.fnv1("hello"))