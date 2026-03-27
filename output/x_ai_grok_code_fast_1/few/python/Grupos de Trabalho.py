import sys

input_data = sys.stdin.read().split()
idx = 0
E = int(input_data[idx]); idx += 1
M = int(input_data[idx]); idx += 1
D = int(input_data[idx]); idx += 1
amigos = []
for _ in range(M):
    x = int(input_data[idx]); idx += 1
    y = int(input_data[idx]); idx += 1
    amigos.append((x, y))
inimigos = []
for _ in range(D):
    u = int(input_data[idx]); idx += 1
    v = int(input_data[idx]); idx += 1
    inimigos.append((u, v))
group = [0] * (E + 1)
num_groups = E // 3
for g in range(num_groups):
    i = int(input_data[idx]); idx += 1
    j = int(input_data[idx]); idx += 1
    k = int(input_data[idx]); idx += 1
    group[i] = g
    group[j] = g
    group[k] = g
violations = 0
for x, y in amigos:
    if group[x] != group[y]:
        violations += 1
for u, v in inimigos:
    if group[u] == group[v]:
        violations += 1
print(violations)