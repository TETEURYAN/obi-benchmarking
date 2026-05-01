
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
        num = grid[i][j]
        pos[num] = (i, j)

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

def find_row_perm():
    perm = [0] * L
    for i in range(L):
        perm[i] = row_target[row_pos[i]]
    return perm

def find_col_perm():
    perm = [0] * C
    for j in range(C):
        perm[j] = col_target[col_pos[j]]
    return perm

def apply_row_swap(a, b):
    row_pos[a], row_pos[b] = row_pos[b], row_pos[a]

def apply_col_swap(a, b):
    col_pos[a], col_pos[b] = col_pos[b], col_pos[a]

def cycle_decomposition(perm, size):
    vis = [False] * size
    cycles = []
    for i in range(size):
        if vis[i]:
            continue
        if perm[i] == i:
            vis[i] = True
            continue
        cycle = []
        x = i
        while not vis[x]:
            vis[x] = True
            cycle.append(x)
            x = perm[x]
        if len(cycle) > 1:
            cycles.append(cycle)
    return cycles

operations = []

row_perm = find_row_perm()
row_cycles = cycle_decomposition(row_perm, L)
for cycle in row_cycles:
    for i in range(1, len(cycle)):
        x = cycle[0]
        y = cycle[i]
        operations.append(('L', x + 1, y + 1))
        apply_row_swap(x, y)

col_perm = find_col_perm()
col_cycles = cycle_decomposition(col_perm, C)
for cycle in col_cycles:
    for i in range(1, len(cycle)):
        x = cycle[0]
        y = cycle[i]
        operations.append(('C', x + 1, y + 1))
        apply_col_swap(x, y)

print(len(operations))
for op in operations:
    print(op[0], op[1], op[2])
