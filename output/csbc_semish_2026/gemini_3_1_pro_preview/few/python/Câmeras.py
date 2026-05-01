import sys
from collections import deque

input_data = sys.stdin.read().split()
if not input_data:
    exit()

N = int(input_data[0])
M = int(input_data[1])
K = int(input_data[2])

observed = [[False] * N for _ in range(M)]

idx = 3
for _ in range(K):
    c = int(input_data[idx]) - 1
    r = int(input_data[idx+1]) - 1
    d = input_data[idx+2]
    idx += 3
    
    if d == 'N':
        for i in range(r, -1, -1):
            observed[i][c] = True
    elif d == 'S':
        for i in range(r, M):
            observed[i][c] = True
    elif d == 'L':
        for j in range(c, N):
            observed[r][j] = True
    elif d == 'O':
        for j in range(c, -1, -1):
            observed[r][j] = True

if observed[0][0] or observed[M-1][N-1]:
    print('N')
    exit()

q = deque([(0, 0)])
visited = [[False] * N for _ in range(M)]
visited[0][0] = True

while q:
    r, c = q.popleft()
    
    if r == M - 1 and c == N - 1:
        print('S')
        exit()
        
    for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
        nr, nc = r + dr, c + dc
        if 0 <= nr < M and 0 <= nc < N:
            if not observed[nr][nc] and not visited[nr][nc]:
                visited[nr][nc] = True
                q.append((nr, nc))

print('N')