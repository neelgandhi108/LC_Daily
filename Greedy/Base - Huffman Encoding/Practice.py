import heapq
from collections import defaultdict

class Node:
    def __init__(self, freq, symbol, left=None, right=None):
        self.freq = freq
        self.symbol = symbol
        self.left = left
        self.right = right
        self.huff = ''

    def __lt__(self, other):
        return self.freq < other.freq


class HuffmanCoding:
    def __init__(self, data):
        self.data = data
        self.huffman_tree = None
        self.huffman_codes = {}

    def build_frequency_table(self):
        """Build frequency table from input data."""
        """
        Iterate over character in data
        Maintaining freq table for data
        """
        freq_table = collections.defaultdict(int)
        for ch in self.data:
            freq_table[ch] =  1+ freq_table.get(ch,0)
        return freq_table

    def build_huffman_tree(self):
        """Construct Huffman Tree using priority queue."""
        """
        00 01 10 11 Huff tree by extracting max freq from min heap
        """
        freq_table = self.build_frequency_table()
        min_heap = []


    def generate_codes(self, node, val=''):
        """Generate Huffman codes from the Huffman Tree."""
        pass

    def encode(self):
        """Encode the input data using Huffman codes."""
        pass

    def decode(self, encoded_data):
        """Decode the encoded data using the Huffman Tree."""
        pass


# Example usage
if __name__ == "__main__":
    data = "your sample input here"
    huffman = HuffmanCoding(data)

    # Build Huffman tree and encode data
    encoded_data = huffman.encode()
    print(f"Encoded Data: {encoded_data}")

    # Decode the encoded data
    decoded_data = huffman.decode(encoded_data)
    print(f"Decoded Data: {decoded_data}")
