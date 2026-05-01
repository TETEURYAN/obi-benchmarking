
import sys
from itertools import combinations

input = sys.stdin.read
data = input().split()

L = int(data[0])
C = int(data[1])
P = int(data[2])

blacks = set()
index = 3
for i in range(P):
    x = int(data[index])
    y = int(data[index + 1])
    blacks.add((x - 1, y - 1))
    index += 2

N = L * C
positions = []
pos_to_idx = {}
idx = 0
for i in range(L):
    for j in range(C):
        if (i, j) not in blacks:
            positions.append((i, j))
            pos_to_idx[(i, j)] = idx
            idx += 1

M = len(positions)
if M == 0:
    print(0)
    sys.exit(0)

adj = [[] for _ in range(M)]
dirs = [(-1, 0), (1, 0), (0, -1), (0, 1)]

for a in range(M):
    x, y = positions[a]
    for dx, dy in dirs:
        nx, ny = x + dx, y + dy
        if 0 <= nx < L and 0 <= ny < C and (nx, ny) not in blacks:
            b = pos_to_idx[(nx, ny)]
            if b > a:
                adj[a].append(b)
                adj[b].append(a)

max_count = 0
ALL = 1 << M

for mask in range(ALL):
    if bin(mask).count('1') <= max_count:
        continue
    valid = True
    for i in range(M):
        if (mask & (1 << i)) == 0:
            continue
        x, y = positions[i]
        has_black = False
        for dx, dy in dirs:
            nx, ny = x + dx, y + dy
            if (nx, ny) in blacks:
                has_black = True
                break
        if not has_black:
            valid = False
            break
        for j in adj[i]:
            if mask & (1 << j):
                valid = False
                break
        if not valid:
            break
    if valid:
        max_count = bin(mask).count('1')

print(max_count)
