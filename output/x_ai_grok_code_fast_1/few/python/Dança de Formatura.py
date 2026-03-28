import sys

data = sys.stdin.read().split()
idx = 0
N = int(data[idx]); idx += 1
M = int(data[idx]); idx += 1
P = int(data[idx]); idx += 1
row_at_pos = list(range(N + 1))
col_at_pos = list(range(M + 1))
for _ in range(P):
    op = data[idx]; idx += 1
    a = int(data[idx]); idx += 1
    b = int(data[idx]); idx += 1
    if op == 'L':
        row_at_pos[a], row_at_pos[b] = row_at_pos[b], row_at_pos[a]
    else:
        col_at_pos[a], col_at_pos[b] = col_at_pos[b], col_at_pos[a]
for i in range(1, N + 1):
    line = []
    for j in range(1, M + 1):
        aluno = (row_at_pos[i] - 1) * M + col_at_pos[j]
        line.append(str(aluno))
    print(' '.join(line))