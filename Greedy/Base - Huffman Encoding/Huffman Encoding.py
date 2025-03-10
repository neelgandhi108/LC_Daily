class Node:
    def __init__(self, freq, symbol, left=None, right=None):
        # frequency of symbol
        self.freq = freq
        # symbol name (character)
        self.symbol = symbol
        # node left of current node
        self.left = left
        # node right of current node
        self.right = right
        # tree direction (0/1)
        self.huff = ''

    def __lt__(self, nxt):
        return self.freq < nxt.freq


# utility function to print huffman codes
def print_nodes(node, val=''):
    # huffman code for current node
    new_val = val + str(node.huff)

    # if node is not an edge node then traverse inside it
    if node.left:
        print_nodes(node.left, new_val)
    if node.right:
        print_nodes(node.right, new_val)

    # if node is edge node then display its huffman code
    if not node.left and not node.right:
        print(f"{node.symbol} -> {new_val}")


def huffman_encoding(data):
    # calculate frequency of each character
    frequency = {}
    for char in data:
        if char in frequency:
            frequency[char] += 1
        else:
            frequency[char] = 1

    # sort frequency dictionary
    sorted_freq = sorted(frequency.items(), key=lambda x: x[1])

    nodes = []

    # create a leaf node for each character and add it to the nodes list
    for char, freq in sorted_freq:
        nodes.append(Node(freq, char))

    # while there is more than one node in the queue
    while len(nodes) > 1:
        # sort all the nodes in ascending order based on their frequency
        nodes = sorted(nodes, key=lambda x: x.freq)

        # pick two smallest nodes
        left = nodes[0]
        right = nodes[1]

        # assign directional value to these nodes
        left.huff = 0
        right.huff = 1

        # combine the two smallest nodes to create new node
        newNode = Node(left.freq + right.freq, left.symbol + right.symbol, left, right)

        # remove the two nodes and add their parent as new node
        nodes.remove(left)
        nodes.remove(right)
        nodes.append(newNode)

    # huffman tree is ready, print codes
    print("Huffman Codes:")
    print_nodes(nodes[0])

    # create a mapping of character to its huffman code
    huffman_code = {}

    def generate_codes(node, val=''):
        new_val = val + str(node.huff)
        if node.left:
            generate_codes(node.left, new_val)
        if node.right:
            generate_codes(node.right, new_val)
        if not node.left and not node.right:
            huffman_code[node.symbol] = new_val

    generate_codes(nodes[0])

    # encode the input text
    encoded_output = ""
    for char in data:
        encoded_output += huffman_code[char]

    return encoded_output, nodes[0]


def huffman_decoding(encoded_data, huffman_tree):
    decoded_output = ""
    current_node = huffman_tree

    for bit in encoded_data:
        # traverse the huffman tree
        if bit == '0':
            current_node = current_node.left
        else:
            current_node = current_node.right

        # check if reached leaf node
        if not current_node.left and not current_node.right:
            decoded_output += current_node.symbol
            current_node = huffman_tree

    return decoded_output


# Example usage
if __name__ == "__main__":
    data = "this is an example for huffman encoding"
    print(f"Original string: {data}")

    # encoding
    encoded_data, huffman_tree = huffman_encoding(data)
    print(f"Encoded string: {encoded_data}")

    # decoding
    decoded_data = huffman_decoding(encoded_data, huffman_tree)
    print(f"Decoded string: {decoded_data}")

    # calculate compression ratio
    original_bits = len(data) * 8  # assuming 8 bits per character
    compressed_bits = len(encoded_data)
    compression_ratio = original_bits / compressed_bits
    print(f"Compression ratio: {compression_ratio:.2f}")