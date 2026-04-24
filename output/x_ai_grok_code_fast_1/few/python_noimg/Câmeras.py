import sys
from collections import deque

input_data = sys.stdin.read().split()
idx = 0
N = int(input_data[idx])
idx += 1
M = int(input_data[idx])
idx += 1
K = int(input_data[idx])
idx += 1

proibida = [[False] * (M + 1) for _ in range(N + 1)]

for _ in range(K):
    Ci = int(input_data[idx])
    idx += 1
    Li = int(input_data[idx])
    idx += 1
    Di = input_data[idx]
    idx += 1
    if Di == 'N':
        for linha in range(Li, 0, -1):
            proibida[Ci][linha] = True
    elif Di == 'S':
        for linha in range(Li, M + 1):
            proibida[Ci][linha] = True
    elif Di == 'L':
        for coluna in range(Ci, N + 1):
            proibida[coluna][Li] = True
    elif Di == 'O':
        for coluna in range(Ci, 0, -1):
            proibida[coluna][Li] = True

visited = [[False] * (M + 1) for _ in range(N + 1)]
q = deque()
if not proibida[1][1]:
    q.append((1, 1))
    visited[1][1] = True

found = False
while q:
    x, y = q.popleft()
    if x == N and y == M:
        found = True
        break
    for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
        nx, ny = x + dx, y + dy
        if 1 <= nx <= N and 1 <= ny <= M and not proibida[nx][ny] and not visited[nx][ny]:
            visited[nx][ny] = True
            q.append((nx, ny))

if found:
    print('S')
else:
    print('N')