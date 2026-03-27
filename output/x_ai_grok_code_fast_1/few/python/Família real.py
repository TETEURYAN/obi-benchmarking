import sys
from collections import deque

input_data = sys.stdin.read().split()
idx = 0
N = int(input_data[idx])
idx += 1
M = int(input_data[idx])
idx += 1
pais = [0] * (N + 1)
for i in range(1, N + 1):
    pais[i] = int(input_data[idx])
    idx += 1
compareceram = set()
for i in range(M):
    compareceram.add(int(input_data[idx]))
    idx += 1
filhos = [[] for _ in range(N + 1)]
for i in range(1, N + 1):
    filhos[pais[i]].append(i)
nivel = [-1] * (N + 1)
nivel[0] = 0
q = deque([0])
while q:
    u = q.popleft()
    for v in filhos[u]:
        if nivel[v] == -1:
            nivel[v] = nivel[u] + 1
            q.append(v)
max_gen = max(nivel) if N > 0 else 0
result = []
for g in range(1, max_gen + 1):
    total_desc = sum(1 for i in range(1, N + 1) if nivel[i] == g)
    presentes = sum(1 for i in range(1, N + 1) if nivel[i] == g and i in compareceram)
    if total_desc > 0:
        perc = (presentes / total_desc) * 100
    else:
        perc = 0.0
    result.append(f"{perc:.2f}")
print(" ".join(result))