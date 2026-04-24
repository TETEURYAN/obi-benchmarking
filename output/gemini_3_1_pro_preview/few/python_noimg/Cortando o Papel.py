import sys
from collections import defaultdict

input_data = sys.stdin.read().split()
if not input_data:
    exit()

n = int(input_data[0])
A = [int(x) for x in input_data[1:n+1]]

compressed_A = []
for x in A:
    if not compressed_A or compressed_A[-1] != x:
        compressed_A.append(x)

arr = [0] + compressed_A + [0]

events = defaultdict(int)

for i in range(1, len(arr) - 1):
    prev = arr[i-1]
    curr = arr[i]
    nxt = arr[i+1]
    
    if curr > prev and curr > nxt:
        events[curr] -= 1
    elif curr < prev and curr < nxt:
        events[curr] += 1

pieces = 2
max_pieces = 2

for h in sorted(events.keys()):
    pieces += events[h]
    if pieces > max_pieces:
        max_pieces = pieces

print(max_pieces)