class FenwickTree:
    def __init__(self, n):
        """Initialize a Fenwick Tree with size n."""
        self.n = n
        self.fen = [0] * (n + 1)  # 1-indexed array

    def update(self, i, add):
        """Add 'add' to the element at index i and update the tree."""
        while i < self.n:
            self.fen[i] += add
            # The key operation: i += (i & -i)
            # This adds the rightmost set bit to i
            i += (i & -i)

    def sum(self, i):
        """Get the sum of all elements from index 1 to i inclusive."""
        s = 0
        while i > 0:
            s += self.fen[i]
            # The key operation: i -= (i & -i)
            # This removes the rightmost set bit from i
            i -= (i & -i)
        return s

    def range_sum(self, left, right):
        """Get the sum of elements from index left to right inclusive."""
        return self.sum(right) - self.sum(left - 1)

    def get_value(self, i):
        """Get the value at a specific index (for demonstration purposes)."""
        if i == 0:
            return 0
        # The value at index i is the range sum from i to i
        return self.range_sum(i, i)


# Example usage
def demonstrate_fenwick_tree():
    n = 10

    # Create a Fenwick Tree of size n
    bit = FenwickTree(n)

    # Insert some values
    print("Performing updates:")
    for i in range(1, n + 1):
        bit.update(i, i)  # Update index i with value i
        print(f"Updated index {i} with value {i}")

    # Print the tree array for demonstration
    print("\nInternal Fenwick Tree array (1-indexed):")
    for i in range(1, n + 1):
        print(f"fen[{i}] = {bit.fen[i]}")

    # Demonstrate prefix sums
    print("\nPrefix sums:")
    for i in range(1, n + 1):
        print(f"Sum(1...{i}) = {bit.sum(i)}")

    # Demonstrate range queries
    print("\nRange queries:")
    ranges = [(1, 3), (2, 7), (4, 9), (1, 10)]
    for left, right in ranges:
        print(f"Sum({left}...{right}) = {bit.range_sum(left, right)}")

    # Demonstrate updates
    print("\nUpdating values:")
    updates = [(2, 10), (5, 20), (8, -5)]
    for idx, val in updates:
        old_val = bit.get_value(idx)
        bit.update(idx, val)
        print(f"Updated index {idx} from {old_val} to {old_val + val}")

    # Show the new sums
    print("\nNew prefix sums after updates:")
    for i in range(1, n + 1):
        print(f"Sum(1...{i}) = {bit.sum(i)}")


if __name__ == "__main__":
    demonstrate_fenwick_tree()
