import heapq

class Node:
    def __init__(self, char, freq):
        self.char = char
        self.freq = freq
        self.left = None
        self.right = None

    def __lt__(self, other):
        return self.freq < other.freq

def print_codes(node, code=""):
    if node is None:
        return
    if node.char is not None:
        print(f"{node.char}: {code}")
        return
    print_codes(node.left, code + "0")
    print_codes(node.right, code + "1")

def huffman_coding(chars, freqs):
    heap = [Node(chars[i], freqs[i]) for i in range(len(chars))]
    heapq.heapify(heap)
    while len(heap) > 1:
        left = heapq.heappop(heap)
        right = heapq.heappop(heap)
        merged = Node(None, left.freq + right.freq)
        merged.left = left
        merged.right = right
        heapq.heappush(heap, merged)
    root = heap[0]
    print("Character Codes from Huffman Tree:\n")
    print_codes(root)

if __name__ == "__main__":
    n = int(input("Enter number of characters: "))
    chars = []
    freqs = []
    for i in range(n):
        ch = input(f"Enter character {i+1}: ")
        fr = int(input(f"Enter frequency of '{ch}': "))
        chars.append(ch)
        freqs.append(fr)
    huffman_coding(chars, freqs)

# Enter number of characters: 4
# Enter character 1: A
# Enter frequency of 'A': 5
# Enter character 2: B
# Enter frequency of 'B': 9
# Enter character 3: C
# Enter frequency of 'C': 12
# Enter character 4: D
# Enter frequency of 'D': 13

# ANS
# A: 110
# B: 111
# C: 10
# D: 0

#TC = O(nlogn)
#SC = O(n)