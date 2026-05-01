
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
cells = [(i, j) for i in range(L) for j in range(C)]

def is_valid_white(pos, whites):
    r, c = pos
    neighbors = 0
    for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
        nr, nc = r + dr, c + dc
        if 0 <= nr < L and 0 <= nc < C:
            neigh_pos = (nr, nc)
            if neigh_pos in blacks:
                neighbors += 1
            elif neigh_pos in whites:
                return False
    return neighbors >= 1

max_white = 0
empty_cells = [pos for pos in cells if pos not in blacks]
K = len(empty_cells)

for k in range(K, -1, -1):
    for combo in combinations(range(K), k):
        whites = set()
        valid = True
        for idx in combo:
            pos = empty_cells[idx]
            if not is_valid_white(pos, whites):
                valid = False
                break
            whites.add(pos)
        if valid:
            max_white = k
            break
    if max_white > 0:
        break

print(max_white)
