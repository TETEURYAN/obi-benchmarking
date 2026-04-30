
import sys

input = sys.stdin.read
data = input().split()

L = int(data[0])
C = int(data[1])
N = L * C

grid = []
index = 2
for i in range(L):
    row = []
    for j in range(C):
        row.append(int(data[index]))
        index += 1
    grid.append(row)

pos = [0] * (N + 1)
for i in range(L):
    for j in range(C):
        chair = grid[i][j]
        pos[chair] = (i, j)

row_target = [0] * L
col_target = [0] * C
for num in range(1, N + 1):
    orig_r = (num - 1) // C
    orig_c = (num - 1) % C
    curr_r, curr_c = pos[num]
    row_target[curr_r] = orig_r
    col_target[curr_c] = orig_c

row_pos = list(range(L))
col_pos = list(range(C))

ops = []

def swap_rows(a, b):
    if a == b:
        return
    ops.append(('L', a + 1, b + 1))
    row_pos[a], row_pos[b] = row_pos[b], row_pos[a]
    row_target[a], row_target[b] = row_target[b], row_target[a]

def swap_cols(a, b):
    if a == b:
        return
    ops.append(('C', a + 1, b + 1))
    col_pos[a], col_pos[b] = col_pos[b], col_pos[a]
    col_target[a], col_target[b] = col_target[b], col_target[a]

for i in range(L):
    target = row_target[i]
    for j in range(i, L):
        if row_pos[j] == target:
            swap_rows(i, j)
            break

for i in range(C):
    target = col_target[i]
    for j in range(i, C):
        if col_pos[j] == target:
            swap_cols(i, j)
            break

print(len(ops))
for op in ops:
    print(op[0], op[1], op[2])
