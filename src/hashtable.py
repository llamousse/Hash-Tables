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

    def _hash_djb2(self, key):
        '''
        Hash an arbitrary key using DJB2 hash

        OPTIONAL STRETCH: Research and implement DJB2
        '''
        pass

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
        
        hashed_mod_key = self._hash_mod(key)
        if self.storage[hashed_mod_key] == None:
            print('Key not found, cannot delete!')
        else:
            tempKey = 0
            currentKey = self.storage[hashed_mod_key]

            while currentKey:
                if currentKey.key == key:
                    if currentKey.next != None:
                        if temp == None:
                            self.storage[hashed_mod_key] = currentKey.next
                            self.count -= 1
                            return
                        else:
                            tempKey.next = currentKey.next
                            self.count -= 1
                            return
                    else:
                        if temp == None:
                            self.storage[hashed_mod_key] = None
                            self.count -= 1
                            return
                        else:
                            tempKey.next = None
                            self.count -= 1
                            return
                else:
                    tempKey = currentKey
                    currentKey = currentKey.next
            print('Key not found, cannot remove')

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
        pass


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


# lecture notes
#
# class DynamicArray:
#     def __init__(self, capacity=8):
#         self.count = 0  # Count is how much is currently used
#         self.capacity = capacity  # How much is currently allocated
#         self.storage = [None] * self.capacity

#     def insert(self, index, value):
#         if self.count == self.capacity:
#             self.resize()
#             return
#         # Shift everything to the right
#         for i in range(self.count, index, -1):
#             self.storage[i] = self.storage[i - 1]
#         # Insert our value
#         self.storage[index] = value
#         self.count += 1

#     def append(self, value):
#         self.insert(self.count, value)

#     def resize(self):
#         self.capacity *= 2
#         new_storage = [None] * self.capacity
#         for i in range(self.count):
#             new_storage[i] = self.storage[i]
#         self.storage = new_storage

#     def replace(self, index, value):
#         self.storage[index] = value

#     def add_to_front(self, value):
#         self.insert(0, value)

#     def slice(self, beginning_index, end_index):  # default value
#         # beginning and end
#         # create subarray to store value
#         # copy beginning  to end to subarray
#         # decide how this works.  What happens  to the original array?
#         # leave it alone?  Or cut out what  we're slicing
#         # return subarray
