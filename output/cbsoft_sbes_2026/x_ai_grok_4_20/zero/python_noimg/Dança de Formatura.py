
import sys

input = sys.stdin.read
data = input().split()

N = int(data[0])
M = int(data[1])
P = int(data[2])

row_perm = list(range(N + 1))
col_perm = list(range(M + 1))

idx = 3
for _ in range(P):
    op = data[idx]
    a = int(data[idx + 1])
    b = int(data[idx + 2])
    if op == 'L':
        row_perm[a], row_perm[b] = row_perm[b], row_perm[a]
    else:
        col_perm[a], col_perm[b] = col_perm[b], col_perm[a]
    idx += 3

pos = [0] * (N * M + 1)
for r in range(1, N + 1):
    for c in range(1, M + 1):
        orig_r = row_perm[r]
        orig_c = col_perm[c]
        student = (orig_r - 1) * M + orig_c
        pos[(r - 1) * M + c] = student

for i in range(1, N * M + 1):
    if i % M == 0:
        print(pos[i])
    else:
        print(pos[i], end=' ')
