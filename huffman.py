import heapq

n = int(input("Enter number of characters: "))
heap = []
count = 0

# Input
for _ in range(n):
    ch, f = input().split()
    heapq.heappush(heap, (int(f), count, ch))
    count += 1

# Build Huffman Tree
while len(heap) > 1:
    f1, _, left = heapq.heappop(heap)
    f2, _, right = heapq.heappop(heap)

    heapq.heappush(heap, (f1 + f2, count, (left, right)))
    count += 1

print("\nHuffman Codes:")

def code(node, s=""):
    if isinstance(node, str):
        print(node, ":", s)
        return

    l, r = node
    code(l, s + "0")
    code(r, s + "1")

code(heap[0][2])    