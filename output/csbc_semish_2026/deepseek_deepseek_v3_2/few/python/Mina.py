import sys
import heapq

input_data = sys.stdin.read().split()
if not input_data:
    exit()

N = int(input_data[0])
grid = []
idx = 1
for i in range(N):
    row = list(map(int, input_data[idx:idx + N]))
    grid.append(row)
    idx += N

INF = 10**9
dist = [[INF] * N for _ in range(N)]
dist[0][0] = grid[0][0]  # custo inicial é 0 ou 1? se grid[0][0]==0, custo 0, se 1, custo 1 (mas início nunca bloqueado)

heap = []
heapq.heappush(heap, (dist[0][0], 0, 0))

while heap:
    d, x, y = heapq.heappop(heap)
    if d > dist[x][y]:
        continue
    
    for dx, dy in [(1,0), (-1,0), (0,1), (0,-1)]:
        nx, ny = x + dx, y + dy
        if 0 <= nx < N and 0 <= ny < N:
            new_cost = d + grid[nx][ny]
            if new_cost < dist[nx][ny]:
                dist[nx][ny] = new_cost
                heapq.heappush(heap, (new_cost, nx, ny))

print(dist[N-1][N-1])