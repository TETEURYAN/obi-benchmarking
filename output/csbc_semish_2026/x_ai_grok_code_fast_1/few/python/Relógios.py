import sys
import heapq

input_data = sys.stdin.read().split()
idx = 0
L = int(input_data[idx])
idx += 1
C = int(input_data[idx])
idx += 1
K = int(input_data[idx])
idx += 1

grid = []
for i in range(L):
    row = []
    for j in range(C):
        row.append(int(input_data[idx]))
        idx += 1
    grid.append(row)

INF = float('inf')
dist = [[INF] * C for _ in range(L)]
dist[0][0] = 0

pq = [(0, 0, 0)]  # (tempo, i, j)

directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

while pq:
    t, i, j = heapq.heappop(pq)
    if t > dist[i][j]:
        continue
    for di, dj in directions:
        ni, nj = i + di, j + dj
        if 0 <= ni < L and 0 <= nj < C:
            next_t = t + 1
            can_go = False
            if grid[ni][nj] == -1:  # funcionando
                can_go = True
            else:  # parado
                if next_t % K == grid[ni][nj]:
                    can_go = True
                elif grid[i][j] == -1:  # posso esperar
                    current = next_t % K
                    P = grid[ni][nj]
                    D = (P - current) % K
                    next_t += D
                    can_go = True
            if can_go and next_t < dist[ni][nj]:
                dist[ni][nj] = next_t
                heapq.heappush(pq, (next_t, ni, nj))

if dist[L-1][C-1] == INF:
    print(-1)
else:
    print(dist[L-1][C-1])