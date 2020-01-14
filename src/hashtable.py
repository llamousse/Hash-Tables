# '''
# Linked List hash table key/value pair
# '''
import types

class LinkedPair:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None


class HashTable:
    '''
    A hash table that with `capacity` buckets
    that accepts string keys
    '''

    def __init__(self, capacity):
        self.capacity = capacity  # Number of buckets in the hash table
        self.storage = [None] * capacity
        self.count = 0 # Count is how much is currently used

    def _hash(self, key):
        '''
        Hash an arbitrary key and return an integer.


        You may replace the Python hash with DJB2 as a stretch goal.
        '''
        return hash(key)

    # def _hash_djb2(self, key):
    #     '''
    #     Hash an arbitrary key using DJB2 hash

    #     OPTIONAL STRETCH: Research and implement DJB2
    #     '''
    #     pass

    def _hash_mod(self, key):
        '''
        Take an arbitrary key and return a valid integer index
        within the storage capacity of the hash table.
        '''
        return self._hash(key) % self.capacity

    def insert(self, key, value):
        '''
        Store the value with the given key.
        Hash collisions should be handled with Linked List Chaining.
        Fill this in.
        '''
        
        hashed_mod_key = self._hash_mod(key)

        if self.storage[hashed_mod_key]:
            next_link = LinkedPair(key, value)
            next_link.next = self.storage[hashed_mod_key]
            self.storage[hashed_mod_key] = next_link
        else:
            self.storage[hashed_mod_key] = LinkedPair(key, value)
            self.count += 1


    def remove(self, key):
        '''
        Remove the value stored with the given key.
        Print a warning if the key is not found.
        Fill this in.
        '''

        hashed_key = self._hash_mod(key)
        storage_key = self.storage[hashed_key]
        
        while storage_key is not None and storage_key.key != key:
            storage_key = storage_key.next
        if storage_key is None:
            return None
        else:
            self.count -= 1
            res = storage_key.value
            storage_key.value = None
        return res


    def retrieve(self, key):
        '''
        Retrieve the value stored with the given key.
        Returns None if the key is not found.
        Fill this in.
        '''
        
        hashedKey = self._hash_mod(key)
        currentKey = self.storage[hashedKey]

        while currentKey:
            if currentKey.key != key:
                currentKey = currentKey.next
            else:
                return currentKey.value
        return None

    def resize(self):
        '''
        Doubles the capacity of the hash table and
        rehash all key/value pairs.

        Fill this in.
        '''
        self.capacity *= 2
        new_storage = self.storage
        self.storage = [None] * self.capacity

        for key in new_storage:
            curr_key = key
            while curr_key:
                self.insert(curr_key.key, curr_key.value)
                curr_key = curr_key.next

if __name__ == "__main__":
    ht = HashTable(2)

    ht.insert("line_1", "Tiny hash table")
    ht.insert("line_2", "Filled beyond capacity")
    ht.insert("line_3", "Linked list saves the day!")

    print("")

    # Test storing beyond capacity
    print(ht.retrieve("line_1"))
    print(ht.retrieve("line_2"))
    print(ht.retrieve("line_3"))

    # Test resizing
    old_capacity = len(ht.storage)
    ht.resize()
    new_capacity = len(ht.storage)

    print(f"\nResized from {old_capacity} to {new_capacity}.\n")

    # Test if data intact after resizing
    print(ht.retrieve("line_1"))
    print(ht.retrieve("line_2"))
    print(ht.retrieve("line_3"))

    print("")