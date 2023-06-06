import heapq

ctr = 0
tempchr = []
chr = []
freq = {}
enc = {}


with open("input.txt") as file:

    for line in file:
        tempchr.append(list(line))
        ctr += 1


for i in range(ctr):
    for item in tempchr[i]:
        chr.append(item)
        if item in freq:
            freq[item] += 1
        else:

            freq[item] = 1

print("Frequency Table:\nChar\tFreq")

for key, value in freq.items():
    if key =="\n":
        print(f'\\n\t{value}')
    else:
        print(f'{key}\t{value}')

print("\n")

class Node:
    def __init__(self, char=None, frequency=0, left=None, right=None):
        self.char = char
        self.frequency = frequency
        self.left = left
        self.right = right

    def __lt__(self, other):
        if self.frequency == other.frequency:
            return self.char < other.char
        return self.frequency < other.frequency


def build_huffman_tree():
    heap = []
    for char, frq in freq.items():
        node = Node(char=char, frequency=frq)
        heapq.heappush(heap, node)

    while len(heap) > 1:
        left = heapq.heappop(heap)
        right = heapq.heappop(heap)
        parent = Node(frequency=left.frequency + right.frequency, left=left, right=right)
        heapq.heappush(heap, parent)

    return heap[0]


print("Encode Table:\nChar  Enc")

def encode(node, prefix=''):
    global enc
    if node.char:
        if node.char == "\n":
            print(f"\\n\t{prefix}")
        else:
            print(f"{node.char}\t{prefix}")
        enc[node.char] = prefix

    else:
        encode(node.left, prefix + '0')
        encode(node.right, prefix + '1')



HuffmanTree = build_huffman_tree()

encode(HuffmanTree)


s = ""
with open('encode.txt', 'w+') as f1:
    for x in range(len(chr)):
        for item in chr[x]:
            if item in enc:
                s += enc.get(chr[x])
    f1.write(s)
    f1.close()

def decode(enctxt, root):
    currnode = root
    dectxt = ''
    for bit in enctxt:
        if bit == '0':
            currnode = currnode.left
        else:
            currnode = currnode.right
        if currnode.char:
            dectxt += currnode.char
            currnode = root
    return dectxt


with open('decode.txt', 'w+') as f2:
    f2.write(decode(s, HuffmanTree))
    f2.close()