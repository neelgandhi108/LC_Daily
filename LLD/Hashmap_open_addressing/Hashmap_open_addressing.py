class HashMapBase:
    """Base class for hash map implementations."""

    def __init__(self, capacity=11, load_factor=0.7):
        self.capacity = capacity
        self.size = 0
        self.load_factor = load_factor
        self.table = [None] * capacity
        self.DELETED = object()  # Sentinel for deleted entries

    def _hash(self, key):
        """Primary hash function."""
        return hash(key) % self.capacity

    def _is_full(self):
        """Check if load factor threshold has been reached."""
        return self.size / self.capacity >= self.load_factor

    def _resize(self, new_capacity):
        """Resize the hash table."""
        old_table = self.table
        self.table = [None] * new_capacity
        self.capacity = new_capacity
        self.size = 0

        # Rehash all entries
        for entry in old_table:
            if entry is not None and entry is not self.DELETED:
                key, value = entry
                self.put(key, value)

    def get(self, key):
        """Get the value associated with the key."""
        index = self._find_slot(key)
        if index is None or self.table[index] is None or self.table[index] is self.DELETED:
            return None
        return self.table[index][1]

    def put(self, key, value):
        """Insert or update a key-value pair."""
        if self._is_full():
            self._resize(2 * self.capacity + 1)

        index = self._find_slot(key)
        if index is None:
            return False

        entry = (key, value)
        if self.table[index] is None or self.table[index] is self.DELETED:
            self.size += 1
        self.table[index] = entry
        return True

    def remove(self, key):
        """Remove the key-value pair with the given key."""
        index = self._find_slot(key)
        if index is None or self.table[index] is None or self.table[index] is self.DELETED:
            return False

        self.table[index] = self.DELETED
        self.size -= 1
        return True

    def __len__(self):
        """Return the number of entries in the map."""
        return self.size

    def __contains__(self, key):
        """Check if the map contains the key."""
        return self.get(key) is not None

    def _find_slot(self, key):
        """Find the slot for a key. To be implemented by subclasses."""
        raise NotImplementedError("Subclass must implement _find_slot")


class LinearProbingHashMap(HashMapBase):
    """Hash map implementation using linear probing for collision resolution."""

    def _find_slot(self, key):
        """Find slot for the key using linear probing."""
        start = self._hash(key)

        # Linear probing
        for i in range(self.capacity):
            index = (start + i) % self.capacity
            entry = self.table[index]

            # Empty slot or matching key
            if entry is None:
                return index
            if entry is self.DELETED:
                continue
            if entry[0] == key:
                return index

        return None  # Table is completely full with different keys


class QuadraticProbingHashMap(HashMapBase):
    """Hash map implementation using quadratic probing for collision resolution."""

    def _find_slot(self, key):
        """Find slot for the key using quadratic probing."""
        start = self._hash(key)

        # Quadratic probing: h(k, i) = (h(k) + c1*i + c2*i^2) % m
        # Here we use c1=1, c2=1 for simplicity
        for i in range(self.capacity):
            # This is actually a quadratic, not quartic, probing formula
            index = (start + i + i * i) % self.capacity
            entry = self.table[index]

            # Empty slot or matching key
            if entry is None:
                return index
            if entry is self.DELETED:
                continue
            if entry[0] == key:
                return index

        return None  # Table is completely full with different keys


class DoubleHashingHashMap(HashMapBase):
    """Hash map implementation using double hashing for collision resolution."""

    def _hash2(self, key):
        """Secondary hash function for double hashing."""
        # Common secondary hash function: 1 + (key % (capacity - 2))
        # Ensures step size is relatively prime to capacity (when capacity is prime)
        return 1 + (hash(key) % (self.capacity - 2))

    def _find_slot(self, key):
        """Find slot for the key using double hashing."""
        h1 = self._hash(key)
        h2 = self._hash2(key)

        # Double hashing: h(k, i) = (h1(k) + i * h2(k)) % m
        for i in range(self.capacity):
            index = (h1 + i * h2) % self.capacity
            entry = self.table[index]

            # Empty slot or matching key
            if entry is None:
                return index
            if entry is self.DELETED:
                continue
            if entry[0] == key:
                return index

        return None  # Table is completely full with different keys


# Example usage
def test_hashmap(hashmap_class):
    print(f"\nTesting {hashmap_class.__name__}:")
    hashmap = hashmap_class()

    # Insert key-value pairs
    hashmap.put("one", 1)
    hashmap.put("two", 2)
    hashmap.put("three", 3)

    # Retrieve values
    print(f"Value for 'one': {hashmap.get('one')}")
    print(f"Value for 'two': {hashmap.get('two')}")
    print(f"Value for 'unknown': {hashmap.get('unknown')}")

    # Update value
    hashmap.put("one", 100)
    print(f"Updated value for 'one': {hashmap.get('one')}")

    # Check size
    print(f"Size: {len(hashmap)}")

    # Remove a key
    hashmap.remove("two")
    print(f"After removing 'two', value: {hashmap.get('two')}")
    print(f"Size after removal: {len(hashmap)}")

    # Add many values to trigger resize
    for i in range(10):
        hashmap.put(f"key{i}", i)

    print(f"Size after adding 10 more entries: {len(hashmap)}")
    print(f"Capacity after resize: {hashmap.capacity}")


# Run tests
if __name__ == "__main__":
    test_hashmap(LinearProbingHashMap)
    test_hashmap(QuadraticProbingHashMap)
    test_hashmap(DoubleHashingHashMap)