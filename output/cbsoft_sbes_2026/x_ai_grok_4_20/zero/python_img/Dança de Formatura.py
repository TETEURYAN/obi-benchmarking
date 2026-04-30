
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

pos_to_student = [0] * (N * M + 1)
for i in range(1, N + 1):
    for j in range(1, M + 1):
        student = (i - 1) * M + j
        pos_to_student[student] = (i, j)

final_grid = [[0] * M for _ in range(N)]
for r in range(1, N + 1):
    for c in range(1, M + 1):
        orig_r, orig_c = pos_to_student[r * M - M + c] if M > 0 else (r, c)
        final_r = row_perm[r]
        final_c = col_perm[c]
        student = (orig_r - 1) * M + orig_c
        final_grid[final_r - 1][final_c - 1] = student

for i in range(N):
    print(' '.join(map(str, final_grid[i])))
