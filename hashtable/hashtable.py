class HashTableEntry:
    """
    Linked List hash table key/value pair
    """

    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None


# Hash table can't have fewer than this many slots
MIN_CAPACITY = 8


class HashTable:
    """
    A hash table that with `capacity` buckets
    that accepts string keys

    Implement this.
    """

    def __init__(self, capacity):
        self.capacity = capacity
        self.hash_data = [None] * capacity

    def get_num_slots(self):
        return self.capacity

    def get_load_factor(self):
        """
        Return the load factor for this hash table.

        Implement this.
        """
        # Your code here
        pass

    def djb2(self, key):

        hash = 5381

        for s in key:
            hash = ((( hash << 5) + hash) + ord(s))
        return hash

        # hash = 0

        # for s in key:
        #     hash = ((hash << 16) + (hash << 6) + ord(s) - hash)
        # return hash

    def hash_index(self, key):
        """
        Take an arbitrary key and return a valid integer index
        between within the storage capacity of the hash table.
        """
        # return self.fnv1(key) % self.capacity
        return self.djb2(key) % self.capacity

    def put(self, key, value):
        index = self.hash_index(key)
        new_node = HashTableEntry(key, value)
        current = self.hash_data[index]
        prev = None

        if current:
            while current is not None:
                if current.key == key:
                    current.value = value
                prev = current
                current = current.next
            prev.next = new_node
        else:
            self.hash_data[index] = new_node

    def delete(self, key):
        index = self.hash_index(key)
        current = self.hash_data[index]
        prev = None
        
        while current is not None:
            if current.key == key:
                if prev:
                    prev.next = current.next
                else:
                    self.hash_data[index] = current.next
            prev = current
            current = current.next

    def get(self, key):
        index = self.hash_index(key)
        current = self.hash_data[index]
        
        while current is not None:
            if current.key == key:
                return current.value
            current = current.next
        return None

    def resize(self, new_capacity):
        """
        Changes the capacity of the hash table and
        rehashes all key/value pairs.

        Implement this.
        """
        # Your code here
        pass


if __name__ == "__main__":
    ht = HashTable(8)

    ht.put("line_1", "'Twas brillig, and the slithy toves")
    ht.put("line_2", "Did gyre and gimble in the wabe:")
    ht.put("line_3", "All mimsy were the borogoves,")
    ht.put("line_4", "And the mome raths outgrabe.")
    ht.put("line_5", '"Beware the Jabberwock, my son!')
    ht.put("line_6", "The jaws that bite, the claws that catch!")
    ht.put("line_7", "Beware the Jubjub bird, and shun")
    ht.put("line_8", 'The frumious Bandersnatch!"')
    ht.put("line_9", "He took his vorpal sword in hand;")
    ht.put("line_10", "Long time the manxome foe he sought--")
    ht.put("line_11", "So rested he by the Tumtum tree")
    ht.put("line_12", "And stood awhile in thought.")

    print("")

    # Test storing beyond capacity
    for i in range(1, 13):
        print(ht.get(f"line_{i}"))

    # Test resizing
    old_capacity = ht.get_num_slots()
    ht.resize(ht.capacity * 2)
    new_capacity = ht.get_num_slots()

    print(f"\nResized from {old_capacity} to {new_capacity}.\n")

    # Test if data intact after resizing
    for i in range(1, 13):
        print(ht.get(f"line_{i}"))

    print("")
