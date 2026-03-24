import sys
from collections import deque

data = sys.stdin.read().split()
if not data:
    sys.exit()

N = int(data[0])  # colunas
M = int(data[1])  # linhas
K = int(data[2])

blocked = [[False] * (N + 1) for _ in range(M + 1)]

idx = 3
for _ in range(K):
    c = int(data[idx])
    l = int(data[idx + 1])
    d = data[idx + 2]
    idx += 3

    if d == 'N':
        for r in range(1, l + 1):
            blocked[r][c] = True
    elif d == 'S':
        for r in range(l, M + 1):
            blocked[r][c] = True
    elif d == 'L':
        for col in range(c, N + 1):
            blocked[l][col] = True
    else:  # 'O'
        for col in range(1, c + 1):
            blocked[l][col] = True

if blocked[1][1] or blocked[M][N]:
    print('N')
    sys.exit()

visited = [[False] * (N + 1) for _ in range(M + 1)]
q = deque()
q.append((1, 1))
visited[1][1] = True

dirs = [(1, 0), (-1, 0), (0, 1), (0, -1)]

while q:
    r, c = q.popleft()
    if r == M and c == N:
        print('S')
        sys.exit()

    for dr, dc in dirs:
        nr = r + dr
        nc = c + dc
        if 1 <= nr <= M and 1 <= nc <= N and not visited[nr][nc] and not blocked[nr][nc]:
            visited[nr][nc] = True
            q.append((nr, nc))

print('N')